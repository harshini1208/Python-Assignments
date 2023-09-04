#write a python program to delete given elemet from the list
list=int(input("enter the number of elements you want in list"))
lst=[]
#adding elements to the list
for i in range(0,list):
    s=int(input("enter value for index "+str(i)+":"))
    lst.append(s)
num=int(input("enter a number to remove from list:"))
    #removing element num from list
lst.remove(num)
print("List after removing",num, "=",lst)


