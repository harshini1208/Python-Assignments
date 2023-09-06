#5.Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string : 'marolix technology'
mystr="marolix technology"
print("the input string is :,mystr")
myDict=dict()
for character in mystr:
    if character in mystr:
        myDict[character]+=1
    else:
        myDict[character]=1
print("The dictionary created from characters of the string is :")
print(myDict)            