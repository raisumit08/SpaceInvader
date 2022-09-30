import math as m
def Primeornot(n):
    for i in range(2,n-1):
        if n%i==0:
            count = 1
            break
        else:
            count = 0
    return count


def Primeornot2(n):
    for i in range(2,n/2):
        if n%i==0:
            count = 1
            break
        else:
            count = 0
    return count


'''def Primeornot3(n):
    for i in range(2,m.sqrt(n)):
        if n%i==0:
            count = 1
            break
        else:
            count = 0
    return count'''


n = int(input("Enter an integer: "))
check = Primeornot(n)
if(check == 1):
    print("Not a Prime number")
else:
    print("A Prime number")


check = Primeornot2(n)
if(check == 1):
    print("Not a Prime number")
else:
    print("A Prime number")


'''check = Primeornot3(n)
if(check == 1):
    print("Not a Prime number")
else:
    print("A Prime number")'''