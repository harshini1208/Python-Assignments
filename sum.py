#6. Write a Python program to sum all the items in a dictionary.
d1 = {'a': 100, 'b': 200, 'c':300}
l =[]
for i in d1:
    l.append(d1[i])
print(sum(l))    