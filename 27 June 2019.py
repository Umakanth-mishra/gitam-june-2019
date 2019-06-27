#!/usr/bin/env python
# coding: utf-8

# In[5]:


#function to create a file and write some data
def createfile(filename):
    f=open(filename,"w")
    for i in range(10):
        f.write("this is %d line\n" % i)
    print("file is created successfully and data is written")    
    f.close()    
    return
createfile("file1.txt")


# In[6]:


#function for reading the file data
def readfile(filename):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        print(x)
    f.close()    
    return

readfile("file1.txt")


# In[10]:


#data to append
#function to append the data to existing file
def appenddate(filename):
    f=open(filename,'a')
    f.write("newline 1\n")
    f.write("newline")
    return
appenddate('file.txt')






# In[13]:


def dataanalysiswordcount(filename,word):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=x.split()
    count=lst.count(word)   
    return count
print(dataanalysiswordcount("file.txt","rest"))


# In[14]:


def countcharacter(filename):
    f=open(filename,'r')
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    return len(lst)    
print(countcharacter("file.txt"))


# In[29]:


def uppercasecount(filename):
    cntlower=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.islower():
            cntlower += 1
    return cntlower
uppercasecount("file1.txt")


# In[32]:


def countline(filename):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=x.split("\n")
    return len(lst)    

countline("file1.txt")


# In[38]:


import re
txt = "abcde"
x = re.search("[a-z]", txt)
if x:
    print (True)


# In[44]:


import re
def validaterollnumber(number):
    number=str(number)
    pattern="^[1][5][2][U][1][A][0][1-9][0-6][0-9]$"
    if re.match(pattern,number):
        return True
    return False
print(validaterollnumber("152U1A0555"))
print(validaterollnumber("152U1A0485"))


# In[46]:


import re
def phonenumbervalidate(phone):
    pattern="^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|[+][9][1][6-9][0-9]{9}$"
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phonenumbervalidate("9185291497"))
print(phonenumbervalidate('+917895461230'))
                           


# In[49]:


def validateemailid(email):
    pattern ="^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$"
    if re.match(pattern,email):
        return True
    return False
print(validateemailid("umakanth@gmail.com"))
print(validateemailid("$uma.1234@gmail.com"))


# In[50]:


import re
def validatepassword(s):
    pattern ="^[a-zA-z0-9!@#$]{6,15}$"
    if re.match(pattern,s):
        return True
    return False
print(validatepassword("umakanth123@21#m"))
print(validatepassword("umakanth123@21#m11112222"))


# In[ ]:




