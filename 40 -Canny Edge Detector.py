#!/usr/bin/env python
# coding: utf-8

# In[11]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def main():
    
    path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"
    imgpath = path + "house.tiff"
    img = cv2.imread(imgpath, 0)
  #  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    L1 = cv2.Canny(img, 50, 300) 
    L2 = cv2.Canny(img, 50, 300, L2grandient=True) 
    
    L2 = img
    
    titles = ['Original Image', 'L1 Norm', 'L2 Norm']
    
    outputs = [img, L1, L2]
    
    for i in range(3):
        plt.subplot(1,3,i+1)
        plt.imshow(outputs[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
if __name__ == "__main__":
    main()


# In[ ]:




