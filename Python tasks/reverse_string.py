'''
## 1. Reverse the String

str1 = 'JaVaj'

str2 = str1.casefold()
str3 = reversed(str2)

print(list[str2], list(str3))

if list(str2) == list(str3):
    print('Palindrome')

else:
    print('Not Palindrome')
'''

## 2. Reverse String
while True:
    name = input('enter ur name:-')

    if (name == name[::-1]):
        print(f'{name} is Palindrome Name')
    else:
        print(f'{name} is not Palindrome Name')
