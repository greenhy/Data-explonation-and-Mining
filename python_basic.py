#!/usr/bin/env python
# coding: utf-8

# In[2]:


#This code helps to print something
print('I am now printing hello world!')


# In[4]:


#Variable creation
num_of_students = 150
student_name='name'
student_age = 22
student_gpa = 4.5


# In[5]:


#print variables
print('Student name is:', student_name)
print('Student age is:', student_age)
print('Student gpa is:', student_gpa)


# In[7]:


#function
def student_details(student_name, student_age, student_gpa):
    print('Student name is:', student_name)
    print('Student age is:', student_age)
    print('Student gpa is:', student_gpa)


# In[9]:


student_details('name2',23,4.0)


# In[10]:


#squares any input and sotres it in variable 'num'
def sqr(num):
    num = num*num
    return num
print(sqr(2))


# In[12]:


#defind a function that can do factorial
def factorial(num):
    result=1
    for i in range(1,num+1):
        result*=i
    return result


# In[13]:


print(factorial(5))


# In[ ]:




