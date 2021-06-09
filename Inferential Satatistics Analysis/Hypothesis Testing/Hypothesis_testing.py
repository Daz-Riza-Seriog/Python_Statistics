# Code made for : Sergio Andrés Díaz Ariza
# Specialization--> Statistics in Python Coursera
# 28 May, 2021
# License MIT

import numpy as np
import pandas as pd
from scipy.stats import t
import scipy as sp

pd.set_option('display.max_columns', 30)  # set so can see all columns of the DataFrame

# Import the data
df = pd.read_csv(r"C:\Users\HP\PycharmProjects\Python_Statistics\Inferential Satatistics Analysis"
                 r"\Introduction Confidence Intervals\Assesment\nap_no_nap.csv")

# First, look at the DataFrame to get a sense of the data
print(df.head())

######################################################################
#   Question                                                         #
#   What is the Overall sample size n?                               #
#   What  a are the sample sizes of napping and non-napping toddlers #
######################################################################

size_napping_toddlers = df["napping"].where(df["napping"] == 1).count()
size_non_napping_toddlers = df["napping"].where(df["napping"] == 0).count()
size = df["napping"].count()

######################################################################
#   Hypothesis Test                                                  #
######################################################################

df["nap_bedtime"] = df["night bedtime"].where(df["napping"] == 1)
df["no_nap_bedtime"] = df["night bedtime"].where(df["napping"] == 0)
dx = df[["nap_bedtime", "no_nap_bedtime"]]  # replace(np.nan, 0)  # fillna(0)

# Now find the sample mean bedtime for nap and no_nap.

# Group by the Data
nap_bedtime_des = dx.nap_bedtime.describe()
no_nap_bedtime_des = dx.no_nap_bedtime.describe()
nap_mean_bedtime = dx.nap_bedtime.mean()
no_nap_mean_bedtime = dx.no_nap_bedtime.mean()
print("Describe of the toddlers nap:\t{}".format(nap_bedtime_des))
print("Descriobe of the toddlers no_nap:\t{}".format(no_nap_bedtime_des))
print("Mean of the toddlers nap:\t{}".format(nap_mean_bedtime))
print("Mean of the toddlers no_nap:\t{}".format(no_nap_mean_bedtime))

# Sample difference of the mean bedtime
mean_bedtime_diff = nap_mean_bedtime - no_nap_mean_bedtime
print("Sample Mean Difference of the toddlers :\t{}".format(mean_bedtime_diff))

# Find the Standar Deviation for both groups
nap_sd_bedtime = dx["nap_bedtime"].std()
no_nap_sd_bedtime = dx["no_nap_bedtime"].std()
print("SD of the toddlers nap:\t{}".format(nap_sd_bedtime))
print("SD of the toddlers no_nap:\t{}".format(no_nap_sd_bedtime))

# What is the Standar Error for the difference. We use a pooled Standard Error.
pooled_se = np.sqrt(
    (((size_napping_toddlers - 1) * nap_sd_bedtime ** 2) + ((size_non_napping_toddlers - 1) * no_nap_sd_bedtime ** 2))
    * ((1 / size_napping_toddlers) + (1 / size_non_napping_toddlers)) / (
            size_napping_toddlers + size_non_napping_toddlers - 2))

print("SE pooled for the difference:\t{}".format(pooled_se))

# Calculate t-test statistic for our hypothesis

tstat = mean_bedtime_diff / pooled_se
print("t-stat for the difference:\t{}".format(tstat))

# Find the p-value, we can use the CFD for the t-distribution for the first hypothesis
degree_freedom = size_napping_toddlers + size_non_napping_toddlers - 2
pvalue = 1 - t.cdf(tstat, degree_freedom)
print("Degrees of freedom:\t{}".format(degree_freedom))
print("p-value for the difference, is one-side:\t{}".format(pvalue))

# Using the scipy library to do all the same
nap_bed = dx["nap_bedtime"].dropna()
no_nap_bed = dx["no_nap_bedtime"].dropna()
pvalue1 = sp.stats.ttest_ind(nap_bed, no_nap_bed)
print("T_test Results using scipy, careful with that is for two side:\n{}".format(pvalue1))

#####################################################
#   Resolve the second hypothesis                   #
#####################################################

df["nap_24_sleep"] = df["24 h sleep duration"].where(df["napping"] == 1)
df["no_nap_24_sleep"] = df["24 h sleep duration"].where(df["napping"] == 0)
dx = df[["nap_24_sleep", "no_nap_24_sleep"]]  # replace(np.nan, 0)  # fillna(0)
nap_sleep = dx["nap_24_sleep"].dropna()
no_nap_sleep = dx["no_nap_24_sleep"].dropna()
pvalue2 = sp.stats.ttest_ind(nap_sleep, no_nap_sleep)
print("T_test Results using scipy for the second hypothesis, careful with that is for two side:\n{}".format(pvalue2))
