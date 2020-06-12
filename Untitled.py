#!/usr/bin/env python
# coding: utf-8

# In[34]:


import turtle as t
t.shape('turtle')
t.fd(200)
t.fd(200)
t.left(90)
t.fd(200)
t.left(90)
t.fd(200)
t.fd(200)
t.left(90)
t.fd(200)
t.exitonclick()


# In[37]:


import turtle as t 
t.shape('turtle')
t.fd(200)
t.left(120)
t.fd(200)
t.left(120)
t.fd(200)
t.left(120)
t.exitonclick()


# In[39]:


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


# In[45]:


import turtle as t 
color('blue', 'yellow')
begin_fill()
t.shape('turtle')
t.fd(200)
t.left(120)
t.fd(200)
t.left(120)
t.fd(200)
t.left(120)
end_fill()
t.exitonclick()


# In[185]:


import turtle as t 
t.shape('turtle')
t.left(90)
t.fd(200)
t.left(170)
t.fd(450)
t.left(150)
t.fd(400)
t.left(130)
t.fd(330)
t.left(130)
t.fd(400)
t.left(153.5)
t.fd(445)


t.exitonclick()


# In[57]:


import turtle as t 
t.shape('turtle')
t.color('blue', 'yellow')
t.begin_fill()

n=int(input('몇각형?'))
for i in range(n):
    for i in range(n):
        t.fd(100)
        t.left(360/n)
        t.fd(30)
    t.right(180/n)
    
t.end_fill()
t.exitonclick()

