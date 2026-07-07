# importing necessary libraries & packages
import pandas as pd
import matplotlib.pyplot as plt

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




