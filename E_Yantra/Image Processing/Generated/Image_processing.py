
################## -:PART A:- ##########################################

import cv2
import numpy as np
Cat=cv2.imread('cat.jpg')
Bird=cv2.imread('bird.jpg')
Flowers=cv2.imread('flowers.jpg')
Horse=cv2.imread('horse.jpg')
w_cat=int(Cat.shape[1])
h_cat=int(Cat.shape[0])
w_bird=int(Bird.shape[1])
h_bird=int(Bird.shape[0])
w_horse=int(Horse.shape[1])
h_horse=int(Horse.shape[0])
w_flowers=int(Flowers.shape[1])
h_flowers=int(Flowers.shape[0])
print(w_cat,h_cat)
print(w_bird,h_bird)
print(w_flowers,h_flowers)
print(w_horse,h_horse)

#calculating the intensity of pixels at the center of image

cp_cat=Cat[195,320]
cp_flowers=Flowers[141,320]
cp_bird=Bird[213,320]
cp_horse=Horse[202,320]
print(cp_cat)
print(cp_flowers)
print(cp_bird)
print(cp_horse)

# importing this data into csv file
import csv
with open('stats.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Height","Width","B","G","R"])
    writer.writerow(["bird.jpg","426","640","172","88","244"])
    writer.writerow(["cat.jpg","390","640","10","113","105"])
    writer.writerow(["flowers.jpg", "283", "640","223","206","187"])
    writer.writerow(["horse.jpg", "404", "640","238","192","145"])
 
###################### -:PART B:- ##################################################
# importing essential libraries required to process
import cv2
import numpy as np
import os

#using split function to split all colors individually 
#sing np.zeros to create an array of same dimension as image so as to merge the image easily
image=cv2.imread('cat.jpg')
cv2.imshow('image',image)
B,G,R=cv2.split(image)
zero=np.zeros(image.shape[:2],dtype='uint8')
red_cat=cv2.merge([zero,zero,R])
cv2.imshow('red_cat',red_cat)
cv2.imwrite('cat_red.jpg',red_cat)

cv2.waitKey()
cv2.destroyAllWindows()

###################### -:PART C:- ###############################

#including all essential libraries
import cv2
import numpy as np
import os
import PIL
# Using PIL:-

from PIL import Image, ImageDraw, ImageFilter

img_rgb = Image.open('flowers.jpg')
img_rgba = img_rgb.copy()
img_rgba.putalpha(128)
img_rgba.save('flowers_alpha.png') 

########################### -:PART D:- ############################

import imageio
import cv2
import numpy as np
import matplotlib.pyplot as plt

pic = imageio.imread('horse.jpg')
gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) 
gray = gray(pic)  
plt.imshow(gray, cmap = plt.get_cmap(name = 'gray'))
cv2.imwrite('horse_gray.jpg',gray)   
    
    
    