#!/usr/bin/env python
# coding: utf-8

# In[9]:


# using laplace operator

import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath = path + "5.1.11.tiff"
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    edges = cv2.Laplacian(img, -1,ksize=9,scale=1,delta=0,
                         borderType=cv2.BORDER_DEFAULT) #-1 - depth, ksize-kernel size
    
    # we can play with ksize and it must be odd, by putting even no it will through an error
    # ksize must be upto 31 only
    output = [img,edges]
    titles = ['Original', 'Edges']
    
    for i in range(2):
        plt.subplot(1,2,i+1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
if __name__ == "__main__":
    main()


# In[14]:


# using sobel operator

import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath = path + "5.1.11.tiff"
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    edgesx = cv2.Sobel(img, -1, dx=2, dy=0 , ksize=11,
                         scale=1, delta=0, borderType = cv2.BORDER_DEFAULT) # we can set with our convinience dx,dy
    
    edgesy = cv2.Sobel(img, -1, dx=0, dy=2, ksize=11,
                         scale=1, delta=0, borderType = cv2.BORDER_DEFAULT)
    
    edges = edgesx + edgesy
    
    # we can play with ksize and it must be odd, by putting even no it will through an error
    # ksize must be upto 31 only
    output = [img,edgesx,edgesy,edges]
    titles = ['Original', 'dx=1 dy=0(vertical edges)' , 'dx=0 dy=1(horizontal edges)', 'Edges']
    
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
if __name__ == "__main__":
    main()


# In[17]:


# using scharr operator

import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath = path + "5.1.11.tiff"
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    edgesx = cv2.Scharr(img, -1, dx=1, dy=0,
                         scale=1, delta=0, borderType = cv2.BORDER_DEFAULT) # we can set with our convinience dx,dy
    
    edgesy = cv2.Sobel(img, -1, dx=0, dy=1,
                         scale=1, delta=0, borderType = cv2.BORDER_DEFAULT)
    
    edges = edgesx + edgesy
    
    # we can play with ksize and it must be odd, by putting even no it will through an error
    # ksize must be upto 31 only
    output = [img,edgesx,edgesy,edges]
    titles = ['Original', 'dx=1 dy=0(vertical edges)' , 'dx=0 dy=1(horizontal edges)', 'Edges']
    
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




