
#open CV stuff helps us with the camera
import cv2

#For input
from pynput.keyboard import Key, Controller

#For detecting the hand
from cvzone.HandTrackingModule import HandDetector


keyboard = Controller()
cap = cv2.VideoCapture(0)


def showVideo(): 
    while cap.isOpened():

        ret, frame = cap.read()
        height, width, layers = frame.shape

        frame = cv2.resize(frame, ( width//2, height//2))

        cv2.imshow('Frame', frame)

        k = cv2.waitKey(1)

        if k == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

showVideo()

