import matplotlib.pyplot as plt

import pandas as pd

# add the following line in order to have the plots inside the notebook
% matplotlib inline

# read the data
df = pd.read_csv('data.csv')

# Rename columns in data frame as [x,y]
df.columns = ____;

# Plot axis x vs axis y
plt.____;
