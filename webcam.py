import cv2

webcam = cv2.VideoCapture(0)
webcam.set(0,120)
webcam.set(0,200)

while True:
    success, image = webcam.read()
    cv2.imshow("Video Read", image)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break