import cv2
import numpy as np

kernal = np.ones((5,5), np.uint8)

image = cv2.imread("Resources/image.jpg")
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(imageGray, (7,7), 0)
imageCanny = cv2.Canny(image, 200, 200)
imageDialation = cv2.dilate(imageCanny, kernal, iterations=1)
imageErode = cv2.erode(imageDialation, kernal, iterations=1)


cv2.imshow("Gray Image", imageGray)
cv2.imshow("Blur Image", imageGray)
cv2.imshow("Canny Image", imageCanny)
cv2.imshow("Dialation Image", imageDialation)
cv2.imshow("Erode Image", imageErode)

cv2.waitKey(0)