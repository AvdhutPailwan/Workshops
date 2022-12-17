#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[2]:


# Numpy
import numpy as np     # np is short form for numpy


# In[3]:


a=np.array([4,9,3,89,6])


# In[4]:


type(a)


# In[5]:


a[-2],a[3]


# In[6]:


a[0:3:2]


# In[7]:


a[1:4:]


# In[8]:


a[-2:-5:-1],a[-2:0:-1]


# In[9]:


a[::4]


# In[10]:


a[-1:-6:-4]


# In[11]:


a=np.array([7,9,45,4.5,12.8],dtype="int")


# In[12]:


a


# In[13]:


a = np.arange(4,9,1) # start, end, increment value by


# In[14]:


a


# In[15]:


np.arange(7)


# In[16]:


a.ndim #dimension


# In[17]:


#creating 2-D array
a1=np.array([[7,8],[9,5],[3,8]])


# In[18]:


a1


# In[19]:


a1.ndim


# In[20]:


a1[0]


# In[21]:


a1[1][0]


# In[22]:


# create 2-D array using arange()
a=np.arange(20)


# In[23]:


a


# In[24]:


a1.shape


# In[25]:


a.ndim


# In[26]:


a.shape


# In[27]:


a=a.reshape(5,4)  #change dimension of array


# In[28]:


a


# In[29]:


# a[r,c] --slicing
a[1:3:1,0:2:1]


# In[30]:


a[2:4:,2:4:]


# In[31]:


# 3-D array
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[2,5,7]]])


# In[32]:


a


# In[33]:


a.ndim


# In[34]:


a.shape


# In[35]:


# 3-D array with arange
a = np.arange(30)


# In[36]:


a


# In[37]:


a.ndim


# In[38]:


a=a.reshape(3,2,5)


# In[39]:


a


# In[40]:


#a[n,r,c] ---slicing
a[0:2:1,1:2:1,2:4:1]


# In[42]:


# 0,4,20,24
a[::2,:1:,::4]


# In[ ]:




