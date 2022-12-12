import csv
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\szech\Desktop\sampleclient.csv') 
s = df.groupby('Campaign Name').size()
s.plot(
    kind = 'bar',
)
plt.savefig('plot.png') 
plt.show() 