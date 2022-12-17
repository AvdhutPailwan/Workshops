#!/usr/bin/env python
# coding: utf-8

# In[1]:


# use kaggle.com to access datasheets


# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv("F:\Avdhut\Workshops\ML_Workshop_IIT_Bombay_2022\pandas\dataset2\insurance.csv")


# In[4]:


pd.read_csv(r"F:\Avdhut\Workshops\ML_Workshop_IIT_Bombay_2022\pandas\dataset2\insurance.csv")


# In[5]:


df.head(2)


# In[6]:


df


# In[7]:


a = pd.read_csv("insurance.csv")


# In[8]:


a


# In[9]:


a.shape


# In[10]:


type(a)


# In[11]:


a.head()


# In[12]:


a["sex"]


# In[13]:


a[["sex"]]


# In[14]:


df.head(1)


# In[15]:


df.sex


# In[16]:


df[["sex"]]


# In[17]:


df[["sex","charges"]]


# In[18]:


df[["sex","charges","children"]]


# In[19]:


type(df["sex"])


# In[20]:


df


# In[21]:


df[0:50:6]


# In[22]:


# access random dataset --- loc and  iloc
df.iloc[[5,9,6,89,32]]


# In[23]:


import pandas as pd
df=pd.read_csv("F:\Avdhut\Workshops\ML_Workshop_IIT_Bombay_2022\pandas\dataset2\insurance.csv")
df.loc[[57,89],["sex","age"]]


# In[24]:


df.iloc[6:23:5,1:4:2]


# In[25]:


df[df["sex"]=="male"]


# In[26]:


df[df["sex"]=="male"].count()


# In[27]:


df.bmi>30


# In[28]:


df[df.bmi>30]


# In[29]:


df.head(2)


# In[30]:


df[df.bmi.between(25,35)].count()


# In[31]:


df.bmi.between(25,35)


# In[32]:


df.head(1)


# In[33]:


df.age.isin([22,19])


# In[34]:


df[df.children.isin([2,9])].count()


# In[35]:


x = df.groupby("age")


# In[36]:


one = x.get_group(22)


# In[37]:


one

