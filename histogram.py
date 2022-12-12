import pandas as pd
import matplotlib.pyplot as plt
import csv
df = pd.read_csv(r'C:\Users\szech\Desktop\sampleclient.csv')         
s = df['Total Profit ($)'] # Select the cyl column to get a series
s.plot(
    kind = 'hist'
)
plt.savefig('histogram.png')
plt.show()  