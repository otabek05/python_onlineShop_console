import random
import time


class Human:
    def __init__(self, name, hp, run_speed):
        self.name=name
        self.hp=hp
        self.run_speed = run_speed
        
    def __str__(self):
        return self.name
    
class Gun:
    def __init__(self, name, bullets, damage, reload_time):
        self.name=name
        self.bullets=bullets
        self.damage=damage
        self.reload_time=reload_time
        
    def fire(self, human1: Human, human2: Human):
        hp = human2.hp
        distance = 0
        bullets = self.bullets
        
        while True:
            if hp > 0:
                if distance <= 200:
                    print(f"{human1} {human2} ga o'q uzmoqda, {human2} ning {hp} joni qoldi, {distance}m masofaga qochdi.")
                    bullets = bullets - 1
                    hp = hp - random.randint(self.damage[0], self.damage[1])  # [3, 8]
                    distance = distance + random.randint(human2.run_speed[0], human2.run_speed[1])  # 4, 8
                    
                    if bullets <= 0:
                        print("O'qlanmoqda ...")
                        bullets = self.bullets
                        distance = distance + (self.reload_time * random.randint(human2.run_speed[0], human2.run_speed[1]))
                        time.sleep(self.reload_time)
                    time.sleep(1)
                else:
                    print(f"{human2} {human1} dan qochishga muvaffaq bo'ldi!")
                    break
            else:
                print(f"{human1} {human2} ni o'ldirdi.")
                break
                
human1 = Human('Alex', 200, [3, 5])
human2 = Human('John', 200, [4, 8])

desert_eagle = Gun("Desert Eagle", 7, [3, 10], 4)
desert_eagle.fire(human1=human1, human2=human2)

# print( human1 )  # <__main__.Human object at 0x10262bf40>
# print( human2 )

'''
class KvTenglama:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f'{self.a}(x**x)+{self.b}x+{self.c}'

    def __add__(self, other):  # add --> ing. qo'shish
        return KvTenglama(self.a+other.a, self.b+other.b, self.c+other.c)

    def __sub__(self, other):  # subtract --> ing. ayirish
        return KvTenglama(self.a-other.a, self.b-other.b, self.c-other.c)

    def __call__(self):
        return print(f'{self.a}(x**x)+{self.b}x+{self.c}')

    def __gt__(self, other):  # greater than --> ing. dan katta
        return sum([self.a, self.b, self.c]) > sum([other.a, other.b, other.c])
    
    # def __lt__(self, other):  # less than --> ing. dan kichik
    #     pass
    
    def __gte__(self, other):  # greater than or equal
        return sum([self.a, self.b, self.c]) >= sum([other.a, other.b, other.c])
    
    # def __lte__(self, other):  # less  than or equal
    #     pass
        
tenglama1 = KvTenglama(2, 4, 0)
tenglama2 = KvTenglama(4, 2, 3)

# 6(x**x)+6x+3

# print( tenglama1 + tenglama2 )
# print( tenglama1 - tenglama2 )
# tenglama1()

# print( tenglama1 > tenglama2 )
# print( tenglama1 < tenglama2 )
# print( tenglama1 <= tenglama2 )
# print( KvTenglama.__dict__ )
'''



