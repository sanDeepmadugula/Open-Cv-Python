#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def main():
    imgpath = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\lena_color_256.tif"
    img = cv2.imread(imgpath,1)
    
    plt.imshow(img) 
    plt.title('Color image with default colormap')
    plt.xticks([]) # the numbers in x-axis will be vanish
    plt.yticks([])
    plt.show() # final output to show
    
if __name__ == "__main__":
    main()
    
# output image color is distored. bcz
# 1. when ever we say, cv2.imread -> it stores as BGR
# 2. where as in  matplotlibs , plt.imshow() -> it stores as RGB
# 3. BGR and RGB are the color spaces.


# In[ ]:


# Gray scale images are 2D - height and width
# color images are 3D - height, width, channels
# various colorspaces - GRAY, RGB, BGR, HSV(Hue Saturation Value), CMY, CMYK


# In[6]:


# To overcome the above problem 
import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def main():
    imgpath = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\lena_color_256.tif"
    img = cv2.imread(imgpath,1)
    
    # we need to change the color space of img
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img) 
    plt.title('Color image with default colormap')
    plt.xticks([]) # the numbers in x-axis will be vanish
    plt.yticks([])
    plt.show() # final output to show
    
if __name__ == "__main__":
    main()
    
# now output is as before


# In[7]:


# program to list out all color conversion stuffs
import cv2

def main():
    j = 0
    for filename in dir(cv2):
        if filename.startswith('COLOR_'):
            print(filename)
            j = j+1
    print('There are' + str(j+1) + 'color conversion flags in OpenCV')
    
if __name__ == '__main__':
    main()


# In[ ]:




