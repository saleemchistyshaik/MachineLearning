#!/usr/bin/env python
# coding: utf-8

# In[10]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


x = [0.1,0.2,0.3,0.4,0.5,0.6]
y = [1,2,3,4,5,6]


# In[14]:


#rd r-- r* r#
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(x,y,color = 'red', marker = 'D', linestyle='--', alpha=0.7)
plt.show()


# In[4]:


A = [1,2,3,4,5,6,7]
Loss = [50,49,48,47,46,45]
Profit = [5,10,20,30,40,50]


# In[17]:


plt.plot(A,label = 'A')
plt.plot(Profit, color = 'green',label = 'Profit')
plt.plot(Loss, color = 'red',label = 'Loss')
plt.legend( loc = 'best',shadow = True, fontsize = 'large')
plt.grid()
plt.show()


# In[19]:


#bar chart
import numpy as np
x = ['A','B','C','D']
y = [98,136,89,27]
p = [20,50,30,10]


# In[21]:


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.bar(x,y, width=0.4,label = 'Sales')
plt.bar(x,p,width=0.4,label = 'Revenue')
plt.legend()


# In[23]:


#barh
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.barh(x,y,label = 'Sales')
plt.barh(x,p,label = 'Revenue')
plt.legend()


# In[27]:


#histogram
A = [100,20,30,10,200,40,50,70,90]

plt.hist(A,bins=3,rwidth=0.5,color='green', )


# In[4]:


#histogram
A = [100,20,30,10,200,40,50,70,90]
B = [10,30,20,50,40,60,80,70]

plt.hist([A,B],bins=3,rwidth=0.5,color=['green','red'] )


# In[38]:


labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# In[26]:


#scatter
x = [1,2,3]
y = [4,5,6]
plt.xlabel('Xaxis')
plt.ylabel('Yaxis')
plt.scatter(x,y,color="pink",marker ="D")
plt.show()


# In[6]:


import pylab
import scipy
x = scipy.linspace(-2,2,1500)
y1 = scipy.sqrt(1-(abs(x)-1)**2)
y2 = -3*scipy.sqrt(1-(abs(x)/2)**0.5)
pylab.fill_between(x, y1, color='red')
pylab.fill_between(x, y2, color='red')
pylab.xlim([-2.5, 2.5])
pylab.text(0, -0.4, 'I love someone', fontsize=30, fontweight='bold',
           color='blue', horizontalalignment='center')


# In[27]:


import os
os.getcwd()


# In[ ]:




