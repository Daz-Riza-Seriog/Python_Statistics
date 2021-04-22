# Code made for : Sergio Andrés Díaz Ariza
# Specialization--> Statistics in Python Coursera
# 23 April, 2021
# License MIT

import numpy as np
import pandas as pd
from scipy.stats import t

pd.set_option('display.max_columns', 30)  # set so can see all columns of the DataFrame

# Import the data
df = pd.read_csv("nap_no_nap.csv")

# First, look at the DataFrame to get a sense of the data
print(df.head())

############################################################################
# Average bedtime confidence interval for napping and non napping toddlers #
# Create two 95% confidence intervals for the average bedtime, one for     #
# toddler who nap and one for toddlers who don't.                          #
# ##########################################################################

# First, isolate the column 'night bedtime' for those who nap into a new variable, and those who didn't nap
# into another new variable.

df["bedtime_nap"] = df["night bedtime"].where(df["napping"] == 1)
df["bedtime_no_nap"] = df["night bedtime"].where(df["napping"] == 0)
dx = df[["bedtime_nap", "bedtime_no_nap"]]  # replace(np.nan, 0)  # fillna(0)

# Now find the sample mean bedtime for nap and no_nap.

# Group by the Data
nap_mean_bedtime = dx.bedtime_nap.mean()
no_nap_mean_bedtime = dx.bedtime_no_nap.mean()
print("Mean of the toddlers nap:\t{}".format(nap_mean_bedtime))
print("Mean of the toddlers no_nap:\t{}".format(no_nap_mean_bedtime))

# Find the t_stars for the 95% confidence intervals

# Careful the t-distribution has two tails, then you dont do (1 - 0.05)= 0.95 instead (1 - 0.05 / 2)
nap_t_star = t.ppf(1 - 0.05 / 2, dx.bedtime_nap.count()-1)
no_nap_t_star = t.ppf(1 - 0.05 / 2, dx.bedtime_no_nap.count()-1)

print("t* of the interval toddlers nap:\t{}".format(nap_t_star))
print("t* of the interval toddlers no_nap:\t{}".format(no_nap_t_star))

# Now to create our confidence intervals. For the average bedtime for nap and no nap,
# find the upper and lower bounds for the respective 95% confidence intervals.

# Standard Error for each Population of the mean
sd_nap = dx["bedtime_nap"].std()  # standard Deviation
sd_no_nap = dx["bedtime_no_nap"].std()
se_nap = sd_nap / np.sqrt(dx.bedtime_nap.count())    # Is of the sample not of the populaton
se_no_nap = sd_no_nap / np.sqrt(dx.bedtime_no_nap.count())

print("Standard Error of the Napping Group:\t{}".format(se_nap))
print("Standard Error of the No-Napping Group:\t{}".format(se_no_nap))

# Confidence Intervals
lcb_nap = nap_mean_bedtime - nap_t_star * se_nap
ucb_nap = nap_mean_bedtime + nap_t_star * se_nap
lcb_no_nap = no_nap_mean_bedtime - no_nap_t_star * se_no_nap
ucb_no_nap = no_nap_mean_bedtime + no_nap_t_star * se_no_nap
print("\nConfidence Interval Napping:\t({}, {})".format(lcb_nap, ucb_nap))
print("\nConfidence Interval No-Napping:\t({}, {})".format(lcb_no_nap, ucb_no_nap))
