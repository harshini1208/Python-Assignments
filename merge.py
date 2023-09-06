#10.Write a Python script to merge two Python dictionaries.
d1 = {'a': 100, 'b': 200, 'c':300}  
d2 = {'d': 300, 'e': 400, 'f':500} 
d1.update(d2)
print(d1)