numbers=[]
for x in range(1,10):
    numbers.append(x)
    print(numbers)


# for bilan karra ajadval tuzish

for num1 in range(1,11):
    for x in range(1,11):
        print(f'{num1}x{x}={num1*x}')
    print('Line Break')
    
sonlar=[1,3,2,4,2,4,7,8,9,11,22,33,44,55,66,77,89]
counter=0
for x in sonlar:
    counter+=x
print(f'Total sum: {counter}')
