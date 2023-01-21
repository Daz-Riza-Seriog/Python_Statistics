# import numpy as np
# import statsmodels.api as sm
# import pandas as pd
#
# from sklearn.datasets import load_boston
# boston_dataset = load_boston()
#
# boston = pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
# boston["MEDV"] = boston_dataset.target
#
# url = "nhanes_2015_2016.csv"
# NHANES = pd.read_csv(url)
# vars = ["BPXSY1", "RIDAGEYR", "RIAGENDR", "RIDRETH1", "DMDEDUC2", "BMXBMI", "SMQ020"]
# NHANES = NHANES[vars].dropna()
# NHANES["smq"] = NHANES.SMQ020.replace({2: 0, 7: np.nan, 9: np.nan})
# NHANES["RIAGENDRx"] = NHANES.RIAGENDR.replace({1: "Male", 2: "Female"})
# NHANES["DMDEDUC2x"] = NHANES.DMDEDUC2.replace({1: "lt9", 2: "x9_11", 3: "HS", 4: "SomeCollege",5: "College", 7: np.nan, 9: np.nan})
#
# np.random.seed(123)
#
# # QUESTION 1-3 Boston Data-Set
# #
# # Here is the description for each column:
# #
# # CRIM: Per capita crime rate by town
# # ZN: Proportion of residential land zoned for lots over 25,000 sq. ft
# # INDUS: Proportion of non-retail business acres per town
# # CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
# # NOX: Nitric oxide concentration (parts per 10 million)
# # RM: Average number of rooms per dwelling
# # AGE: Proportion of owner-occupied units built prior to 1940
# # DIS: Weighted distances to five Boston employment centers
# # RAD: Index of accessibility to radial highways
# # TAX: Full-value property tax rate per  $10,000
# # PTRATIO: Pupil-teacher ratio by town
# # B:  1000(Bk—0.63)2 , where Bk is the proportion of [people of African American descent] by town
# # LSTAT: Percentage of lower status of the population
# # MEDV: Median value of owner-occupied homes in  $1000 s
#
# model = sm.OLS.from_formula("MEDV ~ RM + CRIM", data=boston)
# result = model.fit()
# print(result.summary(),"\n")
#
# # Question 3
# model2 = sm.OLS.from_formula("MEDV ~ RM + CRIM + LSTAT", data=boston)
# result2 = model2.fit()
# print('\n',result2.summary(),"\n")
#
# # Question 5-6
# # NHANES data-set
#
# model3 = sm.GLM.from_formula("smq ~ RIAGENDRx + RIDAGEYR + DMDEDUC2x", family=sm.families.Binomial(), data=NHANES)
# result3 = model3.fit()
# print('\n',result3.summary(),"\n")

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
return max_of_2(a, max_of_2(b, c))