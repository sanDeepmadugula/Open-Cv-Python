#!/usr/bin/env python
# coding: utf-8

# In[8]:


import cv2
import numpy as np

def main():
  
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # hsv - hue saturation value
        
        # as here converting Blue green Red to HSV
        
        
        # trackig with Blue color
        # low = np.array([100,50,50])
        # high = np.array([140, 255, 255])
        
        # tracking with green color
        low = np.array([40,50,50])
        high = np.array([80, 255, 255])
        
        # tracking with red color
        low = np.array([140,150,0])
        high = np.array([180, 255, 255])
        # we can track either with blue/green/red color
        
        image_mask = cv2.inRange(hsv, low, high) # image_mask return the binary image/ binary matrix based on interval between low and high
        
        output  = cv2.bitwise_and(frame,frame,mask=image_mask) # making bitwise end of two masks by passing two frames
        
        cv2.imshow("Image mask", image_mask)
        
        cv2.imshow("Original Webcam Feed", frame)
        cv2.imshow("Color Tracking", output)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == '__main__':
    main()


# In[ ]:




