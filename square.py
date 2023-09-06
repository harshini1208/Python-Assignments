#4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
N = 16
d = dict()
for i in range(1,N):
    d[i] = i * i
print(d)   