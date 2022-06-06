string = input('Enter a string: ')
sum1 = 0
for i in string:
    if i.isdigit():
        sum1 += int(i)
print(sum1)