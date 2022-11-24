'''
string = 'abjajkbjk afnefig[vn qfqkbabebn'

duplicate = []

for char in string:
    if string.count(char)>1:
        if char not in duplicate:
            duplicate.append(char)

print(duplicate)


'''
'''
def removeDuplicate(str):
    s=set(str)
    s="".join(s)
    print("Without Order:",s)
    t=""
    for i in str:
        if(i in t):
            pass
        else:
            t=t+i
        print("With Order:",t)
     
str="geeks for geeks"
removeDuplicate(str)

'''

string = "My name is Valddimir Putin"


for i in range(0,len(string)):
    count = 1;
    for j in range(i+1, len(string)):
        if (string[i] == string[j] and string[i] != ""):
            count += 1

            string = string[:j] + '0' + string[j+1:];


    if(count > 1 and string[i] != '0'):  
        print(string[i], end=" ");
