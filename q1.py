list = []
print('Press -1 to end')
n = 0
N = int(input('Enter Number '))
while N != -1 :
    list.append(N)
    N = int(input('Enter Number '))
    print('press -1 to stop')
print(list)
l1 = list.copy()

choice = input('Enter asc, dsc or none ')

if choice == 'asc' :
    list.sort()
    print(list)
elif choice == 'dsc':
    list.reverse()
    print(list)
elif choice == 'none':
    print(l1)
else:
    print('Sorry! Invalid entry')