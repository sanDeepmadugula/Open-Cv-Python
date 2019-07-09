#!/usr/bin/env python
# coding: utf-8

# In[2]:


# affine transformation requires 3 points
# points should not fall in a same plane
import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath1 = path + "4.2.01.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img1.shape
    
    point1 = np.float32([[100,100], [300,100],[100,300]]) # set of points in input image
    point2 = np.float32([[200,150], [400,150],[200,400]]) # set of points in output image

    A = cv2.getAffineTransform(point1, point2)
    
    print(A)
    
    output = cv2.warpAffine(img1, A, (columns, rows))
    
    plt.imshow(output)
    plt.title('Transformed Image')
    plt.show()
    

if __name__ == "__main__":
    main()


# In[ ]:




