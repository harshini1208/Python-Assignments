#7.Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
new_dict = d2
for i, j in d1.items():  
    if i in d2:  
        new_dict[i] = j + d2[i]  
    else:   
        new_dict[i] = j  
print(new_dict)