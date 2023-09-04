#Write a Python program to remove a specified column from a given nested list.
#Original Nested list:
#[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
#After removing 1st column:
#[[2, 3], [4, 5], [1, 1]]

lst = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print("the original list is :"+str(lst))
#using pop()+list comprehension
[j.pop(0) for j in lst]
print("the modified mesh after column deletion:"+str(lst))

