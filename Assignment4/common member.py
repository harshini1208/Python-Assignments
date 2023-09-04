#Write a Python function that takes two lists and returns True if they have at least one common member.
def check_common(first,second):
    for item in first:
        if item in second:
            return True
    return False
length=int(input("enter List length:"))
list1=[]
for _ in range(length):
    temp=int(input("enter list1 item :"))
    list1.append(temp)
length=int(input("enter list2 length:"))
list2=[]
for _ in range(length):
    temp=int(input("enter list2 item:"))
    list2.append(temp)
if check_common(list1,list2):
    print("At least one common member exists between two lists")
else:
    print("No common memeber exists between the lists")        