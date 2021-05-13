#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv('C:/Users/kushal/Desktop/LeetCode-Files/Statistics/iqr_data.csv')


# In[6]:


df=df.drop(columns='Unnamed: 0')


# In[7]:


df


# In[10]:


df.describe() #18 19 indexed heights are outliers


# In[11]:


Q1=df.height.quantile(0.25)
Q3=df.height.quantile(0.75)
IQR=Q3-Q1
IQR


# In[12]:


lower_limit=Q1-1.5*IQR
upper_limit=Q3+1.5*IQR


# In[13]:


upper_limit,lower_limit


# In[14]:


df[(df.height<lower_limit)|(df.height>upper_limit)]


# In[15]:


df=df[(df.height>lower_limit)&(df.height<upper_limit)]


# In[16]:


df


# In[ ]:




