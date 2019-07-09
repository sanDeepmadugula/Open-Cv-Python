#!/usr/bin/env python
# coding: utf-8

# In[10]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imagepath1 = path + "4.2.01.tiff"
    img1 = cv2.imread(imagepath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
   
    # Affine Transformation. Geomatric transformation comes under Affine transformation. The shhifting comes under geomatric transformation
    # to collect the value of shape we need rows, columns,channels(no of dimensions)
    
    rows, columns, channels = img1.shape
    
    # define the matrix, R = Rotation purpose
    #R = cv2.getRotationMatrix2D((columns/2,rows/2),0,1) # 0 -Rotation in degrees, 1- neighter scaling up nor scaling down
    #R = cv2.getRotationMatrix2D((columns/2,rows/2),0,0.5) # 0 -Rotation in degrees, 0.5- scaling to half
    R = cv2.getRotationMatrix2D((columns/2,rows/2),180,0.5) # 180 -Rotation in degrees, 0.5- scaling to half

    print(R)
    
    
    output = cv2.warpAffine(img1,R,(columns,rows))
    plt.imshow(output)
    plt.title('Rotated Image')
    plt.show()
    
if __name__ == "__main__":
    main()


# In[ ]:




