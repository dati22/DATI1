#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=[30,29,41,64,75,44,56,16]
print(a[1:7:2])


# In[4]:


a=[30,29,41,64,75,44,56,16]
b=(30,29,41,64,75,44,56,16)
print(type(a))
print(type(b))


# In[7]:


a={'lesson'}
print(set(a))


# In[12]:


a=set()
a.add("football")
print(a)
print(type(a))


# In[16]:


a={1,3,2}
b={2,3,3}
d=a.difference(b)
print(d)
print(type(d))


# In[20]:


#задание №1
a=["abc","xyz","aba",1221]
print(a[3:])


# In[31]:


#задание №2
a=["green","white","black"]
b=["red","pink","yellow"]
print(a+b)


# In[40]:


for i in range(10,5,-1):
    print(i)


# In[41]:


sum=0
for i in range(0,21):
    sum=sum+i
print(sum)


# In[43]:


a=[39,31,46,63,44,15,25,74,44,352,50,54]
for i in a:
    print(i*2)


# In[44]:


a=['белый','красный','желтый','зеленый','черный']
for i in a:
    print("цвет: " + i)


# In[49]:


a=0
while (a<10):
    a=a+3
    print(a)


# In[51]:


a=int(input())
for i in range(0,a+1):
    print(i)


# In[54]:


a=int(input())
c=int(input())
for i in range(a,c +1):
    print(i)


# In[62]:


a=int(input())
c=int(input())
if (a<c):
    for i in range(a,c):
        print(i)
else:
    for i in range(a,c -1):
        print(i)


# In[63]:


sum=0
a=int(input())
for i in range(0,a+1):
    sum=sum+i
print(sum)


# In[ ]:




