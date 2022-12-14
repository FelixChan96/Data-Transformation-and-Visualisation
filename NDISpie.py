import pandas as pd 
import csv
import matplotlib.pyplot as plt 
df = pd.read_csv(r'C:\Users\szech\Desktop\registered_providers_NDIS.csv')
s = df.groupby('State')['Total Profit ($)'].mean() #Find the mean profit of each campaign
s.plot(
    kind = 'pie'
)
plt.savefig('NDISprovidersbystate.png')   
plt.show() 