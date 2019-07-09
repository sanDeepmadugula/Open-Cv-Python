#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

def emptyFunction():
    pass

def main():
    imgpath1 = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.01.tiff"
    imgpath2 = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.07.tiff"
    
    img1 = cv2.imread(imgpath1,1)
    img2 = cv2.imread(imgpath2,1)
    
    output = cv2.addWeighted(img1, 0.5, img2,0.5,0) # alpha,beta,gamma - 0.5,0.5,0(Blending effect)
    
    windowName = "Transition Demo"
    cv2.namedWindow(windowName)
    
    cv2.createTrackbar("Alpha", windowName, 0, 10, emptyFunction) # divide track position by 10 par
    
    while (True):
        
        cv2.imshow(windowName, output)
        
        if cv2.waitKey(1) == 27:
            break
            
        alpha = cv2.getTrackbarPos('Alpha',windowName) / 10 # to get 10 values in the interval
        beta = 1 - alpha
        
        output = cv2.addWeighted(img1, alpha, img2, beta,0)
        print(alpha,beta)
        
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()
        


# In[ ]:




