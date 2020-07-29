#!/usr/bin/env python
# coding: utf-8

#Variable creation
num_of_students = 150
student_name='name'
student_age = 22
student_gpa = 4.5


#types of the variables
print(type(student_age))
print(type(student_name))
print(type(student_gpa))


#This is how empty list can be defined
student_names= []
student_ages = []
student_gpas = []


#define fucntion for add student information in the lists
def student_details(student_name, student_age, student_gpa):
    student_names.append(student_name)# add value in the list
    student_ages.append(student_age)
    student_gpas.append(student_gpa)


student_details('student1',23,3.7)
student_details('student2',21,3.9)
student_details('student3',20,4.3)


print(student_names)
print(student_ages)
print(student_gpas)


#add same info
student_details('student1',23,3.7)


#list can have duplicate records
print(student_names)
print(student_ages)
print(student_gpas)


#try to calculate mean -> student_names is categorical variable so this throws an error with type
#using numpy
import numpy as np
np.mean(student_names)


#calculate mode
from scipy import stats
stats.mode(student_names)


#This is how an empty set can be defined
student_names= set()
student_ages = set()
student_gpas = set()


#define fucntion for add student information in the sets
def student_details(student_name, student_age, student_gpa):
    student_names.add(student_name)# add value in the set
    student_ages.add(student_age)
    student_gpas.add(student_gpa)

    
student_details('student1',23,3.7)
student_details('student2',21,3.9)
student_details('student3',20,4.3)
student_details('student3',20,4.3)


#set doesn't allow duplicate entries and the order is not preserved
print(student_names)
print(student_ages)
print(student_gpas)


# Working with the Boolean representation
sentence = "This is a fairly boring sentence."

#split the sentence
words = sentence.split()

for word in words:
    print(word)


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


#Working with a set
name_set={'name1','name2'}
print(name_set)

name_set.add('name3')
print(name_set)

name_set.add('name3')
print(name_set)
