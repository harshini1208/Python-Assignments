#2.write a python program to find the sum of list elements.
lst=[]
num=int(input('how many numbers:'))
for n in range(num):
    numbers=int(input('enter number'))
    lst.append(numbers)
print("sum of elements in given list is:",sum(lst))
