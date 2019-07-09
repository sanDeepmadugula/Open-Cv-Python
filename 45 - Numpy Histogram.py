#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

def main():
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath = path + "4.2.07.tiff"
    img = cv2.imread(imgpath,0)
    
    plt.subplot(1,2,1)
    plt.imshow(img,cmap='gray')
    plt.title('Image')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1,2,2)
    hist, bins = np.histogram(img.ravel(),256,[0,255]) # 256 no of bins
    plt.xlim([0,255])
    plt.ylim([0,3000])
    plt.plot(hist)
    plt.title('Histogram')
    plt.show()
    
if __name__ == "__main__":
    main()


# In[4]:


# histogram for color images using numpy

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
    R, G, B = cv2.split(img)
    
    
  #  plt.subplot(1,2,1)
  #  plt.imshow(img)
  #  plt.title('Original Image')
  #  plt.xticks([])
  #  plt.yticks([])
    
    plt.subplot(3,1,1)
    hist, bins = np.histogram(R.ravel(),256,[0,255]) # 256 no of bins
    plt.xlim([0,255])
    plt.plot(hist, color='r')
    plt.title(' Red Histogram')
    plt.show()
    
    plt.subplot(3,1,2)
    hist, bins = np.histogram(G.ravel(),256,[0,255]) # 256 no of bins
    plt.xlim([0,255])
    plt.plot(hist,color='g')
    plt.title(' Green Histogram')
    plt.show()
    
    plt.subplot(3,1,3)
    hist, bins = np.histogram(B.ravel(),256,[0,255]) # 256 no of bins
    plt.xlim([0,255])
    plt.plot(hist,color='b')
    plt.title(' Blue Histogram')
    plt.show()
    
if __name__ == "__main__":
    main()


# In[ ]:




