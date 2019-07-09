#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Gaussian Noise
# salt and pepper noise

import cv2
import matplotlib.pyplot as plt

def main():
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath = path + "4.2.05.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    rows,columns,channels = img.shape
    
    output = img
    
    plt.imshow(output)
    plt.title('Original Image')
    plt.show()
    
if __name__ == "__main__":
    main()


# In[6]:


# Introducing salt and pepper noise
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath = path + "4.2.05.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    rows,columns,channels = img.shape
    
    output = np.zeros(img.shape, np.uint8) # zeros are added for pepper noise, as pepper means black, for black we have only zeros
    p = 0.5 # 50 % probability of noise
    output = np.zeros(img.shape, np.uint8)
    
    for i in range(rows):
        for j in range(columns):
            r = random.random()
            if r < p/2:
                # pepper sprinkle(black noise represents in 0,0,0)
                output[i][j] = [0,0,0]
            elif r < p:
                # salt sprinkle(white noise represents in 255,255,255)
                output[i][j] = [255,255,255]
            else:
                output[i][j] = img[i][j]
    plt.imshow(output)
    plt.title('Image with salt & pepper noise')
    plt.show()
    
if __name__ == "__main__":
    main()


# In[ ]:




