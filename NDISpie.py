import pandas as pd 
import csv
import matplotlib.pyplot as plt 
df = pd.read_csv(r'C:\Users\szech\Desktop\registered_providers_NDIS.csv')
for col in df.columns:
    print(col)

s = df.groupby('Postcode')['NoWebsiteFlag'].sum() 
s.plot(
    kind = 'hist'
)
#s.plot(
        #kind = 'bar',
#) Can also do multiple plots on the same axes

plt.title("NDIS providers with no website by state")
plt.ylabel('Proportion of state against total without a website')
plt.savefig('NDISprovidersbystate.png')   
plt.show()  
s = df.groupby('cut').size()
s.plot(
    kind = 'bar',
)
s.plot(
    kind = 'line',
)
plt.savefig('plot.png') 
plt.show()