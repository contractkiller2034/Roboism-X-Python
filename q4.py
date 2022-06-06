def doubbler(s):
    n=len(s)
    output=" "
    for i in range(n):
        output += (s[i]*2)
    return output

s1=input("enter the string ")
print(doubbler(s1))