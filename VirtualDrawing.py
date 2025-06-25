import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

red_points= []

while True:
    sucess, image = cap.read()
    image = cv2.flip(image, 1)
    imageRGB = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
    result= hands.process(imageRGB)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
            for id, lm  in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy , cz= int(lm.x*w), int(lm.y*h), int(lm.z* 1000)
                print(id,": ", cx,cy,cz)
                if id== 0:
                    cv2.circle(image, (cx,cy), 7, (255,100,0),3, 10)
                if (id % 4)== 0 and id != 0:
                    cv2.circle(image, (cx,cy), 7, (100,255,0),3, 10)
                if cz < (-80) and id == 8:
                    red_points.append((cx,cy))   
        for pt in red_points:
            cv2.circle(image, pt, 10, (0, 0, 255), -1)
    cv2.putText( image,"Hardik Sharma", (10,70), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0),3)
    cv2.imshow("Image",image)
    cv2.waitKey(1)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('d'):
        red_points.clear()
cap.release()
cv2.destroyAllWindows()
