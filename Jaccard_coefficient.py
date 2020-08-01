#!/usr/bin/env python
# coding: utf-8

#calculate the vocabulary

d1 = "If you fail to plan then you plan to fail"
d2 = "do not fail me or else I will fail you"

#split d1 and d2
d1_l = d1.split()
d2_l = d2.split()


#list to set
d1_s = set(d1_l)
d2_s = set(d2_l)


print(d1_l)
print(d2_l)
print('\n')
print(d1_s)
print(d2_s)


#combine d1_s and d2_s to make a vocabulary 
voc = d1_s.union(d2_s)
print(voc)


#make a vector list for d1
d1_vec=[]
for word in voc:
    if word in d1_s:
        d1_vec.append(1)
    else:
        d1_vec.append(0)

print(d1_vec)


#make a vector list for d2
d2_vec=[]
for word in voc:
    if word in d2_s:
        d2_vec.append(1)
    else:
        d2_vec.append(0)

print(d2_vec)

#calculate the Jaccard coefficient between d1 and d2
# JC = |d1 AND d2| / | d1 OR d2|

#calculate set union
s_union = len(voc)

#calculate set intersection
s_and=0
for i in range(s_union):
    if d1_vec[i] == d2_vec[i]:
        s_and+=1
            
print(s_union)
print(s_and)

#| d1 OR d2|
s_or=0
for i in range(s_union):
    if d1_vec[i] or d2_vec[i] == 1:
        s_or += 1
 
#divide s_union and s_inter
result = s_and/s_or

print(result)
