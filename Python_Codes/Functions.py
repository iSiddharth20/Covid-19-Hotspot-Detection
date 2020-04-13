import pandas as pd

'''
A function that can identify and returns name of city in each state that has maximum number of cases.
Used for Mathematical Proof of Concept.
'''

def identify(DF):
    DF.reset_index(inplace = True)
    LST = []
    # 'x' will have all the names of Cities in the State
    for x in DF['Detected City'].unique():
        # 'temp' is a DataFrame that contains details of the Current City
        temp = DF[DF['Detected City']==x]
        # The List 'DF' contains sub-lists with 'Name of City' and 'Number of Registered Cases'
        LST.append([x,temp['Detected City'].count()])
    # Converting the Nested List into a DataFrame
    DF_df = pd.DataFrame(LST)
    # Defining the Column Names
    DF_df.columns = ['City_Name','Number_Of_Patients']
    # Arranging the DataFrame in Descending Order to Obtain Cities with Max Cases on Top
    DF_df = DF_df.sort_values(by=['Number_Of_Patients'],ascending=False)
    DF_df.reset_index(inplace = True)
    return DF_df['City_Name'][0]


'''
A function that can identify and returns name of city and number of patients in each state.
Used for Visual Proof of Concept.
'''

def divide(DF):
    LST = []
    # 'x' will have all the names of Cities in the State
    for x in DF['Detected City'].unique():
        # 'temp' is a DataFrame that contains details of the Current City
        temp = DF[DF['Detected City']==x]
        # The List 'DF' contains sub-lists with 'Name of City' and 'Number of Registered Cases'
        LST.append([x,temp['Detected City'].count()])
    # Converting the Nested List into a DataFrame
    DF_df = pd.DataFrame(LST)
    # Defining the Column Names
    DF_df.columns = ['City_Name','Number_Of_Patients']
    # Arranging the DataFrame in Descending Order to Obtain Cities with Max Cases on Top
    DF_df = DF_df.sort_values(by=['Number_Of_Patients'],ascending=False)
    return DF_df