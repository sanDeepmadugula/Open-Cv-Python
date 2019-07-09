#!/usr/bin/env python
# coding: utf-8

# In[9]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath1 = path + "cameraman.tif"
    
    img = cv2.imread(imgpath1, 0)
    
    th = 0
    max_val = 255
    
    ret,binary_inv = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # calculate kernel
    # k = np.ones((5,5), np.uint8)
        
    # antoher way of kernel
    
    #k = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
   # k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    k = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
    
    erosion = cv2.erode(binary_inv,k, iterations = 5) # 1st type of morphological opertaion
    
    dilation = cv2.dilate(binary_inv,k, iterations = 3) # 2nd type of morphological operation
    
    gradient = cv2.morphologyEx(binary_inv, cv2.MORPH_GRADIENT, k) # gradient is the diff b/w erosion and dilation
    
    
    
    print(k)
    
    output = [img, binary_inv, erosion,dilation,gradient]
    
    titles = ['Original', 'Binary_inv', 'Erosion','Dialation','Gradient']
    
    for i in range(5):
        plt.subplot(3,2,i+1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()
    


# In[11]:


# Morphological operation on grey scale image

import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath1 = path + "cameraman.tif"
    
    img = cv2.imread(imgpath1, 0)
    
   # th = 0
   # max_val = 255
    
    #ret,binary_inv = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # calculate kernel
    # k = np.ones((5,5), np.uint8)
        
    # antoher way of kernel
    
    #k = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
   # k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    k = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
    
    erosion = cv2.erode(img,k, iterations = 5) # 1st type of morphological opertaion
    
    dilation = cv2.dilate(img,k, iterations = 3) # 2nd type of morphological operation
    
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k) # gradient is the diff b/w erosion and dilation
    
    
    
    print(k)
    
    output = [img, erosion,dilation,gradient]
    
    titles = ['Original', 'Erosion','Dialation','Gradient']
    
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()
    


# In[13]:


# For color images

# Morphological operation on grey scale image

import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath1 = path + "4.2.05.tiff"
    
    img = cv2.imread(imgpath1, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
   # th = 0
   # max_val = 255
    
    #ret,binary_inv = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # calculate kernel
    # k = np.ones((5,5), np.uint8)
        
    # antoher way of kernel
    
    #k = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
   # k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    k = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
    
    erosion = cv2.erode(img,k, iterations = 5) # 1st type of morphological opertaion
    
    dilation = cv2.dilate(img,k, iterations = 3) # 2nd type of morphological operation
    
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k) # gradient is the diff b/w erosion and dilation
    
    
    
    print(k)
    
    output = [img, erosion,dilation,gradient]
    
    titles = ['Original', 'Erosion','Dialation','Gradient']
    
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()
    


# In[ ]:




