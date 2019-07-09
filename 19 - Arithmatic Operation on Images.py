#!/usr/bin/env python
# coding: utf-8

# In[11]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

imgpath1 = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.01.tiff"
imgpath2 = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.07.tiff"

# imgpath1 = path + "4.2.01.tiff"
# imgpath2 = path + "4.2.07.tiff"

img1 = cv2.imread(imgpath1,1)
img2 = cv2.imread(imgpath2,1)



img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

add = img1 + 5

sub1 = img1 - img2
sub2 = img2 - img1

titles = ['Liquid Drop', 'Veg', 'Addition', 'img1 - img2', 'img2 - img1']
images = [img1, img2, add, sub1,sub2]


for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks()
    plt.yticks()
    
plt.show()


# In[15]:


# multipication and division

import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

imgpath1 = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.01.tiff"
imgpath2 = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.07.tiff"

# imgpath1 = path + "4.2.01.tiff"
# imgpath2 = path + "4.2.07.tiff"

img1 = cv2.imread(imgpath1,1)
img2 = cv2.imread(imgpath2,1)



img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

mult = img1 * 2

div = img1/img2


titles = ['Liquid Drop', 'Veg', 'Multipication','Division']
images = [img1, img2, mult, div]


for i in range(4):
    plt.subplot(1,4,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks()
    plt.yticks()
    
plt.show()


# In[ ]:




