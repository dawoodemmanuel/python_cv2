import cv2
import numpy as np

image = np.zeros((512,512,3), np.uint8)

cv2.line(image,(0,0),(511,511),(0,255,0),1)
cv2.rectangle(image,(120,200),(190,400),(255,0,0),5)
cv2.circle(image,(350,230),70,(100,200,150),2)
cv2.putText(image,"Hello World!!!",(110,100),cv2.FONT_HERSHEY_COMPLEX,1,(150,100,50),2)

cv2.imshow("Image",image)
cv2.waitKey(0)