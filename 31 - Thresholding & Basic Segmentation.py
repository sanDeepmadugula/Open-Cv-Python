#!/usr/bin/env python
# coding: utf-8
# Segmentation - diiding the image into various regions, such that boundries of such regions are marked

# 1. threshold segmentation - applied on gray scale images(basic thresholding)



# In[1]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath1 = path + "gray21.512.tiff"
    
    img = cv2.imread(imgpath1, 1)
    
    plt.imshow(img)
    plt.title("Original Image")
    plt.show()
    
if __name__ == '__main__':
    main()


# In[6]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath1 = path + "gray21.512.tiff"
    #imgpath1 = path + "4.2.07.tiff" # for colored image
    img = cv2.imread(imgpath1, 1)
    
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # for colored image only
    
    threshold = 127
    max_value = 255
    
    algorithm1 = cv2.THRESH_BINARY
    algorithm2 = cv2.THRESH_BINARY_INV
    algorithm3 = cv2.THRESH_TOZERO
    algorithm4 = cv2.THRESH_TOZERO_INV
    algorithm5 = cv2.THRESH_TRUNC
    
    ret,output1 = cv2.threshold(img,threshold,max_value,algorithm1)
    ret,output2 = cv2.threshold(img,threshold,max_value,algorithm2)
    ret,output3 = cv2.threshold(img,threshold,max_value,algorithm3)
    ret,output4 = cv2.threshold(img,threshold,max_value,algorithm4)
    ret,output5 = cv2.threshold(img,threshold,max_value,algorithm5)
    
    # list of outputs
    output = [img,output1,output2,output3,output4,output5]
    titles = ['Original','Binary','Binary Inverted','Zero','Zero Inverted','Trunc']

    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    
   
    plt.show()
    
if __name__ == '__main__':
    main()


# In[ ]:




