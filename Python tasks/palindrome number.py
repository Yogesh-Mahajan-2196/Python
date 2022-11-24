
num = int(input('enter any munber :- '))
num2 = num
reverse_num = 0

while num>0:
    remainder = num % 10
    reverse_num = (reverse_num * 10) + remainder
    num = num // 10
    
if num2 == reverse_num:
    print(f'{num2} is a Palindrome Number.')
else:
    print(f'{num2} is not a Palindrome Number.')

