#write a python program to delete element of given index in list.
print("enter the size of List:")
total=int(input())
lst=[]
print("enter" +str(total)+"elements:")
for i in range(total):
    lst.append(input())
print("Enter the Index Value:")
index=int(input())    
if index<total:
    lst.pop(index)
    print("\n The New list is:")
    for i in range(total-1):
        print(end=lst[i]+ " ")
else:
    print("\n Invalid Index Number!")         
