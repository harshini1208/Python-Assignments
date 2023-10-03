#1.write a program to create a calculator using functions (sum,sub,mul,div).
def mul(a,b):
    print(a*b)

def sum(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def div(a,b):
    print(a/b)

a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
choice = int(input("enter your choice number: "))
if (choice == 1):
    sum(a,b)
elif (choice == 2):
    sub(a,b)
elif (choice == 3):
    mul(a,b)
elif (choice == 4):
    div(a,b)
else:
    print("enter the valid choice number")  