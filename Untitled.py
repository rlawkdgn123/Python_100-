#!/usr/bin/env python
# coding: utf-8

# In[9]:


a=[[1,1,0,1,0],
  [1,0,1,0]]
tot, totsu = 0, 0
for i in a:
    for j in i:
        tot += j
    totsu = totsu + len(i)
print(totsu,tot)


# In[12]:


i,hap =1,0
while i<=6:
    hap+=i
    i+=2
print(f"i={i},hap={hap}")


# In[38]:


str='Sinagong'
n=len(str)
st=list()
for k in range(n):
    st.append(str[k])
for k in range(n-1,-1,-1):
    print(st[k],end='')


# In[39]:


hap = 0
for i in range(1,11):
    hap += i
print(i,hap)


# In[41]:


hap1=10+10%4-10%9
hap2=10*10%4-10%9+5
print("%d, %d"%(hap1,hap2))


# In[50]:


a,b=1,1
y=a+b
n=int(input())
for k in range(3,n+1):
    c=a+b
    y=y+c
    a=b
    b=c
print(y)


# In[7]:


a= "what's this?"
print("%-10.4s" % a)
print("%10.4s" % a)


# In[2]:


a=sum=0
while a < 10:
    a+=1
    if a%2==1:
        continue
    sum+=a
print(sum)


# In[3]:


a,b=2,3
c=a&b
print(c)


# In[4]:


a,c=32,-3
b=a<<2
a>>=3
c=c<<2
print(a,b,c)


# In[6]:


def change():
    global i,j
    temp = i
    i = j
    j = temp
i,j=10,20
change()
print(f"i={i},j={j}")

