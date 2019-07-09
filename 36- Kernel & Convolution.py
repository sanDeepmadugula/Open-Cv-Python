#!/usr/bin/env python
# coding: utf-8
 Kernel image processing which is a convolution matrix
 matrix is represented as ndarray, ndarray is also a matrix

 Identity Kernel(we get same image when identity kernel is applied) 
        
 0 0 0
 0 1 0
 0 0 0

# In[10]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath = path + "4.2.07.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # lets create a simple conv matrix
    # k = np.array(([0,0,0],[0,1,0],[0,0,0]), np.float32) # identity kernel
    
    k = np.array(([0,1,0],
                  [1,-4,1],
                  [0,1,0]), np.float32) # edge detection kernel
    
 #   k = np.array(np.zeros((3,3),np.float32))

# to apply filter we can apply output = cv2.filter2D(img,depth of outputimg,convolution kernel)
    
    output = cv2.filter2D(img, -1, k)
    
    print(k)
    
    print(type(k))
    
    output = img
    
    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.title('Original Imate')
    
    plt.subplot(1,2,2)
    plt.imshow(output)
    plt.title('Filtered Image')
    
    plt.show()
    
if __name__ == "__main__":
    main()


# In[ ]:




