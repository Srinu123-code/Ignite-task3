# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1otwKQZZ_UwRML2PsO5POOs5L2Fs-1NK7
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_csv('exams.csv')
data.columns

data.head()

data.isnull().sum()

data['Total_marks']=data['math score']+data['reading score']+data['writing score']

data['average']=data['Total_marks']/3

data.head()

data.describe()

# number of student who got 90 or more than 90 average marks
np.shape(data[data['average']>=90]['average'])[0]

data.rename(columns={'race/ethnicity':'group'}, inplace=True)

a=data['group'].unique()
l=[]

for i in a:
  d=data[data['group']==i]
  l.append(np.sum(d['Total_marks']))
  #print(i,np.sum(d['Total_marks']))

import matplotlib.pyplot as plt
plt.bar(x=a,height=l)
plt.show()

b=data['gender'].unique()
for i in b:
  print(i)
  print(sum(data[data['gender']==i]['Total_marks']))



f=data[(data['math score']>90) &(data['reading score']>90) &( data['writing score']>90)]

import seaborn as s
import matplotlib.pyplot as plt
s.countplot(x='gender', hue='gender', data=f)
plt.show()

for i in data['gender'].unique():
  c=data[data['gender']==i]
  print(i,'\n',c.loc[:,['math score','reading score','writing score']].mean())
  print('\n')

s.violinplot(y='math score', data=data, color='yellow')
plt.show()
s.violinplot(y='reading score', data=data, color='blue')
plt.show()
s.violinplot(y='writing score', data=data, color='red')
plt.show()