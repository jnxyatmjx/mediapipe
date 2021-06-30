import cv2
import time

pTime = 0
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap.set(cv2.CAP_PROP_FPS,30)
while cap.isOpened():
    succ , image = cap.read()
    if not succ:
        print('Empty frame omit')
        continue
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    print(fps)

    image = cv2.putText(image,'FPS:' + str(int(fps)), (50,50),cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (213,12,56), 1, cv2.LINE_AA)
    cv2.imshow("OK",image)
    

    if cv2.waitKey(5) & 0xFF == ord('q'):
      break

cap.releast()