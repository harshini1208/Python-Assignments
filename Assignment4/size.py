#write a python program to check the sizes of given two lists are same.
list1 = [input('enter input:')]
list2 = [input('enter input:')]

list1.sort()
list2.sort()
 
if list1 == list2:
    print("The lists sizes are same")
else:
    print("The lists sizes are not same")