#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

# In[17]:


x=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(x)):
    for j in range(len(x)):
        if x[i][1]<x[j][1]:
            x[i],x[j]=x[j],x[i]
print(x)

