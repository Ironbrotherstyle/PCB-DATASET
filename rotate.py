import cv2
from math import *
import numpy as np
import random
import os
import glob as gb

def rotate_bound_white_bg(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)

    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image

    return cv2.warpAffine(image, M, (nW, nH),borderValue=(143,148,151))

    # return cv2.warpAffine(image, M, (nW, nH))

file="Open_circuit"
f=open(file+'_angles.txt','a')
out_name=[]
path1 = "/home/weapon/Desktop/PCB_DATASET/"+file
# print(path1)
path2 = "/home/weapon/Desktop/PCB_DATASET/"+file+"_rotation"
# print(path2)
paths = gb.glob(path1+"/*.jpg")
# print(paths)
for path in paths:

 	file_name=path.split('/')[-1].split('.')[-2]
 	# print(file_name)
	angle=random.randint(-10,10)
	img = cv2.imread(path)

	imgRotation = rotate_bound_white_bg(img, angle)

	# print(angle)
	f.write(str(file_name) + '\t' +  str(angle) + '\n')
	cv2.imwrite(path2+"/"+file_name+".jpg",imgRotation)
	#cv2.imshow("img",img)
	#cv2.imshow("imgRotation",imgRotation)
	#cv2.waitKey(0)
 	
