import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\szech\Desktop\sampleclient.csv') 
df.plot(
    kind = 'scatter',
    x = 'Postcode',
    y = 'Total Profit ($)',
    marker = '.', # Set the shape of the markers
)
plt.savefig('plot.png')  
plt.show()  
