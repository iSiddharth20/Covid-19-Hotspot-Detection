# Importing Required Packages
from DataSource import data
from functions import identify
import pandas as pd

# The dictionary SD will have Name of State and Name of corresponding city with max cases
sd = {}

for s_name in data['Detected State'].unique():
    sd[s_name] = identify(data[data['Detected State']==s_name])

# Converting the Obtained Dictionary to a Pandas Data Frame
final_data = pd.DataFrame.from_dict(sd, orient='index')

# Resetting Index so as to assign Column Names
final_data.reset_index(inplace = True)

# Assigning the Column Names
final_data.columns = ['Name of State','City with Maximum Cases']

# Printing Results
pritn(final_data)