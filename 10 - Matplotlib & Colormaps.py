#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

def main():
    imgpath = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\4.2.05.tiff"
    img = cv2.imread(imgpath,0)
    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()


# In[9]:


# new way to display image output using matplot lib
import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def main():
    imgpath = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\lena_color_256.tif"
    img = cv2.imread(imgpath,0)
    
    # plt.imshow(img) # push the image to show(The pic will be something differenent)
    plt.imshow(img,cmap='gray') # now it will be good . you can use different cmaps available
    plt.title('gray colormap')
    plt.xticks([]) # the numbers in x-axis will be vanish
    plt.yticks([])
    plt.show() # final output to show
    
if __name__ == "__main__":
    main()


# In[ ]:




