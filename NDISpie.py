import pandas as pd 
import csv
import matplotlib.pyplot as plt 
df = pd.read_csv(r'C:\Users\szech\Desktop\registered_providers_NDIS.csv')
#for col in df.columns:
    #print(col)

s = df.groupby('State')['NoWebsiteFlag'].sum() #Find the mean profit of each campaign
s.plot(
    kind = 'pie'
)
plt.title("NDIS providers by state")
plt.ylabel('Has no website with respect to other states')
plt.savefig('NDISprovidersbystate.png')   
plt.show() 
