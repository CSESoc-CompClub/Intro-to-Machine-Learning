# More complex program which continuously captures webcam content, and
# tries to detect front-on face, eyes, and smile
import cv2
import sys

camera_id = 1
window_name = 'frame'
delay = 1

# load the required trained XML classifiers
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# Trained XML classifiers describes some features of some object we want to
# detect a cascade function is trained from a lot of positive(faces) and
# negative(non-faces) images.
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
# Trained XML file for detecting eyes
eye_cascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')

# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_smile.xml
# Trained XML file for detecting smiles
smile_cascade = cv2.CascadeClassifier('data/haarcascade_smile.xml')

# gets camera for capture
cap = cv2.VideoCapture(camera_id)
if not cap.isOpened():
    sys.exit()

while True:
    _, frame = cap.read()

    # convert to gray scale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detects faces in captured content
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw a rectangle around each face found
        cv2.rectangle(frame, (x, y), (x + w,y + h), (0, 255, 0), 2)
        roi_gray = gray[y:(y + h), x:(x + w)]
        roi_color = frame[y:(y + h), x:(x + w)]

        # Detects eyes of different sizes in the input image
        eyes = eye_cascade.detectMultiScale(roi_gray)
        # Draw a rectangle around each eye found
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

        # Detects smile in the input image
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        # Draw a rectangle around each smile found
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)

    cv2.imshow(window_name, frame)

    key_press = cv2.waitKey(delay) & 0xFF
    # Quit by pressing 'q' key or 'esc' key
    if key_press in (27, ord('q')):
        break

# Release used memory
cv2.destroyAllWindows()
cap.release()
