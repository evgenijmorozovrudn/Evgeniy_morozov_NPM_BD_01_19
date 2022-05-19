#!/usr/bin/env python
# coding: utf-8

# In[7]:


matrix =[
         [1, 2, 3],
         [5, 9,16],
         [24, 90, 3]
]
def swap_rows (matrix, i, j):
    matrix[i], matrix [j] = matrix [j], matrix [i]
    return matrix
print (swap_rows (matrix, 1, 0))


# In[ ]:




