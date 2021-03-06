import cv2

image = cv2.imread("Resources/image.jpg")

cv2.imshow("Image Read", image)
cv2.waitKey(0)
