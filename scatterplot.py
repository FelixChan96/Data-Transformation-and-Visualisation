import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/felixchan/Desktop/iris.csv',index_col=0) 
df.plot(
    kind = 'scatter',
    x = 'Petal.Width',
    y = 'Sepal.Width',
    marker = '.', # Set the shape of the markers
)
plt.savefig('plot.png')  
plt.show() 
