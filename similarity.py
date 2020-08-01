#!/usr/bin/env python
# coding: utf-8

import math

d1 = "If you fail to plan then you plan to fail"
d2 = "do not fil me or else I will fail you"
d3 = "I always organise well"


# define cosine_similarity to calculate consine cimilarity
def cosine_similarity(vector1, vector2):
    assert (len(vector1) == len(vector2)), " The two vectors do not have the same length"
    #cosine = 0
    cosine = np.inner(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)

    return cosine


def calculate_vocab(d1, d2, d3):
    d1_l = d1.split()
    d2_l = d2.split()
    d3_l = d3.split()
    
    #list to set
    d1_s = set(d1_l)
    d2_s = set(d2_l)
    d3_s = set(d3_l)
    
    voc = d1_s.union(d2_s)
    voc = voc.union(d3_s)
    print(voc)
    
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
    
    #make a vector list for d3
    d3_vec=[]
    for word in voc:
        if word in d3_s:
            d3_vec.append(1)
        else:
            d3_vec.append(0)

    print(d3_vec)
    
    return [d1_vec, d2_vec, d3_vec]


vec = calculate_vocab(d1,d2,d3)
vec1 = vec[0]
vec2 = vec[1]
vec3 = vec[2]


#define function for calculate euclidean similarity 
# def euclidean_similarity(vec1, vec2):
    
#     sum=0
#     for i in range(len(vec1)):
#         sum += (vec1[i]-vec2[i])**2
    
#     result = math.sqrt(sum)
    
#     return result  
    
Euclidean_dist_d1d2 = np.linalg.norm(np.array(vec1)-np.array(vec2))
Euclidean_dist_d1d3 = np.linalg.norm(np.array(vec1)-np.array(vec3))

# #Euclidean similarity between d1 and d2
print(Euclidean_dist_d1d2)
# #Eulidean similarity between d1 and d3
print(Euclidean_dist_d1d3)

#cosine similarity between d1 and d2
print(cosine_similarity(vec1, vec2))
# cosine similarity between d1 and d3
print(cosine_similarity(vec1,vec3))




