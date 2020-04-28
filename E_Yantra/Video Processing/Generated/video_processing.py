
################## -:PART A:- ###########################

#capturing the image at 6th second

import cv2
import numpy as np
cap=cv2.VideoCapture('RoseBloom.mp4')
cap.set(cv2.CAP_PROP_POS_MSEC,6000)
success,image=cap.read()
if success:
    cv2.imwrite('frame_6_sec.jpg',image)
    cv2.imshow('6_sec',image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    print('complete')
    
##################### -:PART B:- ###########################
    
#converting it to red color
    
flower=cv2.imread('frame_6_sec.jpg')
cv2.imshow('image',flower)
B,G,R=cv2.split(flower)
zero=np.zeros(flower.shape[:2],dtype='uint8')
red_flower=cv2.merge([zero,zero,R])
cv2.imshow('red_flower',red_flower)
cv2.imwrite('frame_as_6_red.jpg',red_flower)
cv2.waitKey()
cv2.destroyAllWindows()




