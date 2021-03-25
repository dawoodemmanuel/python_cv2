import cv2
import numpy as np

image = cv2.imread("Resources/4king.jpeg")
print(image.shape)

width,height = 200,200

pts1 = np.float32(([173,16],[261,20],[82,105],[192,160]))
pts2 = np.float32(([0,0],[width,0],[0,height],[width,height]))

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imageOutput = cv2.warpPerspective(image,matrix,(width,height))

cv2.imshow("Image",image)
cv2.imshow("Matrix",matrix)
cv2.imshow("Output Image",imageOutput)

cv2.waitKey(0)