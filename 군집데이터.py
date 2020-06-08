#!/usr/bin/env python
# coding: utf-8

# ## boolean

# In[1]:


True==False


# In[2]:


True!=0


# In[3]:


False==0


# In[5]:


True or False


# In[73]:


1=='1'


# In[103]:


a=True and False
a


# In[97]:


a=False and True
a


# ## 문자열

# In[9]:


eng='korea COVID 19'


# In[13]:


eng.lower()


# In[104]:


eng.upper()


# In[202]:


eng.lower()
eng.upper()


# ## Lists[]

# In[58]:


data=[]


# In[63]:


data.append('java')
data


# In[19]:


data[0],data[-1],data[1:],data[:2]


# In[61]:


data.sort()
data


# In[203]:


data.reverse()
data


# In[205]:


a='나무위키 꺼라'
a[2:]


# ## Tuple
# ### 튜플은 변동이 안된다.

# In[66]:


b=(1,2,3,'사','오')
c=1,2,3
c


# In[25]:


type(b),type(c)


# In[71]:


b[3]=4


# In[31]:


b[3:],b[1:4]


# ## Dictionay {}

# In[72]:


dic={'name1':'경민','학번1':20103,'name2':'경민2','학번2':20104}
dic


# In[33]:


dic.get('name1')


# In[34]:


dic.keys()


# In[35]:


dic.values()


# ## set {}

# In[56]:


lunch={'햄버거','치킨','라면','콜라',10000}
lunch & dinner


# In[206]:


dinner={'피자','족발','라면','콜라',10000}
dinner | lunch


# ## Pandas

# In[207]:


import pandas as pd


# In[209]:


li=[1,2,3]
li


# In[210]:


type(li)


# In[225]:


s1=pd.core.series.Series(li)
s1


# In[226]:


s2=pd.core.series.Series(['일','이','삼'])
s2


# In[224]:


data=dict(num=s1,word=s2)
data


# In[257]:


pd.DataFrame(data)


# In[272]:


pd.DataFrame([['a',100],['b',200],['c',300]])


# In[273]:


data = pd.DataFrame([['a',100],['b',200],['c',300]])


# In[274]:


data.info()


# In[278]:


data.tail(2)


# In[279]:


data.head(2)


# In[283]:


col=['1군','2군']


# In[292]:


pd.DataFrame(([['a',100],['b',200],['c',300]]),columns=col)


# In[324]:


man=[{'Name':'은주','Age':20,'Job':'J1'},{'Name':'소주','Age':21,'Job':'J2'},{'Name':'대주','Age':22,'Job':'J2'},]
pd.DataFrame(man,index=[1,2,3])


# In[327]:


a=[1,2,3]
b=[4,5,6]
df=[a,b]
dd=pd.DataFrame(df,index=[1,2],columns=['A','B','C'])
dd


# In[ ]:




