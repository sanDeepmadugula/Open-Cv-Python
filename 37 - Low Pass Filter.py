#!/usr/bin/env python
# coding: utf-8

#  Low Pass Filter
#   - Blurring
#   - Denoising
#   - Smoothing
#   

# In[2]:


import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath = path + "4.2.07.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    box = cv2.boxFilter(img, -1, (53,53)) # -1 -> length of i/p and o/p image depth would keeping same, (53,53) - dimension
    
    blur = cv2.blur(img,(13,13))
    
    gaussian = cv2.GaussianBlur(img,(17,17),0)
    
    titles = ['Original Image', 'Box Filter','Blur', 'Gaussian BLur']
    
    outputs = [img, box, blur, gaussian]
    
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(outputs[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
    
if __name__ == '__main__':
    main()


# In[ ]:




