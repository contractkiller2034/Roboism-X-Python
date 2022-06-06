list1 = []
str1 = input('Enter list(use spaces between elements): ')
list1 = str1.split()
print(list1)


def most_frequent(List):
    counter = 0
    num = List[0]


    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num, counter

var = most_frequent(list1)
print(f'The most frequent element in the list is {var[0]} and its frequency is {var[1]}')
