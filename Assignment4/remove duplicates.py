#11.Write a Python program to remove duplicates from a list.
def remove(duplicates):
    final_list=[]
    for num in duplicates:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate=[2,3,4,10,20,5,2,20,4]
print(remove(duplicate))  

#taking input from user
a=[]
n=int(input("enter number of elements in the list:"))
for x in range(0,n):
    element=int(input("enter element"+str(x+1)+":"))
    a.append(element)
b=set()
unique=[]
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("Non duplicate items:")
print(unique)        
