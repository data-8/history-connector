# Note you need to have these packages in your computer. To do this easily just download anaconda.
import pandas as pd
import numpy as np
from scipy stats
import matplotlib.pyplot as plt

# Table is generated using numpy but is essentially the same as the Table package that was designed. Note that the file was converted from xls to csv using an online converter. If you want you can write a python converter but this will be slow. Note that the path will be different for windows. Also the path depends on where your csv file is in. I chose to put it in the downloads section. Also Note that the filename has changed to 07423-0001-Data1.csv due to converting.
Table = np.read_csv('~/Downloads/07423-0001-Data1.csv')

# This line gets the Table of slave numbers and their prices.
prices = Table['V14']

# These two lines gets the Table of slave numbers and their prices, only including those that are we deem to be relevant (i.e. where the column V40 is all 1 gives us the slaves that are guaranteed and 2 gives us those that are guaranteed.)
guarantee = Table['V14'][Table.V40 == 1]
notG = Table['V14'][Table.V40 == 2]


# Assuming that the student has correctly impleneted the KS distance function in lab 8, which we simulate using the python package scipy. Let us set our significance level for the hypothesis testing to be 0.05. Meaning we reject the null hypothesis (that there is no difference between the prices)
stats.ks_2samp(guarantee, notG)

# From running the line above, we get a p-value of about 1.55*10^-17, which leads us to the conclusion to reject the null hypothesis.

# The other variables can be taken into account by creating more queries to the table, or more complex functions that iterate over loops like a for loop having a boolean statement for the different statistics (i.e. the color of the person's skin).

# The results for males and females price difference is significant. From hypothesis test using KS distance, we get a p-value of 2.9943622527702614e-19.
male = Table['V14'][Table.V15 == 1]
female = Table['V14'][Table.V15 == 2]
stats.ks_2samp(male, female)

# Further analysis can be done by looking at the histograms of the two data, using the matplotlib.pyplot
plt.figure()
male.hist()
female.hist()
