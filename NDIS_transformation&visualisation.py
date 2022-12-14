import pandas as pd
import matplotlib.pyplot as plt
import csv
import seaborn
df = pd.read_csv(r'C:\Users\szech\Desktop\registered_providers_NDIS.csv')    

#Checking column headers: 
#for col in df.columns:
    #print(col)

#Checking the first 5 rows: 
#df_first_rows = df.head(5)
#print(df_first_rows)

#Now to start editing the csv file. First, remove duplicates of the same registered provider name, only one office is required:
df = df.drop_duplicates(subset=['Registered Provider Name'], inplace=False)
df = df.to_csv("registered_providers_NDIS.csv", index=False)
