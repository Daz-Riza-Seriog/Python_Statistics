import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt

sns.set()

# This set option allow show more columns when you print the data
pd.set_option('display.max_columns', 100)

path = "nhanes_2015_2016.csv"

# First, you must import the data from the path given above
# using pandas, read in the csv data found at the url defined by 'path'
df = pd.read_csv(path)

# Next, look at the 'head' of our DataFrame 'df'.

# If you can't remember a function, open a previous notebook or video as a reference
# or use your favorite search engine to look for a solution

print("\nDataSet NHANES first 5 rows;\n",df.head(2))

# How many rows can you see when you don't put an argument into the previous method?
# How many rows can you see if you use an int as an argument?
# Can you use a float as an argument?

# Lets only consider the feature (or variable) 'BPXSY2'
bp = df['BPXSY2']

print("\nFeature BPXSY2:\n",bp)

# Numerical Summaries
# Find the mean (note this for the quiz that follows)

# What is the mean of 'BPXSY2'?
bp_mean = np.mean(bp)
print("\nMean of the feature BPXSY2:\n",bp_mean)
bp_mean2 = np.nanmean(bp)
print("\nMean2 of the feature BPXSY2:\n",bp_mean)
# In the method you used above, how are the rows of missing data treated?
# Are the excluded entirely? Are they counted as zeros? Something else?
# If you used a library function, try looking up the documentation using the code:
#
# help(function_you_used)
# For example:
# # help(np.sum)

##help(np.mean)

# .dropna()
# To make sure we know that we aren't treating missing data in ways we don't want,
# lets go ahead and drop all the nans from our Series 'bp'

bp = bp.dropna()
print("\nPrint BPXYS2 without NaN values:\n",bp)

# Find the:
# Median
# Max
# Min
# Standard deviation
# Variance
# You can implement any of these from base python (that is, without any of the imported packages),
# but there are simple and intuitively named functions in the numpy library for all of these.
# You could also use the fact that 'bp' is not just a list, but is a pandas.Series. You can find pandas.
# Series attributes and methods here

# A large part of programming is being able to find the functions you need and to understand
# the documentation formatting so that you can implement the code yourself, so we highly encourage
# you to search the internet whenever you are unsure!

# Example:
# Find the difference of an element in 'bp' compared with the previous element in 'bp'.

# Using the fact that 'bp' is a pd.Series object, can use the pd.Series method diff()
# call this method by: pd.Series.diff()
diff_by_series_method = bp.diff()
# note that this returns a pd.Series object, that is, it had an index associated with it
print("\npd.Series.diff() of bp data:\n",diff_by_series_method.values) # only want to see the values, not the index and values

# Now use the numpy library instead to find the same values
# np.diff(array)
diff_by_np_method = np.diff(bp)
print("\nnp.diff() of bp data:\n",diff_by_np_method)
# note that this returns an 'numpy.ndarray', which has no index associated with it, and therefore ignores
# the nan we get by the Series method

# We could also implement this ourselves with some looping
diff_by_me = [] # create an empty list
for i in range(len(bp.values)-1): # iterate through the index values of bp
    diff = bp.values[i+1] - bp.values[i] # find the difference between an element and the previous element
    diff_by_me.append(diff) # append to out list
print("\nDifference of bp data using looping:\n",np.array(diff_by_me)) # format as an np.array

# Your turn (note these values for the quiz that follows)

bp_median = np.median(bp)
print("\nMedian of bp data:\n",bp_median)

bp_max = np.max(bp)
print("\nMax of bp data:\n",bp_max)

bp_min = np.min(bp)
print("\nMin of bp data:\n",bp_min)

bp_std = np.std(bp)
print("\nStd of bp data:\n",bp_std)

bp_var = np.var(bp)
print("\nVar of bp data:\n",bp_var)

# How to find the interquartile range (note this value for the quiz that follows)
# This time we need to use the scipy.stats library that we imported above under the name 'stats'

bp_iqr = stats.iqr(bp)
print("\nInterquartil Range using Stats Library:\n",bp_iqr)

# Visualizing the data
# Next we'll use what you have learned from the Tables, Histograms, Boxplots in Python video

# use the Series.describe() method to see some descriptive statistics of our Series 'bp'
bp_descriptive_stats = bp.describe()
print("\nDescribe of bp data:\n",bp_descriptive_stats)

# Make a histogram of our 'bp' data using the seaborn library we imported as 'sns'
sns.displot(bp, kde = False)
plt.title("Histogram of BP Data")
plt.show()
# Is your histogram labeled and does it have a title? If not, try appending
# # .set(title='your_title', xlabel='your_x_label', ylabel='your_y_label')
# or just
# .set(title='your_title')
# to your graphing function

# Make a boxplot of our 'bp' data using the seaborn library. Make sure it has a title and labels!
sns.boxplot(data=bp).set_title("Box plot of the BP Data")
plt.show()

