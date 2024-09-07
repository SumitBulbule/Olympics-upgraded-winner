--- Importing libraries
import numpy as np
import pandas as pd

--- Reading files
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')


df.head()
region_df.head()

--- Filtering only summer season data
df = df[df['Season'] == 'Summer']

df.shape

--- merging two dataframes
df = df.merge(region_df,on='NOC',how='left')

df['region'].value_counts()
df['region'].unique()

--- Handling Null values
df.isnull().sum()


























