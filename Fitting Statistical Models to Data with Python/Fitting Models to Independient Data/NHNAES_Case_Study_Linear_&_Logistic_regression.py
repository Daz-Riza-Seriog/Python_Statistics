import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np
from statsmodels.sandbox.predict_functional import predict_functional

sns.set()

# Read the 2015-2016 wave of NHANES data
da = pd.read_csv("nhanes_2015_2016.csv")

# Drop unused columns, and drop rows with any missing values.
vars = ["BPXSY1", "RIDAGEYR", "RIAGENDR", "RIDRETH1", "DMDEDUC2", "BMXBMI", "SMQ020"]
da = da[vars].dropna()

# Linear Regression - Basic Model Ordinary least Squares
# Create a Model blood Pressure-Age/Gender , fit them and look up the summary
model = sm.OLS.from_formula("BPXSY1 ~ RIDAGEYR", data=da)
result = model.fit()
print(result.summary())

# find the Standard Deviation of our variables
std_BP = da.BPXSY1.std()
print("\nStandard Deviation of Our Variables {:}".format(std_BP))

# R-squared and correlation
cc = da[["BPXSY1", "RIDAGEYR"]].corr()
print('\nCorrelation Between Blood Pressure & Age {}\n'.format(cc.BPXSY1.RIDAGEYR ** 2))

# ADDING A SECOND VARIABLE
# Create a labeled version of the gender variable
da['RIAGENDRx'] = da.RIAGENDR.replace({1: "Male", 2: "Female"})

# Now we fit the model
model_2 = sm.OLS.from_formula("BPXSY1 ~ RIDAGEYR + RIAGENDRx", data=da)
result_2 = model_2.fit()
print(result_2.summary(), "\n")

# A MODEL WITH THREE VARIABLES
model_3 = sm.OLS.from_formula("BPXSY1 ~ RIDAGEYR + BMXBMI + RIAGENDRx", data=da)
result_3 = model_3.fit()
print("\n", result_3.summary())

# Visualization of the fitted model
# We are look for age and body mass index and see what is a better indication of blood pressure

values = {"RIAGENDRx": "Female", "RIAGENDR": 1, "BMXBMI": 25, "DMDEDUC2": 1, "RIDRETH1": 1, "SMQ020": 1}
pr, cb, fv = predict_functional(result_3, "RIDAGEYR", values=values, ci_method="simultaneous")

plt.figure()
ax = sns.lineplot(fv, pr, lw=4)
ax.fill_between(fv, cb[:, 0], cb[:, 1], color='grey', alpha=0.4)
ax.set_xlabel("Age")
_ = ax.set_ylabel("SBP")

plt.show()

########################
# LOGISTIC REGRESSION  #
########################
# In this case for Smoker & No-Smokers

da["smq"] = da.SMQ020.replace({2: 0, 7: np.nan, 9: np.nan})

# Look the odds of alcohol use for women an men separately
c = pd.crosstab(da.RIAGENDRx, da.smq).apply(lambda x: x/x.sum(), axis=1)
c["odds"] = c.loc[:,1]/c.loc[:,0]
print("\n",c,"\n")

# A Basic Logistic regression Model
model_4 = sm.GLM.from_formula("smq ~ RIAGENDRx",family=sm.families.Binomial(), data=da)
result_4 = model_4.fit()
print("\n", result_4.summary())

# Adding Additional Covariates
model_5 = sm.GLM.from_formula("smq ~ RIDAGEYR + RIAGENDRx",family=sm.families.Binomial(), data=da)
result_5 = model_5.fit()
print("\n", result_5.summary())