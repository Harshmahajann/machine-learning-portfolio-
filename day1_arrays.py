# DAY1 

import numpy as np

#creating a new array
a = np.array([1, 2, 3, 4, 5]) 
zeros = np.zeros(5) #array will all zeros


# basic ops
print(a+5)
print(a-2)
print(a*3)
print(a/2)
print(a**2)

# array with array
b = np.array([10, 20, 30, 40, 50])
print(a + b)      
print(a * b)

print(a.shape)   
print(a.dtype)

sales = np.array([1200, 1450, 980, 1600, 1100, 2000, 1750])  # a week of daily sales

print(sales.sum())    # total for the week
print(sales.mean())   # average day
print(sales.max())    # best day
print(sales.min())    # worst day