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

#Remove duplicates of the same registered provider name, retaining only the head office: 
