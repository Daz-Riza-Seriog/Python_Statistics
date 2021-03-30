##################################################################################
#           Practice notebook for univariate analysis using NHANES data          #
#                                                                                #
#   This notebook will give you the opportunity to perform some univariate       #
#   analyses on your own using the NHANES. These analyses are similar to what    #
#   was done in the week 2 NHANES case study notebook.                           #
#                                                                                #
#   You can enter your code into the cells that say "enter your code here",      #
#   and you can type responses to the questions into the cells that say "Type    #
#   Markdown and Latex".                                                         #
#                                                                                #
#   Note that most of the code that you will need to write below is very similar #
#   to code that appears in the case study notebook. You will need to edit code  #
#   from that notebook in small ways to adapt it to the prompts below.           #
#                                                                                #
#   To get started, we will use the same module imports and read the data in the #
#   same way as we did in the case study:                                        #
##################################################################################

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np

sns.set()

da = pd.read_csv("nhanes_2015_2016.csv")

##################################################################################
#                                   Question 1                                   #
#                                                                                #
#   Relabel the marital status variable DMDMARTL to have brief but informative   #
#   character labels. Then construct a frequency table of these values for all   #
#   people, then for women only, and for men only. Then construct these three    #
#   frequency tables using only people whose age is between 30 and 40.           #
##################################################################################
print(da.head())
#import sys
#import os
#import pandas
#import csv

# To see data in the Python console, beacuse for any reason it not allow read the CSV
# If there is a command-line argument, and the argument is a valid file, this matches
#if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
#    csv_path = sys.argv[1]
#else:
#    csv_path = r'D:\clovi\Projetos\Python\Usuarios.csv'

#csv_reader = pandas.read_csv(csv_path,encoding='utf-8')

print("\nFrequency Table for All People:\n",da['DMDMARTL'].value_counts())
print("\nFrequency Table for Only Men:\n",da['DMDMARTL'][da['RIAGENDR']==1].value_counts())
print("\nFrequency Table for Only Women:\n",da['DMDMARTL'][da['RIAGENDR']==2].value_counts())
print("\nFrequency Table for Only Men in Range 30-40 years:\n",
      da['DMDMARTL'][da['RIAGENDR']==1][da['RIDAGEYR'].between(30,40)].value_counts())
print("\nFrequency Table for Only Women in Range 30-40 years:\n",
      da['DMDMARTL'][da['RIAGENDR']==2][da['RIDAGEYR'].between(30,40)].value_counts())

##################################################################################
#                                   Question 3                                   #
#                                                                                #
#   Construct a histogram of the distribution of heights using the BMXHT         #
#   variable in the NHANES sample.                                               #
##################################################################################
sns.displot(da["BMXHT"],bins=80, kde = False)
plt.title("Histogram of Heights")
plt.show()

da["BMXHT2"] = da["BMXHT"].dropna()
sns.boxplot(data = da["BMXHT2"][da['RIAGENDR']==1]).set_title("Boxplot of the Mens")
plt.show()