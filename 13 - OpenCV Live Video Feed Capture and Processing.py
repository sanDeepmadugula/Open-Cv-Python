#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import matplotlib.pyplot as plt

def main():
    cap = cv2.VideoCapture(0) # if multiple video cameras are attched then you can choose anyone of them. 0 means very first webcam attached
    
    if cap.isOpened():
        ret,frame = cap.read() # capture single framework, ret return variable
        print(ret)
        print(frame)
    else:
        ret = False
    
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    plt.imshow(img1)
    plt.title("Color Image RGB")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    cap.release() # releases the camera
        
      
        
if __name__ == '__main__':
    main()


# In[4]:


# The above is for pic, lets see how to use for video capturing
import cv2


def main():
    windowName = "Live Video Feed"
    cap = cv2.VideoCapture(0) # if multiple video cameras are attched then you can choose anyone of them. 0 means very first webcam attached
    
    if cap.isOpened():
        ret,frame = cap.read() # capture single framework, ret return variable
    else:
        ret = False
    
    while ret :
        ret, frame = cap.read()
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow(windowName,frame)  # color mode
        cv2.imshow("Gray",output) # gray scale mode
        if cv2.waitKey(1) == 27:
            break
    
    cv2.destroyAllWindows(windowName)
    
    cap.release() # releases the camera
        
    
        
if __name__ == '__main__':
    main()


# In[ ]:




