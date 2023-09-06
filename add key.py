#1.Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
employees={}
for i in range(3):
    name=input("enter employee's name :")
    salary=input("enter employee's salary :")
    employees[name]=salary
print(employees)    

##Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
d={0:10,1:20}
print(d)
d[2]=30
print(d)
