# game => https://chromedino.com

import cv2
from pynput.keyboard import Key, Controller
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

# showVideo()

def showVideoWHands(): 
    from cvzone.HandTrackingModule import HandDetector

    detector = HandDetector(detectionCon= .8, maxHands = 1)

    while cap.isOpened():

        ret, frame = cap.read()
        height, width, layers = frame.shape

        frame = cv2.resize(frame, ( width//2, height//2))

        hands, image = detector.findHands(frame)

        cv2.imshow('Frame', image)

        k = cv2.waitKey(1)

        if k == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()


# showVideoWHands()

def showVideoWFingers(): 

    detector = HandDetector(detectionCon= .8, maxHands = 1)

    while cap.isOpened():

        ret, frame = cap.read()
        height, width, layers = frame.shape

        frame = cv2.resize(frame, ( width//2, height//2))

        hands, image = detector.findHands(frame)

        if hands:
            lmList = hands[0]

            fingerUp = detector.fingersUp(lmList)

            print(fingerUp)
            
            if fingerUp[1] == 1:
                cv2.putText(frame, 'Jump', (20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            if fingerUp[1] == 1:
                cv2.putText(frame, 'Neutral', (20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)


        cv2.imshow('Frame', image)

        k = cv2.waitKey(1)

        if k == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

# showVideoWFingers()

def playGameWFingers(): 

    detector = HandDetector(detectionCon= .8, maxHands = 1)

    while cap.isOpened():

        ret, frame = cap.read()
        height, width, layers = frame.shape

        frame = cv2.resize(frame, ( width//2, height//2))

        hands, image = detector.findHands(frame)

        if hands:
            lmList = hands[0]

            fingerUp = detector.fingersUp(lmList)

            lmList2 = lmList["lmList"]
            print(lmList2)

            length, info, image  = detector.findDistance([lmList2[4][0], lmList2[4][1]] , [lmList2[8][0], lmList2[8][1]] , image)
            print(length)

            print(fingerUp)
            
            if fingerUp[1] == 1:
                cv2.putText(frame, 'Jump', (20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                keyboard.press(Key.space)
                
            else:
                cv2.putText(frame, 'Neutral', (20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                keyboard.release(Key.space)

        cv2.imshow('Frame', image)

        k = cv2.waitKey(1)

        if k == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

# playGameWFingers()

def playGameWDistance(): 

    detector = HandDetector(detectionCon= .8, maxHands = 1)

    while cap.isOpened():

        ret, frame = cap.read()
        height, width, layers = frame.shape

        frame = cv2.resize(frame, ( width//2, height//2))

        hands, image = detector.findHands(frame)

        if hands:
            lmList = hands[0]["lmList"]

            print(lmList)
            
            coord1 = [lmList[4][0], lmList[4][1]]
            coord2 = [lmList[8][0], lmList[8][1]] 
            coord3 = [lmList[12][0], lmList[12][1]] 

            length1, info, image  = detector.findDistance( coord1, coord2, image)
            length2, info, image  = detector.findDistance( coord1, coord3, image)
            print(length1)
            

            if length1 <= 18:
                cv2.putText(frame, 'Jump', (20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                keyboard.press(Key.space)
            # else:
            #     cv2.putText(frame, 'Neutral', (20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            #     keyboard.release(Key.space)
            elif length2 <= 25:
                cv2.putText(frame, 'Duck', (40,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                keyboard.press(Key.down)
            else:
                cv2.putText(frame, 'Neutral', (40,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                keyboard.release(Key.space)
                keyboard.release(Key.down)


        cv2.imshow('Frame', image)

        k = cv2.waitKey(1)

        if k == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

playGameWDistance()