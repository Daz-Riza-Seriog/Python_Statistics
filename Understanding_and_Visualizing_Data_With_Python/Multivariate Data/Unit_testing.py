#################################################################################
#                                  Unit Testing                                 #
# While we will not cover the unit testing library that python                  #
# has, we wanted to introduce you to a simple way that you can test your code.  #
#                                                                               #
# Unit testing is important because it the only way you can be sure that        #
# your code is do what you think it is doing.                                   #
#                                                                               #
# Remember, just because ther are no errors does not mean your code is correct. #
#################################################################################

import numpy as np
import pandas as pd
import matplotlib as plt
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe

# Download NHANES 2015-2016 data
df = pd.read_csv("nhanes_2015_2016.csv")
#df.index = range(1,df.shape[0]+1)

print(df.head(3))

#################################################################################
#                                  Goal                                         #
# We want to find the mean of first 100 rows of 'BPXSY1' when 'RIDAGEYR' > 60   #
#################################################################################

# One possible way of doing this is:
mean = pd.Series.mean(df[df.RIDAGEYR > 60].iloc[0:100,16])
mean2 = pd.Series.mean(df[df.RIDAGEYR > 60].loc[0:100,'BPXSY1'])
# Current version of python will include this warning, older versions will not
print("\nMean with .iloc\n",mean,"\nMean with .loc\n",mean2)

print("\n.loc df\n ",df[df.RIDAGEYR > 60].loc[0:100,'BPXSY1'])
print("\n.iloc df\n ",df[df.RIDAGEYR > 60].iloc[0:100,16])
###### NOTE : .loc fill the values that not accomplish the condition with NaN he deprecated some values
#### Look in the Python console
# csv_path = r'C:\Users\HP\PycharmProjects\Understanding_and_Visualizing_Data_With_Python\Multivariate Data\nhanes_2015_2016.csv'

# test our code on only ten rows so we can easily check
test = pd.DataFrame({'col1': np.repeat([3,1],5), 'col2': range(3,13)}, index=range(0,10))
print("\nTest for understand the Error\n",test)

# pd.Series.mean(df[df.RIDAGEYR > 60].loc[range(0,5), 'BPXSY1'])
# should return 5

mean_test = pd.Series.mean(test[test.col1 > 2].loc[0:5, 'col2'])
print("\nMean Test, 10 samples\n",mean_test)

df_test = test[test.col1 > 2].loc[0:5, 'col2']
# 0 is not in the row index labels because the second row's value is < 2. For now, pandas defaults to filling this
# with NaN

print("\nLook in the test sample\n",df_test)

