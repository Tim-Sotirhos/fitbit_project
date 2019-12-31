import pandas as pd 

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

import warnings
warnings.filterwarnings('ignore')

import prepare

def plot_columns(df):
    for col in df.columns:
        plt.figure(figsize = (16,4))
        plt.plot(df.resample('W').sum()[col])
        plt.xlabel('date')
        plt.ylabel(col)
        plt.show()
        
