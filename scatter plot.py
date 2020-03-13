#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


# In[11]:


df = pd.read_csv("E:\\charts\data sets\google-play-store-apps\googleplaystore.csv",nrows=100)
df.shape


# In[19]:


x = df['Rating']
a = x.head()
print(a)
y = df['Reviews']
b = y.head()
print(b)
plt.xlabel("Ratings")
plt.ylabel("Reviews")
plt.title('Google Play Store Scatter Plot')
plt.scatter(x,y)


# In[33]:


x = df['Rating']
y = df['Reviews']
plt.xlabel("Ratings")
plt.ylabel("Reviews")
plt.title('Google Play Store Scatter Plot')
plt.figure(figsize=(16,9))
plt.scatter(x,y,color = "r",marker = "*",s= 100,alpha = 0.9,linewidth = 2)


# In[35]:


x = df['Rating']
y = df['Reviews']
z = df['Installs']
plt.xlabel("Ratings")
plt.ylabel("Reviews & Installs")
plt.title('Google Play Store Scatter Plot')
plt.figure(figsize=(16,9))
plt.scatter(x,y,color = "r",marker = "*",s= 100,alpha = 0.9,linewidth = 2)
plt.scatter(x,z,color = "b",marker = "+",s= 100,alpha = 0.6,linewidth = 5)


# In[ ]:




