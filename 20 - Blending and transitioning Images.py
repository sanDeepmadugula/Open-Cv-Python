#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def main():
    
    imgpath1 = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.01.tiff"
    imgpath2 = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.07.tiff"


    img1 = cv2.imread(imgpath1,1)
    img2 = cv2.imread(imgpath2,1)



    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    
    alpha = 0.5
    beta = 0.5
    gamma = 0
    
   
    output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    # output = img1 * alpha + img2 * beta + gamma (can achieve blending effect)
    # but if we add output = img1 + img2 then output will be something else

    titles = ['Liquid Drop', 'Veg', 'Weighted Addition']
    images = [img1, img2, output]


    for i in range(3):
        plt.subplot(1,3,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks()
        plt.yticks()
    
   
    
    plt.show()
    
if __name__ == '__main__':
    main()


# In[8]:


# Transitioning Images
import cv2
import numpy as np
import time

def main():
    
    imgpath1 = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.01.tiff"
    imgpath2 = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.07.tiff"


    img1 = cv2.imread(imgpath1,1)
    img2 = cv2.imread(imgpath2,1)

    
    alpha = 0.0
    beta = 1.0
    gamma = 0
    
    for i in np.linspace(0, 1, 100): # 0 to 1 interval will be divided into 10 parts
        alpha = i
        beta = 1 - alpha
        output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
        cv2.imshow('Transition',output)
        time.sleep(0.05)
        if cv2.waitKey(1) == 27:
            break
            
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()


# In[ ]:




