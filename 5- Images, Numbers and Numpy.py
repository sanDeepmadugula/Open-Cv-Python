#!/usr/bin/env python
# coding: utf-8

# Images are numbers for a computer.
# video - rapid sequence of images, so set of numbers
# sounds are also numbers

# In[9]:


# for colored image
import cv2

def main():
    imgpath = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\lena_color_256.tif"
    img1 = cv2.imread(imgpath,1)
    
    print(img1)
    print(type(img1)) # class numpy.ndarray, n-dimensional array part of numerical python
    print(img1.dtype) # uint8 
    print(img1.shape)
    print(img1.ndim)
    print(img1.size)
    cv2.imshow('Lena',img1)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
if __name__ == '__main__':
    main()


# In[ ]:


# output for colored image
print(img1)
------------
[125 137 226] = Red Green Blue in pixel
but in case of open cv its

Blue Green Red (
    125- intensity of blue channel,
    137 - intensity of green channel,
    226 - intensity of red channel)

print(img1.dtype)
------------------
uint8 - Unsigned integer of 8 bits
Minimum value can be reprented as 00000000
in binary - 255 ie 0-255, set of 256 channels
0- black , 255-white
that's why we got only between 0-255 [125 137 226]

so 256^3 = 256x256x256 = 16,777,216 unique colors wll be there 
so every pixel can have 16 million unique colors.

print(img1.shape) # resolution in image
-----------------
(256,256,3) 3 -represents no of channels ie Blue Green Red

print(img1.ndim)
----------------
output - 3 ie 3 channels
(256,256,3) - height, width, channel
but if it is black and white image then it will be 2 channels

print(img1.size)
----------------
196608 (256x256x3)


# In[16]:


# for gray scale image
import cv2

def main():
    imgpath = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\lena_color_256.tif"
    img1 = cv2.imread(imgpath,0)
    
    print(img1)
    print(type(img1)) # class numpy.ndarray, n-dimensional array part of numerical python
    print(img1.dtype) # uint8 
    print(img1.ndim)
    print(img1.size)
    print(img1.shape)
    cv2.imshow('Lena',img1)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
if __name__ == '__main__':
    main()


# In[ ]:




