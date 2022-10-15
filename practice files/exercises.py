def letterCase(x:str)->str:
    counter1=0
    counter2=0
    for letter in x:
        if letter.isupper():
            counter1+=1
        elif letter.islower():
            counter2+=1
        else:
            print('Enter only string Please!')
    print(f' Upper case letters: {counter1} \n Lower case letters: {counter2}')


class Mycar:
    def __init__(this,name,age):
        this.name=name
        this.age=age
    def get(this):
        print(f'name: {this.name}\nage: {this.age}')


class Human:
    def __init__(self,name, age:int,run_speed:list) -> None:
        self.name=name
        self.age=age
        self.run_speed=run_speed
    

    def __str__(self) -> str:
        return f'Name:{self.name}\nAge: {self.age}\nRun Speed: {self.run_speed}'

John=Human('John',30,[3,6])
print(John)

