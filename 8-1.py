#Design a python program using Pandas library functions.

import pandas as pd
from pandas import DataFrame

df = pd.read_csv("Sample.csv")
#print(df)

"""print(df.head(3))

print(df.describe())

print(df.memory_usage(deep = True))

print(df.loc[0:4, ['Name','Age','State']])

print(df['State'].value_counts())

print(df.groupby(by = 'State').Salary.mean())

 
"""

df['Gender'] = df.Gender.astype('category')
print(df['Gender'])
      
df['DOB'] = pd.to_datetime(df['DOB'])
print(df['DOB'])

"""
df.drop_duplicates(inplace = True)
print(df)
"""