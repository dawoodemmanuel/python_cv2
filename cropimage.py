import cv2

image = cv2.imread("Resources/image.jpg")
print("Image Shape: ",image.shape)

imageCropped = image[0:200,200:400]
cv2.imshow("Image",image)
cv2.imshow("Cropped Image",imageCropped)

cv2.waitKey(0)