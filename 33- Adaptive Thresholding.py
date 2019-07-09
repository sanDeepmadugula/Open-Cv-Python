#!/usr/bin/env python
# coding: utf-8

# In[9]:


# to calculate the threshold not by manual

import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath1 = path + "5.1.12.tiff"
    #imgpath1 = path + "4.2.07.tiff" # for colored image
    img = cv2.imread(imgpath1, 0)
    
    block_size = 513 # neighbourhood of pixels, we can play with it
    constant = 2
    th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,block_size,constant)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,block_size,constant)
    
    # list of outputs
    output = [img,th1,th2]
    titles = ['Original','Mean Adaptive','Gaussian Adaptive']
    
    for i in range(3):
        plt.subplot(1,3,i+1)
        plt.imshow(output[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    
   
    plt.show()
    
if __name__ == '__main__':
    main()


# In[ ]:




