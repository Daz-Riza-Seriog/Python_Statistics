#############################################################################################
#                                           Seaborn                                         #
# Seaborn is complimentary to Matplotlib and it specifically targets statistical data       #
# visualization. But it goes even further than that: Seaborn extends Matplotlib and makes   #
# generating visualizations convenient.                                                     #
#                                                                                           #
# While Matplotlib is a robust solution for various problems, Seaborn utilizes more         #
# concise paramesters for ease-of-use.                                                      #
#############################################################################################
# #######################################################
#                   Scatterplots                        #
#########################################################

# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Store the url string that hosts our .csv file
url = "Cartwheeldata.csv"

# Read the .csv file and store it as a pandas Data Frame
df = pd.read_csv(url)

# Create Scatterplot
sns.lmplot(x='Wingspan', y='CWDistance', data=df)
plt.show()

# Scatterplot arguments
sns.lmplot(x='Wingspan', y='CWDistance', data=df,
           fit_reg=False, # No regression line
           hue='Gender')   # Color by evolution stage
plt.show()

# Construct Cartwheel distance plot
sns.swarmplot(x="Gender", y="CWDistance", data=df)
plt.show()

sns.boxplot(data=df.loc[:, ["Age", "Height", "Wingspan", "CWDistance", "Score"]])
plt.show()

# Male Boxplot
sns.boxplot(data=df.loc[df['Gender'] == 'M', ["Age", "Height", "Wingspan", "CWDistance", "Score"]])
plt.show()

# Female Boxplot
sns.boxplot(data=df.loc[df['Gender'] == 'F', ["Age", "Height", "Wingspan", "CWDistance", "Score"]])
plt.show()

# Male Boxplot
sns.boxplot(data=df.loc[df['Gender'] == 'M', ["Score"]])
plt.show()

# Female Boxplot
sns.boxplot(data=df.loc[df['Gender'] == 'F', ["Score"]])
plt.show()

########################################################################
#                     Histogram                                        #
########################################################################

# Distribution Plot (a.k.a. Histogram)
sns.distplot(df.CWDistance)
#sns.histplot(df.CWDistance)  is different but in the next versions it will be removed
plt.show()

########################################################################
#                     Count Plot                                       #
########################################################################

# Count Plot (a.k.a. Bar Plot)
sns.countplot(x='Gender', data=df)

plt.xticks(rotation=-45)

plt.show()