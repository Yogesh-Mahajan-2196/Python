'''
string = input('enter any stirng :- ')
chara = input('please enter a character which u want to count :- ')

count = 0

for i in range(len(string)):
    if string[i] == chara:
        count += 1
print(count)
'''
'''
name = input('enter ur full name : ')
dict1 = dict()

for i in name:
    count1 = name.count(i)
    dict1[i] = count1
print(dict1)

'''
