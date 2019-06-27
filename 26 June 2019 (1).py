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


# In[3]:


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


# In[2]:


list=["python","programming","1989","2019","machine learning","AI"]
print(list)
tuple1=tuple(list)
print(tuple1)


# In[55]:


user1={'name':'ukm','age':'19','EmailId':'ukm@gmail.com','mobile no.':'9325631234'}
print("user1[name]=",user1["name"])
print("user1[EmailId]=",user1["EmailId"])
print("user1[age]=",user1["age"])
print("user1[mobile no.]=",user1["mobile no."])


# In[59]:


#updating of data
user1={'name':'ukm','age':'19','EmailId':'ukm@gmail.com','mobile no.':'9325631234'}      
print(user1["age"])
user1["age"]=35
print(user1['age'])
user1["address"]="hyderabad"
print(user1)

del user1["age"]
# print(user1["age"])
# user1.clear()
user1.clear()
user1


# In[4]:


##methods in dictionary
user1={'name':'ukm','age':'19','EmailId':'ukm@gmail.com','mobile no.':'9325631234'}      
print(user1)
user1
user1["address"]='hyderabad'
print(len(user1))
user1


# In[5]:


user1={'name':'ukm','age':'19','EmailId':'ukm@gmail.com','mobile no.':'9325631234'}      
user2=user1.copy()
user2


# In[6]:


user1={'name':'ukm','age':'19','EmailId':'ukm@gmail.com','mobile no.':'9325631234'}      
user2=user1.copy()
print(user1.values())
print(user2.values())


# In[7]:


user1={'name':'ukm','age':'19','EmailId':'ukm@gmail.com','mobile no.':'9325631234'}      
print(user1.items())


# In[15]:


lst=['python','programming']
print("%s %s"%(lst[0],lst[1]))




# In[17]:


lst=['python','programming']
print("{0} {1}".format(lst[0],lst[1]))


# In[30]:


#contact applications
contacts={}
def addcontact(name,phone):
    #verify that the contact doesnot already exists
    if name not in contacts:
        contacts[name]=phone
        print("contact %s is added" % name)
    else:
        print("contact %s already exists" % name)
        
    return    
addcontact("ukm",879234612)   
addcontact("umk",568759869)
addcontact("ukm",987234957)

    


# In[32]:


#search for a particular contact from contact list
def searchcontact(name):
    if name in contacts:
        print(name, " : " , contacts[name])
    else:
        print("%s does not exists" % name)
    return
searchcontact("ukm")
searchcontact("kkm")
searchcontact("kum")
searchcontact("uma")
searchcontact("kanth")


# In[33]:


#new contacts is given as a dictionary
print(contacts)


# In[35]:


#new contacts is given as a dictionary
#merge new contact with existing contacts list
def importcontacts(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()),"contacts added successfully")
    return
newcontacts={"dinesh":9643527657,"ajay":9832541276}
importcontacts(newcontacts)
    


# In[36]:


print(contacts)


# In[39]:


#delete a contact from contact list
def deletecontact(name):
    if name in contacts:
        del contacts[name]
        print(name," : is deleted from the contacts")
    else:
        print(name," is not exits in the contact")
    return
deletecontact("harshith")
deletecontact("umakanth")


# In[40]:


print(contacts)


# In[44]:


def updatecontact(name,phone):
    if name in contacts:
        contacts[name]=phone
        print(name," : updated with new phone number")
    else:
            print(name,"not exists in the contacts")
    return
updatecontact("ukm",7854437667)  
updatecontact("umk",6743287942)


# In[45]:


print(contacts)


# In[46]:


lst=[1,2,3,4]
print("value at : {0} value at : {1}".format(lst[0],lst[1]))
print("value at : {0} value at : {1}".format(lst[2],lst[3]))


# In[4]:


from math import floor as f1
f1(123.456)


# In[53]:


from math import factorial as fact 
fact(5)


# In[54]:


import math 
math.factorial(5)


# In[3]:


# generate the random numbers between two limits
import random
def generaterandomnumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end=" ")
    return
generaterandomnumbers(10,12,120)


# In[ ]:




