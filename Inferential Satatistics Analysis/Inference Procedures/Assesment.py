# Code made for : Sergio Andrés Díaz Ariza
# Specialization--> Statistics in Python Coursera
# 30 March, 2021
# License MIT


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#1. Write a function that inputs an integers and returns the negative

def negative_int(x):
    out =-x
    return out

print(negative_int(4))

#2. Write a function that inputs a list of integers and returns the minimum value

def min_list(lst):
    out = min(lst)
    return out
lst = [-3, 0, 2, 100, -1, 2]
print(min_list(lst))

#3.Challenge Problem
# Write a function that take in four arguments: lst1, lst2, str1, str2, and returns a pandas DataFrame
# that has the first column labeled str1 and the second column labaled str2, that have values lst1 and
# lst2 scaled to be between 0 and 1.

def DataFrame_make(lst1,lst2,str1,str2):
    df = pd.DataFrame({str1:lst1,str2:lst2})
    return df

lst1 = np.random.randint(-234, 938, 100)
lst2 = np.random.randint(-522, 123, 100)
str1 = 'one'
str2 = 'alpha'

print(DataFrame_make(lst1,lst2,str1,str2))

