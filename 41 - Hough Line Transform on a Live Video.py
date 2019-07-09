#!/usr/bin/env python
# coding: utf-8

# In[5]:


# to calcluate the lines in a video
import cv2
import numpy as np


def main():
    
    windowName = "Preview"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        ret, frame = cap.read()
        
        grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(grey, 50, 250,apertureSize=5, L2gradient=True )
        # 50,250- lower & upper threshold gradient
        
        lines = cv2.HoughLines(edges, 1,np.pie/180 ) 
        #1-row value, distance accuray of accumulator
        # np.pie - theta value
        # 200 - threshold
        
        if lines is not None:
            for row, theta in lines[0]:
                a = np.cos(theta) # converting polar co-oridates to cartesian co-ordinates
                b = np.sin(theta)
                x0 = a * row
                y0 = b * row
                
                # calculate the end points of line
                pts1 = (int(x0 + 1000*(-b)),int(y0 + 1000*(a)))
                pts2 = (int(x0 - 1000*(-b)),int(y0 - 1000*(a)))
                cv2.line(frame, pts1, pts2 , (0,255,0),1)
                
        cv2.imshow(windowName,frame)
        
        if cv2.waitKey(1) == 27:
            break
            
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()
        
    
        


# In[ ]:




