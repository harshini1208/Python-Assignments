#2.Write a Python script to check whether a given key already exists in a dictionary.
dic = {"Fruit":"apple", "cars":"Audi"}
b = "car"
if b in dic.keys():
    print("This key already exists in a dictionary")
else: 
    print("This key is not exists in a dictionary")

