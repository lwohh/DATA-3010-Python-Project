# importing necessary libraries & packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats as sp
import statistics as stat

GSS = pd.read_csv('C:/Users/canyon.white/OneDrive - Convergint/Documents/GitHub/DATA 3010 Python Project/GSSData_PythonProject_Sp2022.csv')

# Q1
# Descriptive statistics table for the quantitative variables (tvhours, age, chldidel)
GSS.describe()

# Q2
# Histogram of tvhours
plt.hist(GSS.tvhours, edgecolor="black")
plt.xlabel('Hours Watched Per Day')
plt.ylabel('Frequency')
plt.title('Figure 1: Histogram of Hours TV Watched Per Day')
plt.show()

# Boxplot of tvhours
plt.boxplot(GSS.tvhours)
plt.ylabel('Hours Watched Per Day')
plt.title('Figure 2: Box Plot of Hours TV Watched Per Day')
plt.show()

# Histogram of age
plt.hist(GSS.age, edgecolor="black")
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Figure 3: Histogram of Age')
plt.show()

# Boxplot of age
plt.boxplot(GSS.age)
plt.ylabel('Age')
plt.title('Figure 4: Box Plot of Age')
plt.show()


# Histogram of chldidel
plt.hist(GSS.chldidel, edgecolor="black")
plt.xlabel('Ideal Number of Children')
plt.ylabel('Frequency')
plt.title('Figure 5: Histogram of Ideal Number of Children')
plt.show()

# Boxplot of chldidel
plt.boxplot(GSS.chldidel)
plt.ylabel('Ideal Number of Children')
plt.title('Figure 6: Box Plot of Ideal Number of Children')
plt.show()


# Q4
# Univariate Frequency Table for degree
deg_tab = pd.crosstab(index=GSS["degree"], columns="counts")
# Printing my Degree Frequency Table
print(deg_tab)
# Making my Degree Frequency Table into a Percentages Table
round(deg_tab/deg_tab.sum()*100, 2)

# Univariate Frequency Table for polparty
pol_table = pd.crosstab(index=GSS.polparty, columns="counts")
# Printing my PolParty Frequency Table
print(pol_table)
# Making my PolParty Frequency Table into a Percentages Table
round(pol_table/pol_table.sum()*100, 2)

# Univariate Frequency Table for cappun
cap_table = pd.crosstab(index=GSS.cappun, columns="counts")
# Printing my CapPun Frequency Table
print(cap_table)
# Making my CapPun Frequency Table into a Percentages Table
round(cap_table/cap_table.sum()*100, 2)


# Q5
# Pie Chart of degree
deg_colors = ("red", "blue", "green", "yellow", "purple")
plt.pie(GSS.degree.value_counts(), colors=deg_colors, autopct='%1.1f%%')
plt.legend(['HighSchool','NotHs','Bachelor','Graduate','JunColl'])
plt.title('Figure 7: Pie Chart of Highest Degree Achieved (n=397)', loc='center')
plt.show()

# Bar Chart of degree
deg_name = ['Bachelor','Graduate','HighSchool','JunColl','NotHs']
deg_freq = [52,30,231,28,56]
plt.bar(deg_name, deg_freq, color='green')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Figure 8: Bar Chart of Highest Degree Achieved (n=397)', loc='center')
plt.show()

# Pie Chart of polparty
pol_colors = ('blue','yellow','red','green')
plt.pie(GSS.polparty.value_counts(), colors=pol_colors, autopct='%1.1f%%')
plt.legend(['Democrat','Independent','Republican','Other'])
plt.title('Figure 9: Pie Chart of Political Party Affiliation (n=397)', loc='center')
plt.show()

# Bar Chart of polparty
pol_name = ['Democrat','Independent','Other','Republican']
pol_freq = [139,137,8,113]
plt.bar(pol_name, pol_freq, color='green')
plt.xlabel('Political Party')
plt.ylabel('Frequency')
plt.title('Figure 10: Bar Chart of Political Party Affiliation (n=397)', loc='center')
plt.show()

# Pie Chart of cappun
cap_colors = ('blue','red')
plt.pie(GSS.cappun.value_counts(), colors=cap_colors, autopct='%1.1f%%')
plt.legend(['Favor','Oppose'])
plt.title('Figure 11: Pie Chart of Opinion on Capital Punishment (n=397)', loc='center')
plt.show()

# Bar Chart of cappun
cap_name = ['Favor','Oppose']
cap_freq = [294,103]
plt.bar(cap_name, cap_freq, color='green')
plt.xlabel('Opinion')
plt.ylabel('Frequency')
plt.title('Figure 12: Bar Chart of Opinion on Capital Punishment (n=397)', loc='center')
plt.show()


# Q7
# 2-way Contingency Frequency Table for owngun and gunlaw
own_law_table = pd.crosstab(GSS.owngun, GSS.gunlaw, margins=False)
print(own_law_table)
# 2-way Contingency Percentage Table for owngun and gunlaw
round(own_law_table/own_law_table.sum()*100, 1)


# Q9
# Grouped Bar Chart for owngun and gunlaw
bars1 = [230,97]
bars2 = [27,43]
ind = np.arange(2)
width = 0.35
plt.bar(ind, bars1, width, label='No')
plt.bar(ind + width, bars2, width, label='Yes')
plt.ylabel('Frequency')
plt.title('Figure 13: Side by Side Bar Plot of Votes by Gun Ownership and Gun Law Support (n=397)')
plt.xticks(ind + width / 2, ('No','Yes'))
plt.legend(['Favor', 'Oppose'],loc='best')
plt.show()

# Stacked Bar Chart of owngun and gunlaw
bars = np.add(bars1, bars2).tolist()
r = [0,1]
names = ['No','Yes']
barWidth = 0.98
plt.bar(r, bars1, color='#7f6d5f', edgecolor='white', width=barWidth)
plt.bar(r, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=barWidth)
plt.ylabel('Frequency')
plt.xticks(r, names, fontweight='bold')
plt.ylim([0,275])
plt.xlabel('Gun Ownership')
plt.legend(['Favor','Oppose'])
plt.title('Figure 14: Stacked Bar Chart of Gun Ownership and Gun Law Support (n=397)', loc='center')
plt.show()

# 100% Stacked Bar Chart of owngun and gunlaw
own_law_table/own_law_table.sum()*100
bars3 = [70.33, 38.57]
bars4 = [29.67, 61.43]
bars34 = np.add(bars3, bars4).tolist()
names2 = ['Favor','Oppose']
plt.bar(r, bars3, color='#7f6d5f', edgecolor='white', width=barWidth)
plt.bar(r, bars4, bottom=bars3, color='#557f2d', edgecolor='white', width=barWidth)
plt.ylabel('Percentage')
plt.xticks(r, names2, fontweight='bold')
plt.ylim([0,100])
plt.xlabel('Gun Ownership')
plt.legend(['No','Yes'])
plt.title('Figure 15: 100% Stacked Bar Chart of Gun Ownership and Gun Law Support (n=397)', loc='center')
plt.show()


# Q11
# Stratified Analysis of the mean tvhours, age, and chldidel by degree
GSS.groupby('degree')[['tvhours', 'age', 'chldidel']].mean()
# Choosing tvhours since it is the most interesting difference to me


# Q12
# Side-by-Side Boxplot of tvhours stratified by degree
sns.catplot(data=GSS,
               x = 'degree',
               y = 'tvhours',
               kind = 'box'
               )
plt.ylabel('Daily TV Watch Hours')
plt.title('Figure 16: Side-by-Side Boxplot of Daily TV Watch Hours by Highest Degree Achieved (n=397)')
plt.show()


# Q13
# Finding various datapoints for tvhours by degree
# Calculating tvhours IQR by degree
GSS.groupby('degree')['tvhours'].describe()
tvQ1 = GSS.groupby('degree')['tvhours'].quantile(0.25)
tvQ3 = GSS.groupby('degree')['tvhours'].quantile(0.75)
tvIQR = tvQ3 - tvQ1

# Finding tvhours range by degree
GSS.groupby('degree')['tvhours'].agg(['min','max', 'median'])


# Q14
# Creating a scatterplot of tvhours by age
sns.lmplot(data=GSS, x='age',y='tvhours',fit_reg=True)
plt.ylabel('Daily TV Watch Hours')
plt.xlabel('Age')
plt.title('Figure 17: Scatterplot of Daily TV Watch Hours by Age (n=397)', loc='center', fontsize=14)
plt.tight_layout()
plt.show()


# Q16
sp.t.interval(0.90, len(GSS['tvhours'])-1, loc=stat.mean(GSS['tvhours']), scale=stat.stdev(GSS['tvhours']))
sp.t.interval(0.95, len(GSS['tvhours'])-1, loc=stat.mean(GSS['tvhours']), scale=stat.stdev(GSS['tvhours']))
sp.t.interval(0.99, len(GSS['tvhours'])-1, loc=stat.mean(GSS['tvhours']), scale=stat.stdev(GSS['tvhours']))























