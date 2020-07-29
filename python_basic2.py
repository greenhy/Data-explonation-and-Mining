#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Variable creation
num_of_students = 150
student_name='name'
student_age = 22
student_gpa = 4.5


# In[2]:


#ypes of the variables
print(type(student_age))
print(type(student_name))
print(type(student_gpa))


# In[4]:


#This is how empty list can be defined
student_names= []
student_ages = []
student_gpas = []


# In[5]:


#define fucntion for add student information in the lists
def student_details(student_name, student_age, student_gpa):
    student_names.append(student_name)# add value in the list
    student_ages.append(student_age)
    student_gpas.append(student_gpa)


# In[6]:


student_details('student1',23,3.7)
student_details('student2',21,3.9)
student_details('student3',20,4.3)


# In[7]:


print(student_names)
print(student_ages)
print(student_gpas)


# In[8]:


#add same info
student_details('student1',23,3.7)


# In[9]:


#list can have duplicate records
print(student_names)
print(student_ages)
print(student_gpas)


# In[10]:


#try to calculate mean -> student_names is categorical variable so this throws an error with type
#using numpy
import numpy as np
np.mean(student_names)


# In[11]:


#calculate mode
from scipy import stats
stats.mode(student_names)


# In[12]:


#This is how an empty set can be defined
student_names= set()
student_ages = set()
student_gpas = set()


# In[13]:


#define fucntion for add student information in the sets
def student_details(student_name, student_age, student_gpa):
    student_names.add(student_name)# add value in the set
    student_ages.add(student_age)
    student_gpas.add(student_gpa)


# In[14]:


student_details('student1',23,3.7)
student_details('student2',21,3.9)
student_details('student3',20,4.3)
student_details('student3',20,4.3)


# In[15]:


#set doesn't allow duplicate entries and the order is not preserved
print(student_names)
print(student_ages)
print(student_gpas)


# In[17]:


# Working with the Boolean representation
sentence = "This is a fairly boring sentence."

#split the sentence
words = sentence.split()

for word in words:
    print(word)


# In[19]:


#manipulating lists and sets

#Working with a list
names=['name1', 'name2', 'name3']
print(names)

names.append('name2')
print(names)

for item in names:
    print(item)

#Working with two lists
another_list = ['name4','name5']

for item in another_list:
    if item in names:
        print(items,'is in the list')
    else:
        print(item,'is not in the list')


# In[20]:


#Working with a set
name_set={'name1','name2'}
print(name_set)

name_set.add('name3')
print(name_set)

name_set.add('name3')
print(name_set)


# In[ ]:




