# Simple program to find cars in a video
import cv2

camera_id = 'data/cars.avi'
window_name = 'cars_video'
delay = 33

cap = cv2.VideoCapture(camera_id)

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('data/cars.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # convert to gray scale for content detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detects cars in captured content
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    # Draw a rectangle around each car found
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x , y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow(window_name, frame)

    key_press = cv2.waitKey(delay) & 0xFF
    # Quit by pressing 'q' key or 'esc' key
    if key_press in (27, ord('q')):
        break

# Release used memory
cv2.destroyAllWindows()
cap.release()
