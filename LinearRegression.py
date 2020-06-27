#!/usr/bin/env python
# coding: utf-8

# # Linear Regression HandsOn
# 

# In[23]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model


# In[24]:


import os
os.getcwd()


# In[3]:


df = pd.read_excel('Linear.xlsx')


# In[4]:


df


# In[5]:


#correlation coefficents 
df.corr()


# In[6]:


df.plot(kind = 'scatter', x = 'Price', y = 'SquareFt')
plt.show()


# #linear regression formula y = mx+c
# #where m is slope of line . x is the predicting value , c is the intercept

# In[7]:


df.plot(kind='box')
plt.show()


# In[8]:


df.corr()


# In[9]:


Pr = pd.DataFrame(df['Price'])
Sqr = pd.DataFrame(df['SquareFt'])


# In[10]:


Pr


# In[11]:


Sqr


# In[12]:


#build model
lm = linear_model.LinearRegression()
model = lm.fit(Pr,Sqr)
model


# In[13]:


model.coef_


# In[14]:


model.intercept_


# In[15]:


model.score(Pr, Sqr)


# In[16]:


#predict new values
Price_new = 3300
SquareFt_predict = model.predict([[Price_new]])
SquareFt_predict


# In[17]:


#more values
x = ([2700,3500,4500])
x = pd.DataFrame(x)
y = model.predict(x)
y 


# In[18]:


y= pd.DataFrame(y)
y


# In[19]:


data = pd.concat([x,y], axis = 1, keys= ['Price_new','SquareFt_predict'])
data


# In[27]:


#visualize data do error
df.plot(kind = 'scatter', x = 'Price',y = 'SquareFt')
#plot regression line
plt.plot(Pr, model.predict(Pr),color='red',linewidth=2)
#plotting line for predicted values
plt.scatter(Price_new, SquareFt_predict, color='black')
plt.scatter(x,y)
plt.plot(x,y, color = 'blue', linewidth = 1)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




