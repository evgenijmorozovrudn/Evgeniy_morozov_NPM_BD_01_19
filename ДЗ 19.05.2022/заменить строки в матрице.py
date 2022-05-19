#!/usr/bin/env python
# coding: utf-8

# In[8]:


matrix =[
         [1, 2, 3],
         [5, 9, 16],
         [24, 90, 3]
]
def find_nearest_element (matrix, z):
    dif = abs (matrix [0][0] - z)
    index = [0, 0]
    for i, j in enumerate (matrix):
        for x, y in enumerate (j):
            temp_dif = abs (y - z)
            if temp_dif < dif:
                dif = temp_dif
                index = (i, x)
    return index
print (find_nearest_element (matrix, 3))


# In[ ]:




