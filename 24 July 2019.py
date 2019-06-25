#!/usr/bin/env python
# coding: utf-8

# In[7]:


###binary search 
def binarysearch(a,lindex,rindex,taritem):
    while lindex<=rindex:
        mindex=lindex+(rindex-lindex)//2
        if(a[mindex]==taritem):
            return mindex
        if(a[mindex]>taritem):
            rindex=mindex-1
        else:
            lindex=mindex+1
    return -1
list1=[1,4,9,15,25,45,57,88,98]
res=binarysearch(list1,0,8,57)
if res!=-1:
    print("item is found")
else:
    print("item is not found")


# In[11]:


###def bubblesort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                
    for i in range(len(a)):
        print(a[i],end=" ")
        
list1=[19,1,25,6,18,3]
bubblesort(list1)


# In[12]:


###strings in python
str="applicaiton"
print(str)
str1='application'
print(str1)
str2="""application test
working 
completed
list
strings
python"""
print(str2)


# In[17]:


str="application"
print(str)
print("str[0]= ",str[0])
print("str[1]= ",str[1])
print("str[-1]= ",str[-1])
print("str[-3]= ",str[-3])
print("str[1:5]= ",str[1:5])
print("str[:5]= ",str[:5])
print("str[5:-2]= ",str[5:-2])
print("str[::-1]= ",str[::-1])


# In[18]:


def ispalindrome(s):
    if(s==s[::-1]):
        return True
    else:
        return False
    
print(ispalindrome("python"))
print(ispalindrome("python"))            


# In[21]:


def countuppercase(str):
    cnt=0
    return cnt
print(countuppercase("application"))
print(countuppercase("test"))


# In[31]:


def length(n):
    return len(n)

print(length("GitamUniversity"))


# In[34]:


def countuppercase(str):
    cnt=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=65 and ord(lst[x])<=90:
            cnt=cnt+1
    return cnt

print(countuppercase("AppLication"))
print(countuppercase("TeST"))


# In[40]:


def printdigits(str):
    lst=list(str)
    for x in range(len(lst)):
         if ord(lst[x])>=48 and ord(lst[x])<=57:
            print(lst[x],end=" ")                                               
    
print(printdigits("Application1889")) 


# In[ ]:





# In[ ]:




