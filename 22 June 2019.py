#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
os.getcwd()


# In[9]:


x=10
if(x<15):
 print("the number is less than 15")    


# In[12]:


x=10
if(x>15):
    print("hello good morning"); 
else:
    print("hello good afternoon");


# In[13]:


x=10;
y=20;
if(x<y):
    print("y is greatest")
else:
    print("x is greatest")


# In[1]:


x = int(input("enter x value"))
y = int(input("enter y value"))
if(x==y):
    print(x*x)
else:    
    print(x*y)


# In[2]:


x=10;
if(x<0):
    print("it's negative number ");
elif(x>0):
    print("it's positive number");
elif(x==0):
    print("it's zero");


# In[5]:


n=0
while(n<=10):
    print(n)
    n=n+1
    


# In[2]:


x=1
y=100
sum=0
while(x!=y):
    if(x%2==0):
        sum=sum+x
    x=x+1 
    
print(sum) 

            


# In[3]:


x=int(input("enter x value"))
while(x!=0):
    r=x%10
    print(r)
    x=x//10


# In[13]:


n=145
rv=0
while(n>0):
    dig=n%10
    rv=rv*10+dig
    n=n//10
print("reverse of number", rv)


# In[1]:


x=int(input("enter the number"))
sum=0
while(x!=0):
    rev=x%10
    if(rev%2==0):
        sum=sum+rev
    x=x//10
print(sum)


# In[5]:


x=int(input("enter the number"))
rev=0
while(x!=0):
    rev=x%10
    
    if(rev==0):
        print("zero")
    elif(rev==1):
        print("one")
    elif("rev==2"):
        print("two")
    elif(rev==3):
        print("three")
    elif("rev==4"):
        print("four")
    x=x//10
    


# In[8]:


n=int(input("enter n value"))
l1=int(input("enter n1 value"))
l2=int(input("enter n2 value"))
count=0
while(l1!=l2):
    temp=l1
    r=11%10
    if(r==n):
        count=count+1
    l1=l1/10
    l1=b-temp        
    l1=l1+1
print(count)


# In[12]:


def printnnaturalnumbers(n):
    cnt=1
    while(cnt<=n):
        print(cnt,end=" ")
        cnt=cnt+1
        
printnnaturalnumbers(9)     
printnnaturalnumbers(30)
        


# In[18]:


def findFact(n):
    fact=1;
    while(n!=0):
        fact=fact*n;
        n=n-1
    return fact; 


print( findFact(5))


# In[25]:


def countpalindrome(n1,n2):
    cnt=0
  while(n1!=n2):
    sum=0
    buffer=n1
   while n1!=0:
        r=n1%10;
        sum=(sum*10)+r;
        n1=n1//10
    if buffer==sum:
        cnt=cnt+1
        n1=buffer:
        n1=n1+1;
    return cnt;
print(countpalindrome(10,30))
print(countpalindrome(1,10000000))
    
    


# In[ ]:




