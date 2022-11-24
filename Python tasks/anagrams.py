
def anagramcheck(str1,str2):
    if (sorted(str1) == sorted(str2)):
        return True
    else:
        return False

str1 = input('enter string1 - ')
str2 = input('enter string2 - ')

if anagramcheck(str1, str2):
    print(f'{str1} and {str2} is a anagram string')
    
else:
    print('Not a anagram string')


