import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

df = pd.read_csv('data.csv')

# Rename columns in data frame as [x,y]
df.columns = ['x', 'y']

# Plot axis x vs axis y
plt.plot(df.x, df.y, 'bs')
