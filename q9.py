string = input()

list1 = string.split()
for i in range(0,len(list1)):
    list1[i] = int(list1[i])
list1.sort()
print(list1)
