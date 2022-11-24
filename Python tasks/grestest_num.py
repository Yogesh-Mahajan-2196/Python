num = [10, 50, 60, 120, 40, 90, 65]

highest_num = num[0]

for number in num:
    if number>highest_num:
        highest_num = number

print(highest_num)