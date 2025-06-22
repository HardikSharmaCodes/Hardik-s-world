import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    sucess, image = cap.read()
    imageRGB = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
    result= hands.process(imageRGB)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
            for id, lm  in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id,": ", cx,cy)
                if id== 0:
                    cv2.circle(image, (cx,cy), 7, (255,100,0),3, 10)
                if (id % 4)== 0 and id != 0:
                    cv2.circle(image, (cx,cy), 7, (100,255,0),3, 10)
    cv2.putText( image,"Your Person", (10,70), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0),3)
    cv2.imshow("Image",image)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
