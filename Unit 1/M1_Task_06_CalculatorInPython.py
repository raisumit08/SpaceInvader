#Create a calculator in python

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a % b

def expo(a,b):
    return a ** b

def flor(a,b):
    return a // b


def main():
    if add(10,20)==30:
        print("Add functionality is working fine\n")
    
    if sub(30,20)==10:
        print("Sub functionality is working fine\n")

    if mul(10,20)==200:
        print("Multiplication functionality is working fine\n")

    if div(200,20)==10:
        print("Division functionality is working fine\n")

    if mod(200,20)==0:
        print("Modulus functionality is working fine\n")

    if expo(2,4)==16:
        print("Exponential functionality is working fine\n")
    
    if flor(5,2)==2:
        print("Floor Division functionality is working fine\n")

main()