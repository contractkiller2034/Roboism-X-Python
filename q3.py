def calculator(n1, operator, n2) :
    output = 0
    if operator =='+' :
        output = n1 + n2
    elif operator =='-' :
        output = n1 - n2
    elif operator == '*' :
        output = n1*n2
    elif operator == '/' :
        output = n1/n2
    else:
        print('invalid operator!!')
    return output


try:
    num1 = int(input('Enter 1st number ; '))
    Operator = input('Operator ; ')
    num2 = int(input('Enter 2nd number ; '))
    print(calculator(num1, Operator, num2))
except ValueError:
            print('arithmetic operations can be carried out only on numbers!! ')