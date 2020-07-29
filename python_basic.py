#!/usr/bin/env python
# coding: utf-8

#This code helps to print something
print('I am now printing hello world!')


#Variable creation
num_of_students = 150
student_name='name'
student_age = 22
student_gpa = 4.5


#print variables
print('Student name is:', student_name)
print('Student age is:', student_age)
print('Student gpa is:', student_gpa)


#function
def student_details(student_name, student_age, student_gpa):
    print('Student name is:', student_name)
    print('Student age is:', student_age)
    print('Student gpa is:', student_gpa)


student_details('name2',23,4.0)


#squares any input and sotres it in variable 'num'
def sqr(num):
    num = num*num
    return num
print(sqr(2))


#defind a function that can do factorial
def factorial(num):
    result=1
    for i in range(1,num+1):
        result*=i
    return result


print(factorial(5))
