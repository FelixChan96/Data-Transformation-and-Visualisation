import pandas as pd 
import csv
import matplotlib.pyplot as plt 
df = pd.read_csv(r'C:\Users\szech\Desktop\sampleclient.csv')
s = df.groupby('Campaign Name')['Total Profit ($)'].mean() #Find the mean profit of each campaign
s.plot(
    kind = 'pie'
)
plt.savefig('plot.png')   
plt.show() 