#!/usr/bin/env python
# coding: utf-8

# In[2]:


# create custom filter
import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    w = 800
    h = 600
    
    cap = cv2.VideoCapture(0)
    
    cap.set(3, w)
    cap.set(4, h)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        
        ret, frame = cap.read()

        #below is the custom written code for max rgb vlaue on a live video
        
        (B,G,R) = cv2.split(frame)
        
        M = np.maximum(np.maximum(R, G), B)
        R[R < M] = 0
        G[G < M] = 0
        B[B < M] = 0
        
        output = cv2.merge((B, G, R))
        
        cv2.imshow("Original", output)
        
        if cv2.waitKey(1) == 27:
            break
            
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()
    
    
    


# In[ ]:




