# Code made for : Sergio Andrés Díaz Ariza
# Specialization--> Statistics in Python Coursera
# 19 Abril, 2021
# License MIT

# Manipulate a DataSet between differences in pupulations

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

sns.set()

# Read data NHANES
da = pd.read_csv(r"C:\Users\HP\PycharmProjects\Python_Statistics\Understanding_and_Visualizing_Data_With_Python"
                 r"\Univariate Data\Python Assigment\nhanes_2015_2016.csv")
print(da.head())  # Look the DataFrame in Python console is better

da["SMQ020x"] = da.SMQ020.replace({1: "Yes", 2: "No", 7: np.nan, 9: np.nan})
print(da["SMQ020x"])  # Look the Column in Python console is better

da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
print(da["RIAGENDRx"])  # Look the Column in Python console is better

# New DataFrame with data that i Want

dx = da[["SMQ020x", "RIAGENDRx"]].dropna()
print("\nCross Tab from Female and Male that are Smokers:\n", pd.crosstab(dx.SMQ020x, dx.RIAGENDRx))

dx["SMQ020x"] = dx.SMQ020x.replace({"Yes": 1, "No": 0})  # Put again the values 0 1 to calculate the means
print(dx)

# Group by the Data

dz = dx.groupby("RIAGENDRx").agg({"SMQ020x": [np.mean, np.size]})  # Here we obtain the mean of each group
print(dz)

### Construct the Confidence Intervals ####

# Stanadard Error for each Population
p_fem = dz.iloc[0, 0]
n_fem = dz.iloc[0, 1]
se_fem = np.sqrt(p_fem * (1 - p_fem) / n_fem)
print("\nEstandard Error of the Female Group:\t{}".format(se_fem))

p_mal = dz.iloc[1, 0]
n_mal = dz.iloc[1, 1]
se_mal = np.sqrt(p_mal * (1 - p_mal) / n_mal)
print("\nEstandard Error of the Male Group:\t{}".format(se_mal))

# Differences Between Standard Error-square of the sum
se_diff = np.sqrt(se_fem ** 2 + se_mal ** 2)
print("\nEstandard Error of the both Group:\t{}".format(se_diff))

# Differences between proportion of population
d = p_fem - p_mal

# Confidence Bounds
lcb_df = d - 1.96 * se_diff
ucb_df = d + 1.96 * se_diff
print("\nConfidence Interval:\t({}, {})".format(lcb_df, ucb_df))
