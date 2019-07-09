#!/usr/bin/env python
# coding: utf-8

# Reducing the quality of image/ Representing the image with less number 
# of colors or shades - Image Quantization

# In[12]:


# Kmeans clustering
import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np

def main():
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath = path + "Lenna.png"
    
    img = cv2.imread(imgpath,1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    Z= img.reshape((-1,1))
    Z= np.float32(Z) # converted uint8 to float32
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10, 1.0)

    K = 2 # no of colors to be quantized to
    ret, label1, center1 = cv2.kmeans(Z,K,None,criteria,10,
                                      cv2.KMEANS_RANDOM_CENTERS) 
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    
    K = 4 # no of colors to be quantized to
    ret, label1, center1 = cv2.kmeans(Z,K,None,criteria,10,
                                  cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    
    
    K = 12 # no of colors to be quantized to
    ret, label1, center1 = cv2.kmeans(Z,K,None,criteria,10,
                                      cv2.KMEANS_RANDOM_CENTERS)
    
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    
    output1 = res1.reshape((img.shape))
    output2 = res1.reshape((img.shape))
    output3 = res1.reshape((img.shape))
    
    
    
    output = [img, output1, output2, output3]
    titles = ['Original Image', 'K=2', 'K=4', 'K=12']
    
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()
        
    


# In[19]:


# Quantization with kmeans

import cv2
import numpy as np

def main():
    
    w = 160
    h = 120
    
    cap = cv2.VideoCapture(0)
    cap.set(3,w)
    cap.set(4,h)
    
    print(cap.get(3), cap.get(4))
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        
        ret, frame = cap.read()
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
        Z= frame.reshape((-1,1))
        Z= np.float32(Z) # converted uint8 to float32
    
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10, 1.0)

        K = 5 # no of colors to be quantized to
        ret, label1, center1 = cv2.kmeans(Z,K,None,criteria,10,
                                      cv2.KMEANS_RANDOM_CENTERS) 
        center1 = np.uint8(center1)
        res1 = center1[label1.flatten()]
    
        output1 = res1.reshape((frame.shape))
        
        cv2.imshow("Original",frame)
        cv2.imshow("Quantized",output1)
        
        if cv2.waitKey(1) == 27:
            break
            
    cv2.destroyAllWindows()
    cap.release()
    
   
    
if __name__ == "__main__":
    main()
        
    


# In[ ]:




