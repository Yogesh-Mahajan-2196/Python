num = int(input('enter the number :- '))
b = str(num)
a = len(b)
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   print(digit)
   sum += digit ** b
   print(sum)
   temp //= 10
   print(temp)

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")