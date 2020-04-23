# Importing Libraries
import requests
import pandas as pd 

# Data Source
source_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSz8Qs1gE_IYpzlkFkCXGcL_BqR8hZieWVi-rphN1gfrO3H4lDtVZs4kd0C3P8Y9lhsT1rhoB-Q_cP4/pub?output=xlsx'

# Getting Data from Source
r = requests.get(source_url, allow_redirects=True)

# Writing Data to File for easy Access and Security
open('dataset.xlsx', 'wb').write(r.content)

# Getting Data from File to Pandas Data Frame
raw_data = pd.read_excel('dataset.xlsx',sheet_name='Raw_Data')

# Cleaning and Obtaining just the required columns of the data
data = raw_data[['Detected State','Detected City']]

# Removing all columns with missing values
data = data.dropna()

# Resetting index to avoid error
data.reset_index(inplace = True)

# Removing the extra column created by resetting index
data.drop(columns = ['index'],inplace = True)

