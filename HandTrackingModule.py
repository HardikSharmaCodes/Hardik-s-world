import cv2
import mediapipe as mp
"""
main() works as a test runner.
from HandTrackingModule import HandDetector

findHands(image, draw=True) → Detect hands and draw connections.
findPosition(image, handNo=0) → Get coordinates of hand landmarks.
"""

class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionConfidence=0.5, trackingConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfidence = detectionConfidence
        self.trackingConfidence = trackingConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionConfidence,
            min_tracking_confidence=self.trackingConfidence
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, image, draw=True):
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)

        return image

    def findPosition(self, image, handNo=0, draw=True):
        landmarkList = []

        if self.results.multi_hand_landmarks:
            selectedHand = self.results.multi_hand_landmarks[handNo]
            h, w, _ = image.shape

            for id, lm in enumerate(selectedHand.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarkList.append((id, cx, cy))
                if draw:
                    if id == 0:
                        cv2.circle(image, (cx, cy), 7, (255, 100, 0), cv2.FILLED)
                    elif id % 4 == 0:
                        cv2.circle(image, (cx, cy), 6, (100, 255, 0), 2)

        return landmarkList


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        if lmList:
            print(lmList[0])

        cv2.putText(img, "Hand Tracker", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


