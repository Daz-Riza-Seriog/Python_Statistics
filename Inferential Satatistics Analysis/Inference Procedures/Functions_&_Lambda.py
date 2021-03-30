# Code made for : Sergio Andrés Díaz Ariza
# Specialization--> Statistics in Python Coursera
# 30 March, 2021
# License MIT

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Define a function

#def function_name(arguments):
#    code
#    return output

def sum_x_y(x,y):
    out= x+y
    return out

print('We look the fuction x+y in action:\t', sum_x_y(2,3))

def get_max(lst):
    current_max = lst[0]
    for element in lst[1:]:
        if element > current_max:
            current_max=element
    return current_max

print("Look a function with iterable for a max in a list:\t",get_max([1,2,3]))

## Lambda Function / Anonymus fuction

Handl_func=(lambda x,y: x+y)(2,3)
print("Handle Function lambda:\t",Handl_func)

g = lambda x:x**2
print("function g:\t",g(5))

f = lambda x:np.sin(x)
x = np.linspace(-np.pi,np.pi,100)
y = [f(i) for i in x]

plt.figure(1)
plt.plot(x,y)


#Do he same but in list comprehension wit lambda function

y1 = [(lambda w:np.sin(w))(w) for w in x]
plt.figure(2)
plt.plot(x,y1)
plt.show()

