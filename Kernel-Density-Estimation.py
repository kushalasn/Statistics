#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


cars=sns.load_dataset('mpg').dropna()


# In[7]:


cars.shape


# In[12]:


cars.horsepower


# In[22]:


sns.kdeplot(cars.horsepower,cumulative=True)
#univariate plot - one dimension(1D)


# In[25]:


#multivariate-(2D) plots
sns.kdeplot(cars.horsepower,cars.mpg,shade=True,shade_lowest=False)


# In[ ]:




