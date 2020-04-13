# Importing Required Packages
from DataSource import data
from functions import divide
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

'''
Kerela Data
'''
KL_Data = data[data['Detected State'] == 'Kerala']
KL_Data = KL_Data.dropna()
KL_df = divide(KL_Data)

# Defining a Bar Graph
plt.bar(KL_df[:4]['City_Name'], KL_df[:4]['Number_Of_Patients'])

# Print the Graph
plt.show()

'''
Delhi Data
'''
DL_Data = data[data['Detected State'] == 'Delhi']
DL_Data = DL_Data.dropna()
DL_df = divide(DL_Data)

# Defining a Bar Graph
plt.bar(DL_df[:4]['City_Name'], DL_df[:4]['Number_Of_Patients'])

# Print the Graph
plt.show()