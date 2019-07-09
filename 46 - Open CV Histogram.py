#!/usr/bin/env python
# coding: utf-8

# In[3]:


# cv2.calcHist()

import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

def main():
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath = path + "4.2.07.tiff"
    img = cv2.imread(imgpath,1)
    
    # separating the color channel
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    red_hist = cv2.calcHist([img],[0],None,[256],[0,255]) #[0] - red channel, None-no mast present,
    green_hist = cv2.calcHist([img],[1],None,[256],[0,255]) # [1] - blue
    blue_hist = cv2.calcHist([img],[2],None,[256],[0,255]) # [2] - green
    
    
    plt.subplot(3,1,1)
    plt.xlim([0,255])
    plt.plot(red_hist, color='r')
    plt.title(' Red Histogram')

    
    plt.subplot(3,1,2)
    plt.xlim([0,255])
    plt.plot(green_hist,color='g')
    plt.title(' Green Histogram')
    
    
    plt.subplot(3,1,3)
    plt.xlim([0,255])
    plt.plot(blue_hist,color='b')
    plt.title(' Blue Histogram')
    
    plt.show()
    
if __name__ == "__main__":
    main()


# In[ ]:




