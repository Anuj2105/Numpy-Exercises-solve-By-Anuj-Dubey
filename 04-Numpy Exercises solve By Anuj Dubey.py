#!/usr/bin/env python
# coding: utf-8

# ___
# 
# Mr. Yogesh P Murumkar (Mob. 9657080905)
# 
# www.youtube.com/yogeshmurumkar
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[2]:


np.zeros(10)


# #### Create an array of 10 ones

# In[3]:


np.ones(10)


# #### Create an array of 10 fives

# In[4]:


np.zeros(10)+5


# #### Create an array of the integers from 10 to 50

# In[5]:


np.arange(10,)


# #### Create an array of all the even integers from 10 to 50

# In[6]:


np.arange(10,52,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[8]:


arr1=[[[0,1,2],[3,4,5],[6,7,8]]]
np.array(arr1)


# #### Create a 3x3 identity matrix

# In[9]:


np.eye(3,3)


# #### Use NumPy to generate a random number between 0 and 1

# In[11]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[12]:


np.random.rand(25) 


# #### Create the following matrix:

# In[13]:


arr1=np.arange(0.01, 1.01, 0.01)
arr1.reshape(10,10)


# In[14]:


arr1=np.arange(0.01, 1.01, 0.01)
arr1.reshape(10,10)


# In[15]:


arr1=np.arange(0.01, 1.01, 0.01)
arr1.reshape(10,10)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[16]:


np.linspace(0, 1, 20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[17]:


arr=np.arange(1,26).reshape(5,5)


# In[18]:


arr


# In[19]:


np.arange(1,26).reshape(5,5)


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[20]:


arr1=[[12,13,14,15],[17,18,19,20],[22,23,24,25]]
np.array(arr1)


# In[22]:


arr1=[[12,13,14,15],[17,18,19,20],[22,23,24,25]]
arr2=np.array(arr1)
arr2


# In[23]:


arr2[1,3]


# In[ ]:





# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[24]:


arr2[1,3]


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[ ]:


arr


# In[25]:


arr[0:3,1:2]


# In[26]:


arr[0:3,1:2]


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[31]:


arr[4:,0:]


# In[29]:


arr[4:,0:]


# In[ ]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[32]:


arr[3:,0:]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[ ]:


arr


# In[33]:


np.sum(arr)


# In[34]:


np.sum(arr)


# #### Get the standard deviation of the values in mat

# In[35]:


np.std(arr)


# #### Get the sum of all the columns in mat

# In[36]:


np.sum(arr,axis=1)


# In[37]:


arr[:,4:]


# In[38]:


np.sum(arr,axis=0)


# # Great Job!

# In[ ]:


#Thank You

