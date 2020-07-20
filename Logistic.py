#!/usr/bin/env python
# coding: utf-8

# # Logistic Regression
# 

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


data = pd.read_csv('data.csv')


# In[3]:


data


# In[57]:


frame = pd.DataFrame(data)
frame


# In[60]:


x = data.iloc[:,:-1].values
y = data.iloc[:,1].values


# In[61]:


x.shape


# In[62]:


y.shape


# In[63]:


from sklearn.model_selection import train_test_split


# In[64]:


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.15)


# In[90]:


#for arranging values in order
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn import utils


# In[91]:


sc = StandardScaler()

x_train = sc.fit_transform(x_train)

x_test = sc.transform(x_test)


# In[92]:


from sklearn.linear_model import LogisticRegression


# In[93]:


model = LogisticRegression()


# In[94]:


lab_enc = preprocessing.LabelEncoder()
training_scores_encoded = lab_enc.fit_transform(y_train)
print(training_scores_encoded)
print(utils.multiclass.type_of_target(y_train))
print(utils.multiclass.type_of_target(y_train.astype('int')))
print(utils.multiclass.type_of_target(training_scores_encoded))


# In[95]:


model = model.fit(x_train,training_scores_encoded)


# In[96]:


model


# In[97]:


prediction = model.predict(x_test)


# In[98]:


prediction


# In[136]:


from sklearn.metrics import confusion_matrix,accuracy_score


# In[137]:


acc =  accuracy_score(y_test.round(), prediction)


# In[138]:


cm = confusion_matrix(y_test.round(), prediction)


# In[139]:


acc


# In[140]:


cm


# # example 2

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn import utils


# In[2]:


data = pd.read_csv('Salary_Data.csv')


# In[3]:


data


# In[4]:


x = pd.DataFrame(data['YearsExperience'])
y = pd.DataFrame(data['Salary'])


# In[5]:


x


# In[6]:


y


# In[7]:


from sklearn.linear_model import LogisticRegression


# In[8]:


model = LogisticRegression()


# In[9]:


model.fit(x,y)


# In[10]:


pred = model.predict(x)


# In[11]:


pred


# In[12]:


from sklearn.metrics import confusion_matrix


# In[13]:


c = confusion_matrix(y,pred)


# In[14]:


c


# 

# In[15]:


model.score(y,pred)


# In[ ]:





# In[ ]:





# In[ ]:




