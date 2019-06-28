#!/usr/bin/env python
# coding: utf-8

# In[7]:


class demo:
    def test(self):
        print("test() for the class and method")
        return
obj=demo()
obj.test()


# In[3]:


def test():
    print("test() for function")
    return
test()


# In[10]:


class demo1:
    def fact(self,n):
        #return the factorial
        fact=1
        while(n!=0):
            fact=fact*n
            n=n-1
        return fact
p1=demo1()    
p1.fact(5)


# In[17]:


class demo2:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        return
    def add(self,p1,p2):
        return p1+p2
c1=demo2(10,20)        
print(c1.add(100,200))        


# In[34]:


class person(object):
    #constructor
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def isemployee(self):
        return False
    
#derived class
class employee(person):
    def isemployee(self):
        return True
emp=person("ukm")
print(emp.getname(),emp.isemployee())
emp1=employee("uma")
print(emp.getname(),emp1.isemployee())


# In[35]:


lst=[1,2,3,4]
print(lst)


# In[37]:


import numpy as np
lst=[1,2,3,4]
array=np.array(lst)
print(array)


# In[40]:


lst=[1,2,3,4]
array=np.array(lst)
print(array.shape)
print(array.dtype)


# In[41]:


lst=[1,0,2,5,3,6,9,5]
array=np.array(lst)
print(array)


# In[44]:


a1=np.array([(1,2,3),(4,5,6)])
print(a1.shape)
a2=np.array([(1,2),(4,5,6)])
print(a2.shape)


# In[45]:


a1=np.array([(1,2,3),(4,5,6)])
print(a1)
a1.reshape(3,2)


# In[48]:


a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.hstack((a1,a2)))


# In[49]:


a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.vstack((a1,a2)))


# In[50]:


a1=np.random.normal(5,0.5,10)
print(a1)


# In[51]:


np.zeros((2,2))


# In[52]:


np.zeros((2,2),dtype=np.int64)


# In[3]:


import numpy as np
np.ones((4,3),dtype=np.int64)


# In[7]:


A=np.matrix(np.ones((4,4),dtype=np.int64))
print(A)


# In[9]:


A=np.matrix(np.ones((4,4),dtype=np.int64))
np.asarray(A)[2]=5
print(A)


# In[10]:


import numpy as np
np.arange(1,10)


# In[11]:


np.arange(1,100,9)


# In[12]:


np.arange(2,20,2)
np.arange(1,25,2)


# In[20]:


a1=np.array([(1,2,3),(4,5,6)])
print(a1)


# In[16]:


a1=np.array([(1,2,3),(4,5,6)])
print("first row : ",a1[0])


# In[18]:


a1=np.array([(1,2,3),(4,5,6)])
print("second row : ",a1[1])


# In[21]:


a1=np.array([(1,2,3),(4,5,6)])
print("slicing column: ",a1[:,1])


# In[22]:


a1=np.array([(1,2,3),(4,5,6)])
print("slicing last column: ",a1[:,2])


# In[24]:


a1=np.array([(1,2,3),(4,5,6)])
print("row and column",a1[1,:1])


# In[25]:


a1=np.random.normal(5,1,10)
print(a1)
print("min value = ",np.min(a1))
print("max value = ",np.max(a1))
print("mean value = ",np.mean(a1))
print("median value = ",np.median(a1))


# In[7]:


#multiply of 1d arrays
#numpy.dot(x,y)--
import numpy as np
c1=np.array([1,2])
c2=np.array([3,4])
np.dot(c1,c2)


# In[8]:


c1=np.array([(1,2),(3,4)])
c2=np.array([(3,4),(1,2)])
np.dot(c1,c2)


# In[11]:


b1=np.array([(1,5),[6,9]])
b2=np.array([(1,3),(1,6)])
np.matmul(b1,b2)


# In[8]:


import pandas as pd
dict1 ={"name":["ukm","kkm","kum","muk","uma","mishra"],
        "emailid":["ukm@gmail.com","kkm@gmail.com","kum@gmail.com","muk@gmail.com","uma@gmail.com","mishra@gmail.com"],
        "mobilenumber":[879,564,213,546,864,856],
        "address":["hyd","hyd","hyd","hyd","hyd","hyd"]}
b=pd.DataFrame(dict1)
print(b)


# In[7]:


b.index=["01","02","03","04","05","06"]
print(b)

