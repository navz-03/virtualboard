import cv2
import mediapipe as mp
import time


class handdectector:

    def __init__(self, mode=False, maxHands=2, complexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.complexity = complexity
        self.detectioncon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.complexity, self.detectioncon, self.trackCon)
        self.mpdraw = mp.solutions.drawing_utils
        self.tipids = [4, 8, 12, 16, 20]

    def findhands(self, img, draw=True):
        imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRBG)
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findpostion(self, img, handno=0, draw=True):
        self.lmlist = []
        if self.result.multi_hand_landmarks:
            myhand = self.result.multi_hand_landmarks[handno]
            for id, lm in enumerate(myhand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)
        return self.lmlist

    def fingersup(self):
        fingers = []
        # thumb
        if self.lmlist[self.tipids[0]][1] < self.lmlist[self.tipids[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # fingers
        for id in range(1, 5):
            if self.lmlist[self.tipids[id]][2] < self.lmlist[self.tipids[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers


def main():
    cap = cv2.VideoCapture(0)
    dectector = handdectector()
    ptime = 0
    ctime = 0
    while True:
        success, img = cap.read()
        img = dectector.findhands(img)
        lmlist = dectector.findpostion(img)
        if len(lmlist) != 0:
            print(lmlist[8])

        # fps calculation#
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(img, str(int(fps)), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        cv2.imshow("Video", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
