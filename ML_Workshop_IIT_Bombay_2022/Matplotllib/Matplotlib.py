#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt


# In[2]:


days=[1,2,3,4,5,6,7]


# In[3]:


likes=[567,89,548,658,550,479,649]


# In[13]:


plt.title("Social media analyzation")
plt.xlabel("days")
plt.ylabel("likes")
plt.plot(days,likes,color="red",marker="o",markerfacecolor="black",linestyle="--")
plt.grid(linewidth=3,color="orange")


# In[14]:


f_book = [345,789,112,458,458,697,879]
insta = [128,999,457,789,648,432,153]
ytube = [548,547,985,62,4,784,999]


# In[15]:


days


# In[26]:


plt.title("comparision")
plt.xlabel("days of week")
plt.ylabel("No. of likes")
plt.plot(days,f_book,color="blue",label="fbook")
plt.plot(days,insta,color="green",label="insta")
plt.plot(days,ytube,color="red",label="ytube")
plt.grid()
plt.legend()
plt.savefig("D:\graph.png")


# In[ ]:




