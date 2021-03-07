import cv2

image = cv2.imread("Resources/image.jpg")
print("Image Shape : ",image.shape)

imageResize = cv2.resize(image,(200,300))
print("Resize Image Shape: ",imageResize.shape)

cv2.imshow("Image",image)
cv2.imshow("Resize Image",imageResize)
cv2.waitKey(0)