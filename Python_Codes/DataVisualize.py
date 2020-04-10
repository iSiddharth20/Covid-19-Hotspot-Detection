'''
Data Visualization
'''

# Importing Data Frames from DataSource.py
from DataSource import MH_df , TN_df , DL_df , MP_df

# Importing Libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


'''
Maharashtra Data Visualised
'''
# Defining a Bar Graph
plt.bar(MH_df[:4]['City_Name'], MH_df[:4]['Number_Of_Patients'])
# Print the Bar Graph
plt.show()
# View the Box Plot
sns.boxplot(MH_df[['Number_Of_Patients']])


'''
Tamil Nadu Data Visualised
'''
# Defining a Bar Graph
plt.bar(TN_df[:4]['City_Name'], TN_df[:4]['Number_Of_Patients'])
# Print the Bar Graph
plt.show()
# View the Box Plot
sns.boxplot(TN_df[['Number_Of_Patients']])


'''
Delhi Data Visualised
'''
# Defining a Bar Graph
plt.bar(DL_df[:4]['City_Name'], DL_df[:4]['Number_Of_Patients'])
# Print the Bar Graph
plt.show()
# View the Box Plot
sns.boxplot(DL_df[['Number_Of_Patients']])


'''
Madhya Pradesh Data Visualised
'''
# Defining a Bar Graph
plt.bar(MP_df[:4]['City_Name'], MP_df[:4]['Number_Of_Patients'])
# Print the Bar Graph
plt.show()
# View the Box Plot
sns.boxplot(MP_df[['Number_Of_Patients']])

