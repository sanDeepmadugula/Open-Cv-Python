#!/usr/bin/env python
# coding: utf-8

# In[5]:


# In case of perspective transformation we need to use 4 points which are non colinear that means they are not in same line

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
    
    point1 = np.float32([[0,0], [400,0],[0,400],[400,400]]) # set of points in input image
    point2 = np.float32([[0,0], [500,0],[0,500],[500,500]]) # set of points in output image

    P = cv2.getPerspectiveTransform(point1, point2)
    
    print(P)
    
    output = cv2.warpPerspective(img1, P, (700, 700))
    
    plt.imshow(output)
    plt.title('Changed Perspective Image')
    plt.show()
    

if __name__ == "__main__":
    main()


# In[ ]:




