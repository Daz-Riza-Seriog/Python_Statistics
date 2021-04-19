# Code made for : Sergio Andrés Díaz Ariza
# Specialization--> Statistics in Python Coursera
# 19 Abril, 2021
# License MIT

# Replicate Cartwheel example

import numpy as np
import statsmodels.api as sm
import pandas as pd

t_star = 1.96  # Number of t from tabbles
p = .85  # Proportion of population
n = 659  # Number of observations

se = np.sqrt((p * (1 - p)) / n)  # Standard Error
print("\nStandard Error:\t{}".format(se))

# Confidence Interval
lcb = p - t_star * se
ucb = p + t_star * se
print("\nConfidence Interval:\t({}, {})".format(lcb, ucb))

# Library that calculate the intervals

ci = sm.stats.proportion_confint(n * p,
                                 n)  # Here we calculate the confidence interval, with the proportion and population
print("\nConfidence interval with stats library: {}\n".format(ci))

# With pandas and data basis
df = pd.read_csv(r"C:\Users\HP\PycharmProjects\Python_Statistics\Understanding_and_Visualizing_Data_With_Python"
                 r"\Univariate Data\Python for Analysis of Univariate Data\Cartwheeldata.csv")

print(df.head())

mean = df["CWDistance"].mean()
sd = df["CWDistance"].std()
n = len(df)

tstar = 2.064
se = sd / np.sqrt(n)

print("\nStandard Error of population:\t {}".format(se))

lcb2 = mean - tstar * se
ucb2 = mean + tstar * se
print("\nConfidence Interval Cartwheel:\t({}, {})".format(lcb2, ucb2))

# Using the library stats

ci2 = sm.stats.DescrStatsW(df["CWDistance"]).zconfint_mean()
print("\nConfidence interval with stats library: {}\n".format(ci2))
