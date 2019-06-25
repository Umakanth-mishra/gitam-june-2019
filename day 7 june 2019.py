#!/usr/bin/env python
# coding: utf-8

# In[13]:


def printeven(n):
    print(n) 
    cnt=0
    sum=0
    while(cnt!=n):
        if(cnt%2==0):
            sum=sum+cnt
        cnt=cnt+1
    return sum;
        
print(printeven(20))


# In[12]:


def factorslist(n):
    i=1
    while(i!=n):
        if(n%i==0):
            print(i,end=" ")
        i=i+1
    
factorslist(12)


# In[16]:


for i in range(10):
    print(i)


# In[20]:


list1=[1,2,3,4,5,6,7]
for x in list1:
    print(x,end=" ")
print()  
print(list1[4])
print(list1[3:6])
print(list1[0:3])
print(list1[:3])
print(list1[:7])
print(list1[1:-1])
print(list1[2:-2])
print(list1[::2])
print(list1[::3])
print(list1[::-2])
print(list1[-1])


# In[28]:


list1=["ukm","kkm",2]
list2=[3,4,5,6]
list1[1]="gitam" 
print(list1)
del list1[2]
print(list1)

print(list1+list2)
print(len(list1))
print(len(list2))
list1.append(15)
list1.append(1)
list1.append(1)
list1.append(1)
print(list1)
print(list1.count(1))


# In[39]:


list1=["gitam","python",1,5,"python","python"]
print(list1)
list1.index('python')
list1.index(1)
print(list1)
list1.insert(4,2020)
print(list1)
list1.remove("python")
print(list1)
list1.reverse()
print(list1)


# In[40]:


list1=["gitam","python",1,5,"python","python"]
print(list1)
list1.index('python')
print(list1)


# In[9]:


def linearsearch(a,taritem):
    flag=0;
    for i in range(len(a)):
        if a[i]==taritem:
            flag=1;
            break 
    if(flag!=0):
         print("target item is found")
    else:
         print("target item is not found")
            
a=[16,2,12,6,9,7,1]
linearsearch(a,6)
linearsearch(a,12)


# In[2]:


def lsduplicate(a,taritem):
    flag=0
    for i in range(len(a)):
        if(a[i]==taritem):
            flag=flag+1
    print(flag)
    
a=[9,1,6,1,5,9,15,15]
lsduplicate(a,9)


# In[16]:


def lexample(a,taritem):
    
    for i in range(len(a)):
        if(a[i]==taritem):
            print(i,end=" ")
a=[1,2,3,4,5,6,3]
lexample(a,3)
    


# In[28]:


def linearexample2(a,taritem):
    for i in range(len(a)):
        if a[i]==taritem:
            j=0
            while j!=i:
                print("!",end=" ")
                j=j+1
        
            print(end=" ")


            
a=[1,5,9,6,5,15,12,5]
linearexample2(a,5)
                


# In[30]:


def mul(a):
    sum=0
    for i in range(len(a)):
        if(a[i]%3==0 and a[i]%5==0):
            sum=sum+a[i]
        return sum
a=[30,12,2,9,18,36,20,45]
print(mul(a))


# In[32]:


def linearformattedoutput(a):
    for i in range(len(a)):
        if(i==0 or i==len(a)-1):
            print(a[i],end=" ")
        elif(a[i-1]%2==0 and a[i+1]%2==0):
            print(a[i],end=" ")
            
a=[1,6,9,4,16,19,22]
linearformattedoutput(a)


# In[33]:


def numbertolistconversion(n):
    list=[]
    while(n!=0):
        r=n%10
        list.append(r)
        n=n//10
    list.reverse()
    print(list)
    
n=int(input("enter the number"))
numbertolistconversion()


# In[ ]:




