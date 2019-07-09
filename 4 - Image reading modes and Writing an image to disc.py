#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2

def main():
    imgpath = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.1.04.tiff"
    img = cv2.imread(imgpath,1) #1 is by default reading mode(1 - by saving all coloring information. if you wont mention also its ok)
    #img = cv2.imread(imgpath,0) # 0 means  gray scale in image
    #img = cv2.imread(imgpath,-1) # loads the image as it is, saves the alpha transperency 
    outpath = "C:\\Analytics\\Deep Learning\\Open CV\\output\\4.1.04.jpg"

    cv2.imshow('Lena',img)
    cv2.imwrite(outpath,img) # to save pic
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
        
if __name__ == '__main__':
    main()


# In[8]:


# now lets read as gray scale image 0
import cv2

def main():
    imgpath = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.1.04.tiff"
    # img = cv2.imread(imgpath,1) #1 is by default reading mode(1 - by saving all coloring information. if you wont mention also its ok)
    img = cv2.imread(imgpath,0) # 0 means  gray scale in image
    #img = cv2.imread(imgpath,-1) # loads the image as it is, saves the alpha transperency 
    outpath = "C:\\Analytics\\Deep Learning\\Open CV\\output\\4.1.04.jpg"

    cv2.imshow('Lena',img)
    cv2.imwrite(outpath,img) # to save pic
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
        
if __name__ == '__main__':
    main()


# In[ ]:




