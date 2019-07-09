#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2

def main():
    windowName = "Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    filename = "C:\\Analytics\\Deep Learning\\Open CV\\output\\Output.avi"
    codec = cv2.VideoWriter_fourcc('X','V','I','D') #codec- coding & decoding, popular codecs are - WMV2,WMV1,MJPG,DIVX,XVID,H264
    # fourcc - Four character code
    framerate = 30 # for persistance of vision, generally in movies = 24, but 30 is smooth
    resolution = (640,480) # at lower resolution video is quite smooth
    
    videoFileOutput = cv2.VideoWriter(filename, codec,framerate,resolution)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        
        ret, frame = cap.read()
        
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        videoFileOutput.write(frame)
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    videoFileOutput.release()
    cap.release()
    
if __name__ == "__main__":
    main()


# In[ ]:




