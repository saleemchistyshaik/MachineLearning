#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd


# In[40]:


df = pd.read_csv('titanic.csv')
df


# In[41]:


input = df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked','Survived'], axis = 'columns')
input


# In[43]:


put = input['Sex'].replace({'male':'1','female':'2'})
put


# In[45]:


input['Sex'] = put


# In[46]:


input


# In[47]:


input.isna()


# In[50]:


input = input.fillna(input.Age.mean())


# In[51]:


input


# In[52]:


target = df['Survived']
target


# In[53]:


from sklearn.model_selection import train_test_split


# In[56]:


x_train,x_test,y_train,y_test = train_test_split(input,target,test_size = 0.5)


# In[57]:


x_train


# In[58]:


x_test


# In[59]:


y_train


# In[60]:


y_test


# In[61]:


from sklearn import tree


# In[73]:


model = tree.DecisionTreeClassifier()


# In[74]:


model.fit(x_train,y_train)


# In[83]:


model.score(x_train,y_train)#just for demo in reality we check score for testing data only as of we are using model


# In[84]:


model.score(x_test,y_test)


# In[90]:


x_test.head(10)


# In[97]:


model.predict([[3, 2, 29.699118, 22.3583]])


# In[98]:


target.iloc[127:129]


# In[ ]:




