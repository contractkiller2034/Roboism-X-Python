def is_prime(n):
    if (n==1):
        return False
    for i in range(2,int(n/2)+1):
        if (n%i==0):
            return False
    else:
        return True


try:
    n1=int(input("Start Limit: "))
    n2=int(input("End Limit: "))
    for i in range(n1,n2):
             if (is_prime(i)):
                 print(i)
except ValueError :
                print('Please enter only Integer values!!')

