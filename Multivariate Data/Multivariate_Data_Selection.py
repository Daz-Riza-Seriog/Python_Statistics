###########################################################
# How to select dataframe subsets from multivariate data  #
###########################################################

import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe

# Download NHANES 2015-2016 data
df = pd.read_csv("nhanes_2015_2016.csv")

print(df.head())

############################################################################
# Keep only body measures columns, so only columns with "BMX" in the name  #
############################################################################

# get columns names
col_names = df.columns
print("\nPrint Column Names of the Data:\n",col_names)

# One way to get the column names we want to keep is simply by copying from the above output and storing in a list
keep1 = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC',
       'BMXWAIST']

# Another way to get only column names that include 'BMX' is with list comprehension
# [keep x for x in list if condition met]
keep2 = [column for column in col_names if 'BMX' in column]

# use [] notation to keep columns
df_BMX = df[keep2]

print("\nPrint a Data Columns with only BMX\n",df_BMX.head())

#############################################################################
#           There are two methods for selecting by row and column.          #
#     # link for pandas cheat sheets                                        #
#           df.loc[row labels or bool, col labels or bool]                  #
#           df.iloc[row int or bool, col int or bool]                       #
#     #From pandas docs:                                                    #
#           column indexing                                                 #
#           .loc is primarily label based, but may also                     #
#           be used with a boolean array.                                   #
#           .iloc is primarily integer position based                       #
#           (from 0 to length-1 of the axis), but may also be               #
#           used with a boolean array.                                      #
#############################################################################

print("\nData Frame Indexing BMX\n",df.loc[:, keep2].head())

index_bool = np.isin(df.columns, keep2)

print("\nWe look where the Columns are\n",index_bool)

print("\nAnother way to Indexing BMX to DataFrame\n ",df.iloc[:,index_bool].head()) # Indexing with boolean list

############################################################################
#                   Selection by conditions                                #
############################################################################

# Lets only look at rows who 'BMXWAIST' is larger than the median
waist_median = pd.Series.median(df_BMX['BMXWAIST']) # get the median of 'BMXWAIST'
#  waist_median2 = np.median(df_BMX["BMXWIST"])  Produce a Error

print("\nMedian of BMXWIST:\n",waist_median)

print("\nRows in BMXWAIST larger thn Mediam\n",df_BMX[df_BMX['BMXWAIST'] > waist_median].head())

# Lets add another condition, that 'BMXLEG' must be less than 32
condition1 = df_BMX['BMXWAIST'] > waist_median
condition2 = df_BMX['BMXLEG'] < 32
print("\nUsing Two Conditions with &:\n",df_BMX[condition1 & condition2].head()) # Using [] method
# Note: can't use 'and' instead of '&'

print("\nUsing Two Conditions with & and .loc[]:\n",df_BMX.loc[condition1 & condition2, :].head()) # Using df.loc[] method
# note that the conditiona are describing the rows to keep

# Lets make a small dataframe and give it a new index so can more clearly see the differences between .loc and .iloc
tmp = df_BMX.loc[condition1 & condition2, :].head()
tmp.index = ['a', 'b', 'c', 'd', 'e'] # If you use different years than 2015-2016, this my give an error. Why?
print("\nWe indexing and look the difference beteen .iloc nd .loc:\n",tmp)

print(tmp.loc[['a', 'b'],'BMXLEG'])
print(tmp.iloc[[0, 1],3])

############################################################################
#                   Common errors and how to read them                     #
############################################################################

# print(tmp[:, 'BMXBMI'])

############################################################################
#                   Problem                                                #
# The above gives: TypeError: unhashable type: 'slice'                     #
#                                                                          #
# The [ ] method uses hashes to identify the columns to keep, and each     #
# column has an associated hash. A 'slice' (a subset of rows and columns)  #
# does not have an associated hash, thus causing this TypeError.           #
############################################################################

# print(tmp.loc[:, 'BMXBMI'])
# print(tmp.loc[:, 'BMXBMI'].values)
# print(tmp.iloc[:, 'BMXBMI'])

##############################################################################
#                   Problem                                                  #
# The above gives: ValueError: Location based indexing can only have         #
# [integer, integer slice (START point is INCLUDED, END point is EXCLUDED)   #
# , listlike of integers, boolean array] types                               #
#                                                                            #
# 'BMXBMI' is not an integer that is less than or equal number               #
# of columns -1, or a list of boolean values, so it is the wrong value type. #
##############################################################################

# print(tmp.iloc[:, 2])
# print(tmp.loc[:, 2])

######################################################################################
#                   Problem                                                          #
# The above code gives: TypeError: cannot do label indexing on                       #
# <class 'pandas.core.indexes.base.Index'> with these indexers [2] of <class 'int'>  #
#                                                                                    #
# 2 is not one of the labels (i.e. column names) in the dataframe                    #
######################################################################################

# Here is another example of using a boolean list for indexing columns
print(tmp.loc[:, [False, False, True] +[False]*4])
print(tmp.iloc[:, 2])

# We can use the .loc and .iloc methods to change values within the dataframe
tmp.iloc[0:3,2] = [0]*3
print(tmp.iloc[:,2])

tmp.loc['a':'c','BMXBMI'] = [1]*3
print(tmp.loc[:,'BMXBMI'])

# We can use the [] method when changing all the values of a column
tmp['BMXBMI'] = range(0, 5)
print(tmp)

# We will get a warning when using the [] method with conditions to set new values in our dataframe
tmp[tmp.BMXBMI > 2]['BMXBMI'] = [10]*2 # Setting new values to a copy of tmp, but not tmp itself
print(tmp)
# You can see that the above code did not change our dataframe 'tmp'. This

# The correct way to do the above is with .loc or .iloc
tmp.loc[tmp.BMXBMI > 2, 'BMXBMI']  = [10]*2
print(tmp) # Now contains the chances