# We first need to import the packages that we will be using

import seaborn as sns # For plotting
import matplotlib.pyplot as plt # For showing plots

# Load in the data set
tips_data = sns.load_dataset("tips")

#########################################################################################
#               Visualizing the Data - Tables                                           #
#  When you begin working with a new data set, it is often best to print                #
#  out the first few rows before you begin other analysis. This will show               #
#  you what kind of data is in the dataset, what data types you are working             #
#  with, and will serve as a reference for the other plots that we are about to make.   #
#########################################################################################

# Print out the first few rows of the data
print("\nPrint the first few rows:\n",tips_data.head())

#########################################################################################
#                           Describing Data                                             #
#  Summary statistics, which include things like the mean, min, and max of the data,    #
#  can be useful to get a feel for how large some of the variables are and what         #
#  variables may be the most important.                                                 #
#########################################################################################

# Print out the summary statistics for the quantitative variables
print("\n Print the summary statistics for quantitative variables:\n",tips_data.describe())

#########################################################################################
#                           Creating a Histogram                                        #
#  After we have a general 'feel' for the data, it is often good to get a feel for      #
#  the shape of the distribution of the data.                                           #
#########################################################################################

# Plot a histogram of the total bill
sns.distplot(tips_data["total_bill"], kde = False).set_title("Histogram of Total Bill")
plt.show()

# Plot a histogram of the Tips only
sns.distplot(tips_data["tip"], kde = False).set_title("Histogram of Total Tip")
plt.show()

# Plot a histogram of both the total bill and the tips'
sns.distplot(tips_data["total_bill"], kde = False)
sns.distplot(tips_data["tip"], kde = False).set_title("Histogram of Both Tip Size and Total Bill")
plt.show()

#########################################################################################
#                           Creating a Boxplot                                          #
#  Boxplots do not show the shape of the distribution, but they can give us a better    #
#  idea about the center and spread of the distribution as well as any potential        #
#  outliers that may exist. Boxplots and Histograms often complement each other and     #
#  help an analyst get more information about the data                                  #
#########################################################################################

# Create a boxplot of the total bill amounts
sns.boxplot(data=tips_data["total_bill"]).set_title("Box plot of the Total Bill")
plt.show()

# Create a boxplot of the tips amounts
sns.boxplot(data=tips_data["tip"]).set_title("Box plot of the Tip")
plt.show()

# Create a boxplot of the tips and total bill amounts - do not do it like this
sns.boxplot(data=tips_data["total_bill"])
sns.boxplot(data=tips_data["tip"]).set_title("Box plot of the Total Bill and Tips")
plt.show()

##########################################################################################
#           Creating Histograms and Boxplots Plotted by Groups                           #
#  While looking at a single variable is interesting, it is often useful to see how a    #
#  variable changes in response to another. Using graphs, we can see if there is a       #
#  difference between the tipping amounts of smokers vs. non-smokers, if tipping varies  #
#  according to the time of the day, or we can explore other trends in the data as well. #
##########################################################################################

# Create a boxplot and histogram of the tips grouped by smoking status
sns.boxplot(x = tips_data["tip"], y = tips_data["smoker"])
plt.show()

# Create a boxplot and histogram of the tips grouped by time of day
sns.boxplot(x = tips_data["tip"], y = tips_data["time"])

g = sns.FacetGrid(tips_data, row = "time")
g = g.map(plt.hist, "tip")
plt.show()

# Create a boxplot and histogram of the tips grouped by the day
sns.boxplot(x = tips_data["tip"], y = tips_data["day"])

g = sns.FacetGrid(tips_data, row = "day")
g = g.map(plt.hist, "tip")
plt.show()