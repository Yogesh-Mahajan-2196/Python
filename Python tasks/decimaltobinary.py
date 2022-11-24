'''
def DecimalToBinary(num):
    if num>=1:
        DecimalToBinary(num//2)
    print(num%2, end='')

DecimalToBinary(10)

'''

def binarytodecimal(num):
    decimal = 0
    power = 1
    while num>0:
        res = num%10
        num = num//10
        decimal = decimal + res*power
        power = power*2

    return decimal

print(binarytodecimal(111))