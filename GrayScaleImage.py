#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


Color_img = plt.imread('E:/Git/Numpy_04476/a.jpg')


# In[6]:


plt.imshow(Color_img)


# In[ ]:





# In[ ]:





# In[42]:


rgb_weights = [0.2989, 0.5870, 0.1140]

grayscale_image = np.dot(Color_img[...,:3], rgb_weights)
plt.imshow(grayscale_image, cmap=plt.get_cmap("gray"))


# In[ ]:




