#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import time

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imagepath = path + "4.2.01.tiff"
    img1 = cv2.imread(imagepath, 1)
    
    rows, columns, channels = img1.shape # shape returns rows,cols,channels ie dimesnion
    
    angle = 0
    
    while True:
       # if angle == 360: # anticlock wise rotation
        #    angle = 0
            
        if angle == 0: # clock wise rotation
            angle = 360
        
        R = cv2.getRotationMatrix2D((columns/2,rows/2),angle,0.5)
        print(R)
        
        output = cv2.warpAffine(img1, R, (columns,rows))
        
        cv2.imshow('Rotatedd Image', output)
        # angle = angle + 1 # anticlock wise rotation
        angle = angle - 1 # clock wise rotation
        time.sleep(0.01)
        
        if cv2.waitKey(1) == 27:
            break
            
    cv2.destroyWindow('Rotated Image')
    
if __name__ == '__main__':
    main()


# In[ ]:


# For live webcam
import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import time

def main():
    
    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    rows, columns, channels = frame.shape
    angle = 0
    scale = 0.1
    # scale = 1
    
    while True:
        
        ret, frame = cap.read()
        
        if angle == 360:
            angle = 0
        
        if scale < 2:
            scale = scale + 0.1
            
        if scale >= 2:
            scale = 0.1
            
        print(scale)
        
        R = cv2.getRotationMatrix2D((columns/2,rows/2),angle,scale) # column/2,row/2 - To make image at center
        print(R)
        
        output = cv2.warpAffine(frame, R, (columns,rows))
        
        cv2.imshow(windowName, output)
        angle = angle + 1
        time.sleep(0.05)
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == '__main__':
    main()
        
            


# In[ ]:




