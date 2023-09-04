#3.write a python program to print even and odd numbers seperatly in list.
numList=[]
even=[]
odd=[]
num=int(input("enter total number of list elements:"))
for i in range(1,num+1):
    value=int(input("enter value of %delement:"%i))
    numList.append(value)
for j in range(num):
    if(numList[j]%2==0):
        even.append(numList[j])
    else:
        odd.append(numList[j])
print("element in even list is :",even)
print("elements in odd list is :",odd)


