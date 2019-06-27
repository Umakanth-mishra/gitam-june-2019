#!/usr/bin/env python
# coding: utf-8

# In[1]:


##string functions-built in functions
##upper()-returns strings which all characters in upper case
str="umakanth"
print(str.upper())
print(str.lower())


# In[2]:


s="python is easy programming to learn"
s1='python'
print(s.islower())
print(s1.islower())


# In[3]:


s="Application"
s1='UMKANTH'
print(s.isupper())
print(s1.isupper())


# In[4]:


s="5678"
s1="App1889"
print(s.isnumeric())
print(s1.isnumeric())


# In[5]:


s="Application"
s1="App1889"
print(s.isalpha())
print(s1.isalpha())


# In[15]:


s="Python Programming"
s1="Python"
s2=" " 
print(s.istitle())
print(s.isspace())
print(s2.isspace())


# In[19]:


str="python"
print("9 ".join(str))


# In[21]:


print(",".join(["python","programming","easy"]))


# In[22]:


s="python programming is easy to learn"
print(s.split())


# In[23]:


s="python programming is easy to learn"
print(s.split())
print(s.split("a"))


# In[27]:


s="python programming is easy to learn"
lst=list(s)
print(lst)


# In[28]:


s="python programming";
print(s.replace("gra","application"))


# In[30]:


t="python","programming","1989","2019","machine learning","AI"
t1=(1,1,2,3,4)
print(t)
print(t1)


# In[33]:


t="python","programming","1989","2019","machine learning","AI"
print("t[0]=",t[0])
print("t[1]=",t[1])
print("t[-1]=",t[-1])
print("t[1:4]=",t[1:4])
print("t[2:2]=",t[2:-2])


# In[34]:


t="python","programming","1989","2019","machine learning","AI"
print(t)
t[2]=2019
del t[2]


# In[35]:


t="python","programming","1989","2019","machine learning","AI"
t1=(1988,2019,"ML","AI")
t2=t+t1
print(t2)


# In[39]:


t="python","programming","1989","2019","machine learning","AI"
t1=("python")
t2=(5,454,6,2,645,1,0,45)
print(len(t))
print(len(t1))
print(max(t2))
print(min(t2))


# In[50]:


list1=["python","programming","1989","2019","machine learning","AI"]
tuple1=tuple(list1)
print(tuple1)


# In[ ]:





# In[ ]:




