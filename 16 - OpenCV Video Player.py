#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2

def main():
    windowName = "OpenCV Video Player"
    cv2.namedWindow(windowName)
    filename = "C:\\Analytics\\Deep Learning\\Open CV\\output\\Output.avi"

    cap = cv2.VideoCapture(filename)
    
    #codec = cv2.VideoWriter_fourcc('X','V','I','D') #codec- coding & decoding, popular codecs are - WMV2,WMV1,MJPG,DIVX,XVID,H264
    # fourcc - Four character code
    #framerate = 30 # for persistance of vision, generally in movies = 24, but 30 is smooth
    #resolution = (640,480) # at lower resolution video is quite smooth
    
    #videoFileOutput = cv2.VideoWriter(filename, codec,framerate,resolution)
    
    ret = True
        
    while (cap.isOpened()):
        
        ret, frame = cap.read()
        print(ret)
            
        if ret:
            cv2.imshow(windowName,frame)
            if cv2.waitKey(1) == 27:
                break
        else:
            break
                   
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()


# In[ ]:



# Here we get the output video which is already stored , but the video output is too fast bcz of waitKey , and used framerate = 30fps in the previous example while recording and stroing in a file.
# here video is playing in 30 milliseconds.
#  1000 ms = 1sec
# 1000/30fps here = 33 we need to give in waitkey


# In[5]:


import cv2

def main():
    windowName = "OpenCV Video Player"
    cv2.namedWindow(windowName)
    filename = "C:\\Analytics\\Deep Learning\\Open CV\\output\\Output.avi"

    cap = cv2.VideoCapture(filename)
    
    #codec = cv2.VideoWriter_fourcc('X','V','I','D') #codec- coding & decoding, popular codecs are - WMV2,WMV1,MJPG,DIVX,XVID,H264
    # fourcc - Four character code
    #framerate = 30 # for persistance of vision, generally in movies = 24, but 30 is smooth
    #resolution = (640,480) # at lower resolution video is quite smooth
    
    #videoFileOutput = cv2.VideoWriter(filename, codec,framerate,resolution)
    
    ret = True
        
    while (cap.isOpened()):
        
        ret, frame = cap.read()
        print(ret)
            
        if ret:
            cv2.imshow(windowName,frame)
            if cv2.waitKey(33) == 27: # normal video speed, # 130 very slow
                break
        else:
            break
                   
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()


# In[ ]:


Now you can check down the video which is normal speed.

