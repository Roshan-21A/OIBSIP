#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("Unemployment in India.csv")


# In[3]:


data.describe


# In[4]:


#check the head of data
data.head()


# In[18]:


#check the back of the data
data.tail()


# In[19]:


#info about data
data.info()


# In[5]:


print(data.isnull().sum())


# In[6]:


plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr())
plt.show()


# In[7]:


data.columns


# In[16]:


#now, we are checking start with a pairplot, and check for missing values
sns.heatmap(data.isnull(),cbar=False)


# In[23]:


#Which state has the most data
color = sns.color_palette()
cnt_srs = data.Region.value_counts()

plt.figure(figsize=(12,8))
sns.barplot(cnt_srs.index, cnt_srs.values, alpha=0.8, color=color[1])
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Region', fontsize=12)
plt.title('Count the region', fontsize=15)
plt.xticks(rotation='vertical')
plt.show()


# In[26]:


#see the number of unique Regions
data.Region.nunique()


# In[ ]:




