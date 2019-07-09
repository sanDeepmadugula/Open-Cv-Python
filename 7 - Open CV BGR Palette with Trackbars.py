#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import libraries
import cv2
import numpy as np

def emptyFunction():
    pass

def main():
    
    # define an empty image
    img1 = np.zeros((512,512,3),np.uint8)
    windowName = 'OpenCV BGR Color Palette'
    cv2.namedWindow(windowName)
    
    # create trackbars
    cv2.createTrackbar('B',windowName,0,255,emptyFunction) # track bar created for blue, 0- min value and 255- max value of track bar
    cv2.createTrackbar('G',windowName,0,255,emptyFunction) # track bar created for Green
    cv2.createTrackbar('R',windowName,0,255,emptyFunction) # track bar created for Red
    
    while(True):
        cv2.imshow(windowName,img1)
        
        if cv2.waitKey(1) == 27: # 27 is the key for escape
            break
            
        blue = cv2.getTrackbarPos('B',windowName)
        green = cv2.getTrackbarPos('G',windowName)
        red = cv2.getTrackbarPos('R',windowName)
        
        # create a composite image
        img1[:] = [blue,green,red]
        
        
    cv2.destroyAllWindows()
         
if __name__ == '__main__':
    main()


# In[ ]:




