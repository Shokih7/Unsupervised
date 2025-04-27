###Basic
import pandas as pd

###Visuale
import warnings
from plot_all import PlotAll
from grouping import *
from clustering import Clustering
from getdata import GetData
warnings.filterwarnings('ignore')


##Data
# For getting the raw data and apply the clustering algorithms use the next 4 rows. We used the dataframe to ensure the same results as in the paper.
# get = GetData()
# df = get.df
# clustering = Clustering(df)
# df = clustering.df
df = pd.read_csv('results_df.csv')

#Analyze

plot = PlotAll(df)

for i in fet1:
    print(i)
    print(df.groupby('spec_cluster_habits')[i].describe())
    print()

for i in intresting:
    for j in i:
        print(j)
        print(df.groupby('spec_cluster_habits')[j].describe())
        print()


