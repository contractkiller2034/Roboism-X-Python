def list_maker(string):
    a = 0
    for i in string:
         if i.isdigit():
             a = a*10 + int(i)
         else:
            list1.append(a)
            a = 0
    list1.append(a)
    return list1

list1 = []
string = input("ENTER LIST(use spaces between elements) : ")
list1 = list_maker(string)

list1.sort()
duplicate = -1
while duplicate == -1:
    for i in range(0,len(list1)-1):
        if list1[i] == list1[i+1]:
            duplicate = list1[i]
            break
print(duplicate)

