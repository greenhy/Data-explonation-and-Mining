#!/usr/bin/env python
# coding: utf-8

# In[13]:


import math

d1 = "If you fail to plan then you plan to fail"
d2 = "do not fil me or else I will fail you"
d3 = "I always organise well"


# In[36]:


# define cosine_similarity to calculate consine cimilarity
def cosine_similarity(vec1, vec2):
#     assert (len(vec1) == len(vec2)), " The two vectors do not have the same length"
#     cosine = 0
    
    mol=0
    r1=0
    r2=0
    
    for i in range(len(vec1)):
        mol += (vec1[i]*vec2[i])
    
    
    
    for i in range(len(vec1)):
        r1 += vec1[i]**2
    for i in range(len(vec2)):
        r2 += vec2[i]**2
    
    r1 = math.sqrt(r1)
    r2 = math.sqrt(r2)
    
    den = r1*r2
    
    cosine = mol/den
    
    
    return cosine


# In[4]:


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
        if word in d1:
            d1_vec.append(1)
        else:
            d1_vec.append(0)

    print(d1_vec)
    
    #make a vector list for d2
    d2_vec=[]
    for word in voc:
        if word in d2:
            d2_vec.append(1)
        else:
            d2_vec.append(0)

    print(d2_vec)
    
    #make a vector list for d3
    d3_vec=[]
    for word in voc:
        if word in d3:
            d3_vec.append(1)
        else:
            d3_vec.append(0)

    print(d3_vec)
    
    return [d1_vec, d2_vec, d3_vec]


# In[10]:


vec = calculate_vocab(d1,d2,d3)
vec1 = vec[0]
vec2 = vec[1]
vec3 = vec[2]


# In[15]:


#define function for calculate euclidean similarity
def euclidean_similarity(vec1, vec2):
    
    sum=0
    for i in range(len(vec1)):
        sum += (vec1[i]-vec2[i])**2
    
    result = math.sqrt(sum)
    
    return result  
    


# In[16]:


#Euclidean similarity between d1 and d2
print(euclidean_similarity(vec1, vec2))
#Eulidean similarity between d1 and d3
print(euclidean_similarity(vec1, vec3))


# In[37]:


#cosine similarity between d1 and d2
print(cosine_similarity(vec1, vec2))
# cosine similarity between d1 and d3
# print(cosine_similarity(vec1,vec3))


# In[ ]:




