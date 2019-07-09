#!/usr/bin/env python
# coding: utf-8
# Transformations
 1. Scaling / Resizing = Shriking(scaling down)
 2. Zooming(scaling up)
 
 cv2.resize(img1,None,fx=1,fy=1, interpolation = cv2.LINEAR)
 # fx = 1 , scalilng to be performed on x axis
 # fy = 1 , scaling to be performed on y axis
 # interpolation - determines how new picture will look line based on neighbourhood pixels.
 
 # different interpolation Methods
 1. INTER_LINEAR
 2. INTER_NEAREST
 3. INTER_AREA - for shrinking
 4. INTER_CUBIC - for zooming (operates in neighbourhood area of 4x4 pixel area)
 5. INTER_LANCZOS4 - operates in neighbourhood area of 8x8
# In[5]:


import cv2

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath1 = path + "4.2.01.tiff"
    img1 = cv2.imread(imgpath1, 1)
    
   # output = cv2.resize(img1, None, fx=1, fy=1 , interpolation=cv2.INTER_LINEAR) # Original Image
   # output = cv2.resize(img1, None, fx=1.5, fy=1.5 , interpolation=cv2.INTER_CUBIC) # Stretched Image(scle up)
    output = cv2.resize(img1, None, fx=0.5, fy=0.5 , interpolation=cv2.INTER_AREA) # Scale down


    
    cv2.imshow('Output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()

    


# In[ ]:




