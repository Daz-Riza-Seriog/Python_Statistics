# Code made for : Sergio Andrés Díaz Ariza
# Specialization--> Statistics in Python Coursera
# 30 March, 2021
# License MIT

import numpy as np
import pandas as pd

########
# List #
########
my_list =[1,'Colorado',4.7]

#You can obtain elements in the list with index
print("Obtain First element:\t",my_list[0])
print("Obtain First element:\t",my_list[2])
print("Obtain First element:\t",my_list[-1]) # Obtaian the last element

#########
# Array #
#########

my_array = np.array([1,2,3])
my_array2 = np.array((1,2,3))
print("Two ways to write a Array, with tupleas and square brackets,",my_array2==my_array)
print("Obtain the element in Array:\t",my_array2[0])

#############################
# Differences Between both  #
#############################

print("Divide the Array by 3:\t",my_array/3)
print("Divide the list by 3:\t","it's not supported TypeError")

# Append
my_list.append('new thing')
print("Append something to list:\t",my_list)

my_array = np.append(my_array,5) #Note: you need rewrite the Array
print("Append something to Array:\t",my_array)


#########################
#   Dictionaries        #
#########################

my_dict = {'key1':'first value','Key2':'Second value'} #it's a curly brackets notation with pair of 'Key' & 'Values'
print("Call the first value of the dictionary:\t",my_dict['key1']) #Note:in the call we use the Key in square brackets

# Add a Value
my_dict['new key']='newest value'
my_dict['int']= 5
print("call the new value:\t",my_dict['new key'])
# "Note Dict has not order how list or Array-->",my_dict[0]


#####################
# DataFrame         #
####################

# Create
df = pd.DataFrame({'col1':range(0,3),'col2':range(3,6)}) #Herea we combaine dicts with DataFrames to help us to create
print(df)

# Rename Columns
df.rename(columns={'col1':'apples','col2':'oranges'})
print("What Happend if i change the column Names?\n",df) # You must overwrite the Dataframe variable
df = df.rename(columns={'col1':'apples','col2':'oranges'})
print("Now its better:\n",df)

#Here we do a Inverse of matrix
df['Bananas'] = [6,7,15] # Add a new column
df_inv = pd.DataFrame(np.linalg.inv(df.values),df.columns,df.index) #Create a new DF wit the inverse matrix
print(df_inv)
