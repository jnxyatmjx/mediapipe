import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

pTime = 0

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,960)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,320)
cap.set(cv2.CAP_PROP_FPS,30)

with mp_face_mesh.FaceMesh(False,3,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.2) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = face_mesh.process(image)

    # Draw the face mesh annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
        mp_drawing.draw_landmarks(
            image=image,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACE_CONNECTIONS,
            landmark_drawing_spec=drawing_spec,
            connection_drawing_spec=drawing_spec)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    image = cv2.putText(image,'FPS:' + str(int(fps)), (50,50),cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (3,12,156), 1, cv2.LINE_AA)

    cv2.imshow('MediaPipe FaceMesh', image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
      break
cap.release()