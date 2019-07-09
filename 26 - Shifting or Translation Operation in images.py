#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imagepath1 = path + "4.2.01.tiff"
    img1 = cv2.imread(imagepath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    plt.imshow()
    # Affine Transformation. Geomatric transformation comes under Affine transformation. The shhifting comes under geomatric transformation
    # to collect the value of shape we need rows, columns,channels(no of dimensions)
    
    rows, columns, channels = img1.shape
    
    # define the matrix, T = transformation matrix which will be represent in numpy array
    T = np.float32([[1,0,50],[0,1,-50]])
    print(T)
    
    
    output = cv2.warpAffine(img1,T,(columns,rows))
    plt.imshow(output)
    plt.title('Shifted Image')
    plt.show()
    
if __name__ == "__main__":
    main()


# In[ ]:




