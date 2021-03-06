import cv2

video = cv2.VideoCapture("Resources/video.mp4")

while True:
    success, image = video.read()
    cv2.imshow("Video Read", image)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
