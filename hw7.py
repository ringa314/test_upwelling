# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 02:00:31 2025
MAST638: homework 7

@author: Adrian Ring
"""
import pandas as pd
import glob
import os
import sys
import matplotlib.pyplot as plt
import numpy as np

#===========================================================================
# build dataframe in pandas
#===========================================================================
###################
# load station data
###################
path = r'C:/Users/brave/Downloads/Homework/data' # use your path
all_files = glob.glob(os.path.join(path + "/*.csv")) # all csv files in folder
df_list = (pd.read_csv(file) for file in all_files) 
# Concatenate all DataFrames
df = pd.concat(df_list, ignore_index=True)

#############################
# convert datetime to y, m, d
#############################
df['time'] = pd.to_datetime(df['timestamp']) 
df['Month'] = df['time'].dt.month 
df['Years'] = df['time'].dt.year

####################
# variable selection
####################
v_names = ['Month', 'station_id', 'time', 'chlora_value']
df_v = df[v_names].copy() # dataframe with all relevant columns

#===========================================================================
# data preprocessing
#===========================================================================
#################
# remove outliers
#################
data_value = [col for col in df_v.columns if col.endswith('value')] # extract all data values in df_data
for col in data_value: # remove outliers for data ending in "-value" suffix
    q1, q3 = np.percentile(df_v.loc[:, col].dropna(), [0, 90])  # turkey fences
    iqr = q3-q1
    lower_bound = q1-(iqr*1.5)
    upper_bound = q3+(iqr*0.8)
    df_v.loc[(df_v[col] > upper_bound) | (df_v[col] < lower_bound), col] = np.nan  
#sys.exit()
##################
# temporal binning
##################
df_m_avg = (df_v
         .groupby(['station_id','Month']) # dataframe organized by both station and month
         .mean(numeric_only = True)    # monthly mean across years
         .reindex(range(1, 13), level='Month')
         .reset_index()
)

# claude
df_chl = df_m_avg.pivot(index='station_id', columns='Month', values='chlora_value')
df_chl.columns = [f'month_{col}' for col in df_chl.columns]

##########################################
# Select variables and remove missing data
##########################################
pd.DataFrame(df_chl).isnull().sum()
df_chl = df_chl.dropna(axis=1)

#######################
# data visualization
#######################
# fig, axes = plt.subplots(3,6, figsize=(30,15))
# axes = axes.flatten()
# months = range(0,12)
# for i in range(18):
#     row = df_chl.iloc[i,0:]
#     index_label = str(df_chl.index[i])[-6:]
#     axes[i].plot(months,row.values, marker='o')
#     axes[i].text(0.05, 0.9, 
#                  f"{index_label}",  
#                  transform=axes[i].transAxes, 
#                  fontsize=25)
#     axes[i].grid(True)
# fig.supxlabel("Month", fontsize=25)
# fig.supylabel("Chl", fontsize=25)
# plt.tight_layout()
# plt.show()

####################
# k-means clustering
####################
# raschka & mirjalili
distortions = []
for i in range(1, 11):
    km = KMeans(n_clusters=i,
    init='k-means++',
    n_init=10,
    max_iter=300,
    random_state=0)
    km.fit(X)
    distortions.append(km.inertia_)
plt.plot(range(1,11), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.tight_layout()
plt.show()
