###################################################################
# In this assignment we'll ask you to plot multiple variables.    #
#                                                                 #
# You will use what you find in this assignment to answer the     #
# questions in the quiz that follows. It may be useful to keep    #
# this notebook side-by-side with this week's quiz on your screen.#
###################################################################

import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
sns.set()
pd.set_option('display.max_columns', 100)

path = "Cartwheeldata.csv"

# First, you must import the cartwheel data from the path given above
df = pd.read_csv(path)  # using pandas, read in the csv data found at the url defined by 'path'

# Next, look at the 'head' of our DataFrame 'df'.
print(df.head())

###################################################################
#                               Scatter plots                     #
# First, let's looks at two variables that we expect to have a    #
# strong relationship, 'Height' and 'Wingspan'.                   #
###################################################################

# Make a Seaborn scatter plot with x = height and y = wingspan using sns.scatterplot(x, y)
plt.figure(1) ## Using scatterplot that only makes a scatter plot
sns.scatterplot(x=df["Height"],y=df["Wingspan"],)
plt.title("Height vs Wingspan")
plt.xlabel("Height")
plt.ylabel("Wingspan")

plt.figure(2) ##Using lmplot that make a sctter and linear regression
sns.lmplot(x='Height', y='Wingspan', data=df,
           fit_reg=True)# Regression line
plt.title("Height vs Wingspan")

plt.show()

# With a Gender Hue

plt.figure(3) ## Using scatterplot that only makes a scatter plot
sns.scatterplot(x=df["Height"],y=df["Wingspan"],hue=df["Gender"])
plt.title("Height vs Wingspan")
plt.xlabel("Height")
plt.ylabel("Wingspan")

plt.figure(4) ##Using lmplot that make a sctter and linear regression
sns.lmplot(x='Height', y='Wingspan', data=df,
           fit_reg=True,# Regression line
           hue='Gender')
plt.title("Height vs Wingspan")
plt.show()
############################################################################################
#             How would you describe the relationship between 'Height' and 'Wingspan'?     #
#   Questions you can ask:                                                                 #
#                                                                                          #
#   Is it linear?                                                                          #
#   Are there outliers?                                                                    #
#   Are their ranges similar or different?                                                 #
#   How else could you describe the relationship?                                          #
#                                                                                          #
#   Now let's look at two variables that we don't yet assume have a strong relationship,   #
#   'Wingspan' and 'CWDistance'                                                            #
############################################################################################

# Make a Seaborn scatter plot with x = wingspan and y = cartwheel distance

plt.figure(5) ## Using scatterplot that only makes a scatter plot
sns.scatterplot(x=df["Wingspan"],y=df["CWDistance"])
plt.title(" Wingspan vs CWDistance")
plt.xlabel("Wingspan")
plt.ylabel("CWDistance")

plt.figure(6) ##Using lmplot that make a sctter and linear regression
sns.lmplot(x='Wingspan', y='CWDistance', data=df,
           fit_reg=True # Regression line
           )
plt.title("Wingspan vs CWDistance")

plt.show()

# 3. Question 3 # Is the interquartile range of ‘CWDistance’ similar to ‘Wingspan’?

CWD_data = df["CWDistance"].dropna()
Wing_data = df["Wingspan"].dropna()

CWD_iqr = stats.iqr(CWD_data)
Wing_iqr = stats.iqr(Wing_data)

print("\nCWDistnce Interquartile Range\t:",CWD_iqr,"\nWingspan Interquartile Range\t:",Wing_iqr)

############################################################################################
#         How would you describe the relationship between 'Wingspan' and 'CWDistance'?     #
#   Questions you can ask:                                                                 #
#                                                                                          #
#   Is it linear?                                                                          #
#   Are there outliers?                                                                    #
#   Are their ranges similar or different?                                                 #
#   How else could you describe the relationship?                                          #
#                                                                                          #
#   Let makes the same plot as above, but now include 'Gender' as the color scheme by      #
#   including the argument                                                                 #
#                                                                                          #
#   hue=df['Gender']                                                                       #
#   in the Seaborn function                                                                #
############################################################################################

#  Make a Seaborn scatter plot with x = wingspan and y = cartwheel distance, and hue = gender

plt.figure(7) ## Using scatterplot that only makes a scatter plot
sns.scatterplot(x=df["Wingspan"],y=df["CWDistance"],hue=df["Gender"])
plt.title(" Wingspan vs Distance")
plt.xlabel("Wingspan")
plt.ylabel("CWDistance")

plt.figure(8) ##Using lmplot that make a sctter and linear regression
sns.lmplot(x='Wingspan', y='CWDistance', data=df,
           fit_reg=True, # Regression line
           hue='Gender')
plt.title("Wingspan vs CWDistance")

plt.show()

# Does does this new information on the plot change your interpretation of the relationship between
# 'Wingspan' and 'CWDistance'?

############################################################################################
#                                           Barcharts                                      #
#         Now lets plot barplots of 'Glasses                                               #
############################################################################################

# Make a Seaborn barplot with x = glasses and y = cartwheel distance
plt.figure(9)
sns.barplot(x=df["Glasses"],y=df["CWDistance"])
plt.title(" Glasses vs CDistance")
plt.xlabel("Glasses")
plt.ylabel("CWDistance")

# What can you say about the relationship of 'Glasses' and 'CWDistance'?

# Make the same Seaborn boxplot as above, but include gender for the hue argument
plt.figure(10)
sns.barplot(x=df["Glasses"],y=df["CWDistance"],hue=df["Gender"])
plt.title(" Glasses vs CWDistance")
plt.xlabel("Glasses")
plt.ylabel("CWDistance")

plt.show()

#How does this new plot change your interpretation about the relationship of 'Glasses' and 'CWDistance'?