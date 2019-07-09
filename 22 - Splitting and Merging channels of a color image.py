#!/usr/bin/env python
# coding: utf-8
Color various channels

Greyscale / Black & White = single channel,0 = black, 255 or 1 = white
RGB / BGR = B G R
HSV = Hue Saturation Value/intensity
CMY = CYAN Magenta Yellow
CCMYK = CYAN Magenta Yellow Key

cv2.split() - returns multiple channels which contain intensity of multiple levels

cv2.merge() - to compse single image using this color channel

# In[2]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"

imgpath1 = path + "4.2.01.tiff"

img = cv2.imread(imgpath1, 1)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r,g,b = cv2.split(img1)

titles = ['Original Image', 'Red', 'Green', 'Blue']
images = [cv2.merge((r,g,b)),r, g, b]

plt.subplot(2,2,1)
plt.imshow(images[0])
plt.title(titles[0])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(images[1], cmap='gray')
plt.title(titles[1])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(images[2], cmap='gray')
plt.title(titles[2])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(images[3], cmap='gray')
plt.title(titles[3])
plt.xticks([])
plt.yticks([])

plt.show()

# as per original image is red, hence the output red is showing white one.


# In[4]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

path = "C:\\Analytics\\Deep Learning\\Open CV\\misc\\"

imgpath1 = path + "4.2.01.tiff"

img = cv2.imread(imgpath1, 1)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r,g,b = cv2.split(img1)

titles = ['Original Image', 'Red', 'Green', 'Blue']
images = [cv2.merge((r,g,b)),r, g, b]

plt.subplot(2,2,1)
plt.imshow(images[0])
plt.title(titles[0])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(images[1], cmap='Reds')
plt.title(titles[1])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(images[2], cmap='Greens')
plt.title(titles[2])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(images[3], cmap='Blues')
plt.title(titles[3])
plt.xticks([])
plt.yticks([])

plt.show()

# as per original image is red, hence the output red is showing white one.


# In[ ]:




