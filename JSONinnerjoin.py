#inner join on two JSON files 

import pandas as pd
from pandas import DataFrame
df1 = pd.read_json("customerreviews.json", lines=True)
df2 = pd.read_json("customerreviews1.json",lines=True)

print(df1.head())
print(df2.head())

df3 = df1.merge(df2,how='inner')

print(df3) 

df3.to_json('jsoninnerjoinoutput.json') #to export to JSON 
