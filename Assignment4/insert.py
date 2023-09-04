#write a python program to insert an elemet  at given index location.
#insert element at specific index position
num=[]
print(end="enter the size:")
numSize=int(input())
print(end="enter" +str(numSize)+ "elements:")    
for i in range(numSize):
    num.append(input())
print("\n Enter an Element to Insert:")
element=input()
print(end="At What Index?")
s=int(input())
num.insert(s,element)
numSize=numSize+1
print("\n The New List is:")
for i in range(numSize):
    print(end=num[i]+ " ")
print()  

#insert element at end of the list
print("enter 10 elements of List:")
num=[]
for i in range(10):
    num.insert(i,input())
print("enter element to insert at end :")
element=input()
num.append(element)
print("\n The New List is :")
print(num)