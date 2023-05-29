import cv2
import time
import os
import mediapipe as mp
import math

class HandDetector():
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5, max_num_hands = 1)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB.flags.writeable = False
        self.results = self.hands.process(imgRGB)
        imgRGB.flags.writeable = True
        imgRGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:   
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS, self.mpDraw.DrawingSpec(color = (0, 0, 0)), self.mpDraw.DrawingSpec(color = (0, 255, 0)))
        return img

    def findPosition(self, img, handNumber = 0, draw = True):
        self.lmList = []
        xList = []
        yList = []
        boundingBox = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNumber]
            for id, lm in enumerate(myHand.landmark):
                height, weight, channel = img.shape
                cx, cy = int(lm.x * weight), int(lm.y * height)
                xList.append(cx)
                yList.append(cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
            xmin, xmax =  min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            boundingBox = xmin, ymin, xmax, ymax
            if draw: 
                cv2.rectangle(img, (boundingBox[0]-20, boundingBox[1]-20), (boundingBox[2]+20, boundingBox[3]+20), (0,255, 0), 2)
        return self.lmList, boundingBox

    def findDistance(self, p1, p2, img, draw = True):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        if draw:
            cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)
        return length, img, [x1, y1, x2, y2, cx, cy]
    
    def fingersUp(self):
        fingers = []
        self.tipIds = [4, 8, 12, 16, 20]
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

def main():
    wCam, hCam = 1200, 720
    capture =  cv2.VideoCapture(0)
    capture.set(3, wCam)
    capture.set(4, hCam)
    detector = HandDetector()
    prevTime = 0
    curTime = 0
    folderPath = "img/handImg"
    imgList = os.listdir(folderPath)
    overlayList = []
    tipIds = [4, 8, 12, 16, 20]
    totalFingers = 0
    for imgPath in imgList:
        image = cv2.imread(f'{folderPath}/{imgPath}')
        overlayList.append(image)
    while capture.isOpened():
        success, img = capture.read()
        img = detector.findHands(img)
        lmList, boundingBox = detector.findPosition(img, draw=True)
        if len(lmList) != 0:
            fingers = detector.fingersUp()
            # print(fingers)
            totalFingers = fingers.count(1)
            height, width, channel = overlayList[totalFingers].shape
            img[200:height+200, 50:width+50] = overlayList[totalFingers]
            cv2.rectangle(img, (57, 510), (240, 620), (152, 133, 31), cv2.FILLED)
            cv2.putText(img, str(totalFingers), (115, 598), cv2.FONT_HERSHEY_COMPLEX, 3,(150, 168, 244), 10)
        curTime = time.time()
        fps = 1/(curTime - prevTime)
        prevTime = curTime
        cv2.putText(img, f'FPS: {int(fps)}', (10, 45), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 9), 2)
        cv2.imshow("Volume Control", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()