#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
def main():
    print("cv2 version:",cv2.__version__)

if __name__== "__main__":
    main()


# In[4]:


import cv2
def main():
    imgpath = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.05.tiff"
    img = cv2.imread(imgpath)
    
    cv2.imshow('Lena',img) # we have to specify the name of window
    cv2.waitKey(0) # to bind the keybold event cv2.imshow method
    cv2.destroyAllWindows() # when we enter any key on keyboard it is goint to destroy the window
    
if __name__ == "__main__":
    main()


# In[6]:


# before imshow method call create an explicit window
import cv2
def main():
    imgpath = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.05.tiff"
    img = cv2.imread(imgpath)
    cv2.namedWindow('Lena',cv2.WINDOW_AUTOSIZE) # explicit window
    cv2.imshow('Lena',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows('Lena') # named window destroyed
    
if __name__ == '__main__':
    main()


# In[ ]:




