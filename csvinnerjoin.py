import pandas as pd
import csv
from pandas import DataFrame
df1 = pd.read_csv("students.csv")
#print(df1.head())

df2 = pd.read_csv("students1.csv")

df3 = df1.merge(df2, how='inner')

print (df3)   

df3.to_csv('csvoutput1.csv', header=True) #to export to CSV

df3.to_json('jsonoutput.json') #to export to JSON 

