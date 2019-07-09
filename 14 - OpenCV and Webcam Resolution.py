#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2

def main():
    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    print('Width:' + str(cap.get(3))) # gives the resolution of width, Property no. 3 of any digital camera gives the Width
    print('Height:' + str(cap.get(4))) # gives the resolution of height,Property no. 4 of any digital camera gives the Height

    # after running the program got the width and height as 640.0, 480.0 which is default
    
    # now lets set the resolution manually
    cap.set(3, 1024) # set the 3rd parameter rolution
    cap.set(4,768) # set the 4th parameter resolution
    
    print('New Width:' + str(cap.get(3))) 
    print('New Height:' + str(cap.get(4)))
    # after setting new height and widht got widht and height as :
     # New Width:960.0
     # New Height:540.0
    # might be camera not able to display it, might be the maximum resolution for this camera is 960x540
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        
        ret, frame = cap.read()
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow("Gray",output)
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
        


# In[ ]:




