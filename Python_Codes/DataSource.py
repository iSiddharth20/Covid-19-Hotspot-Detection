# Importing Libraries
import io
import requests
import pandas as pd 

# Obtaining the Data
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSc_2y5N0I67wDU38DjDh35IZSIS30rQf7_NYZhtYYGU1jJYT6_kDx4YpF-qw0LSlGsBYP8pqM_a1Pd/pub?output=csv'
res = requests.get(url)

# Storing the data in a Pandas Data Frame
raw_data = pd.read_csv(io.BytesIO(res.content), sep=',')

# Cleaning and Obtaining just the required columns of the data
data = raw_data[['Detected State','Detected City']]

# Removing all columns with missing values
data = data.dropna()

# Resetting index to avoid error
data.reset_index(inplace = True)

# Removing the extra column created by resetting index
data.drop(columns = ['index'],inplace = True)

