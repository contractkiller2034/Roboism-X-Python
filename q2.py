card = (input("Enter your card number "))
while len(card) != 16 :
     print('card number consists of 16 digits')
     card = input("Enter your card number ")
for i in range(0, len(card)) :
    if i <= 11 :
        print('*', end='')
    else :
        print(card[i], end='')