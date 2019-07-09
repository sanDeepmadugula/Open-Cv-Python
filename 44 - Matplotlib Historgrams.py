#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

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
    plt.hist(img.ravel(),256,[0,255]) # 256 no of bins
    plt.title('Histogram')
    plt.xlim(xmin=0, xmax=256)
    plt.show()
    
if __name__ == "__main__":
    main()


# In[10]:


# for colored image historgram

import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def main():
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath = path + "4.2.07.tiff"
    img = cv2.imread(imgpath,1)
    
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    R, G, B = cv2.split(img)
    
    #plt.subplot(1,4,1)
    #plt.imshow(img,cmap='gray')
    #plt.title('Image')
    #plt.xticks([])
    #plt.yticks([])
    
    plt.subplot(3,1,1)
    plt.hist(R.ravel(),256,[0,255]) # 256 no of bins
    plt.title('Red Channel Histogram')
    plt.xlim(xmin=0, xmax=256)
    plt.show()
    
    plt.subplot(3,1,2)
    plt.hist(G.ravel(),256,[0,255]) # 256 no of bins
    plt.title('Green Channel Histogram')
    plt.xlim(xmin=0, xmax=256)
    plt.show()
    
    plt.subplot(3,1,3)
    plt.hist(B.ravel(),256,[0,255]) # 256 no of bins
    plt.title('Blue Channel Histogram')
    plt.xlim(xmin=0, xmax=256)
    plt.show()
    
if __name__ == "__main__":
    main()


# In[ ]:




