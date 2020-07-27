#!/usr/bin/env python
# coding: utf-8

# ## 웹크롤링

# In[5]:


get_ipython().system('pip install bs4')


# https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&tg=0&date=20200201

# In[6]:


import pandas as pd


# In[8]:


mov_data = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&tg=0&date='


# In[11]:


data=pd.read_html(mov_data)
data


# In[12]:


type(data),len(data)


# In[13]:


df=data[0]


# In[22]:


df.head()


# In[23]:


data[0]


# In[24]:


data[1]


# In[27]:


data[2]


# In[28]:


df.info()


# In[30]:


df['영화명'].head()


# In[31]:


pick=['순위','영화명','평점.1']
df2=df[pick]


# In[32]:


df2


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




