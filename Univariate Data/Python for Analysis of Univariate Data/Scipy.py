from scipy import stats
import numpy as np

### Print Normal Random Variables
print('\nNomal Random Variables:\n',stats.norm.rvs(size = 10))

import matplotlib.pyplot as plt

# Create some test data
dx = .01
X  = np.arange(-2,2,dx)
Y  = np.exp(-X**2)

# Normalize the data to a proper PDF
Y /= (dx*Y).sum()

# Compute the CDF
CY = np.cumsum(Y*dx)

# Plot both
plt.plot(X,Y)
plt.plot(X,CY,'r--')

plt.show()

### Compute the Normal CDF of certain values.
print('\nThe Normal CDF of certain Values:\n',stats.norm.cdf(np.array([1,-1., 0, 1, 3, 4, -2, 6])))

##############################################################
#                 Descriptive Statistics                     #
##############################################################

np.random.seed(282629734)

# Generate 1000 Student’s T continuous random variables.
x = stats.t.rvs(10, size=1000)

# Do some descriptive statistics
print('\nDescriptive Statistics')
print('\nx.min() equivalent `np.min(x)`\n',x.min())   # equivalent to np.min(x)

print('\nx.max() equivalent `np.max(x)`\n',x.max())   # equivalent to np.max(x)

print('\nx.mean() equivalent `np.mean(x)`\n',x.mean())  # equivalent to np.mean(x)

print('\nx.var() equivalent `np.var(x)`\n',x.var())   # equivalent to np.var(x))

print('\nOverall Statistics Parameters compare whit above dta:\n',stats.describe(x))

#########################################
# Later in the course, we will discuss  #
# distributions and statistical tests   #
# such as a T-Test. SciPy has built in  #
# functions for these operations.       #
#########################################