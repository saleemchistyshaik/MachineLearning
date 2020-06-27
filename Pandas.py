#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


x = [1,2,3,4]
y = [14,5,6,8]
pd.Series(x,y)


# In[6]:


x = [1,2,3,4]
y = [14,5,6,8]
pd.DataFrame(x,y)


# In[7]:


RS = pd.read_excel('cropdata.xlsx')


# In[19]:


RS.shape


# In[20]:


RS.head(19)


# In[21]:


RS.head()


# In[22]:


RS.tail()


# In[9]:


RS.head(19)


# In[10]:


RS.isna()


# In[11]:


RS.isna().sum()


# In[12]:


RS.isna().sum().sum()


# In[23]:


RS.describe()


# In[26]:


RS['Year'].fillna(value = 0, inplace = True)


# In[15]:


RS.head()


# In[16]:


RS.head(19)


# In[17]:


RS['Profit'].fillna(value= 0, inplace = True)


# In[18]:


RS.head(19)


# In[19]:


RS['Loss'].fillna(value = 0, inplace = True)


# In[20]:


RS.head(19)


# In[32]:


RS['Year'].sum()


# In[33]:


RS[['Year','Profit']].sum()


# In[23]:


RS['Year'].astype(int)


# In[24]:


RS['Profit'].astype(int)


# In[25]:


RS['Loss'].astype(int)


# In[26]:


RS['Profit'].sum(axis = 0)


# In[35]:


RS.iloc[[2,4]].sum(axis = 0)


# In[40]:


RS.rename(columns = {'Profit': 'Profit-value'}, inplace = True)


# In[41]:


RS.head()


# In[42]:


RS.iloc[1:4].head()


# In[43]:


RS.rename(columns = {'Profit-value':'Profit'})


# In[59]:


RS[['Year','Loss']].iloc[1:4]


# In[65]:


RS.drop_duplicates().shape


# In[72]:


RS[RS['Year'] == 1991].iloc[0:4]


# In[73]:


RS.dtypes


# In[74]:


RS['Year'].astype(float)


# In[75]:


RS['Year'].astype(int)


# In[ ]:





# In[ ]:





# In[ ]:




