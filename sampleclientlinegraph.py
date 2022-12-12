#To import a CSV file with Python: 

import pandas as pd 
import csv

df = pd.read_csv(r'C:\Users\szech\Desktop\sampleclient.csv')

import matplotlib.pyplot as plt 
s = df.groupby('Campaign Name')['Total Profit ($)'].mean() # Find the mean profit of each campaign
s.plot(
    kind = 'line' # You don't need this - it's the default kind
)
plt.savefig('plot.png') 
plt.show()