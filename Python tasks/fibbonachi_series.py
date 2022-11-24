
num = int(input('enter a number for a series:- '))

first = 0
second = 1

for i in range(num):
    if i <= 1:
        result = i
        #print(result)

    else:
        result = first + second
        first = second
        second = result
    
    print(result)
'''

def fibonachi_series(num):
    p , q = 0 , 1
    while p<num:
        print(p)
        p , q = q , p+q
fibonachi_series(10)

'''