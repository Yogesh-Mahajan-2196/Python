'''
num = int(input('enter a number :- '))

flag = False
for i in range(2 , num):
    if (num % i) == 0:
        flag = True
        break

if flag:
    print(f'{num} is not a prime number.')
else:
    print(f'{num} is a prime number.')


'''
num1 = int(input('enter a start value to find prime numbers:- '))
num2 = int(input('enter a last value to find a prime numbers:- '))

for i in range(num1,num2+1):
    if num1 > 1:
        for j in range(2,i):
            if (i%j) == 0:
                break       
        else:
            print(i)