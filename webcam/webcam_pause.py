# Simple program to continously captures webcam content, and feed can be paused
import cv2
import sys
import time

camera_id = 1
window_name = 'frame'
delay = 1

# gets camera
cap = cv2.VideoCapture(camera_id)
if not cap.isOpened():
    sys.exit()

is_webcam_paused = False
while True:
    if is_webcam_paused:
        # unpause webcam by pressing 'p' key again
        if cv2.waitKey(delay) & 0xFF == ord('p'):
            time.sleep(0.1)
            is_webcam_paused = False
        continue

    # Read an image from the captured content
    _, frame = cap.read()
    cv2.imshow(window_name, frame)

    key_press = cv2.waitKey(delay) & 0xFF
    # Quit by pressing 'q' or 'esc' key
    if key_press in (27, ord('q')):
        break
    # Pause capture by pressing 'p' key
    if key_press == ord('p'):
        time.sleep(0.1)
        is_webcam_paused = True

# Release used memory
cv2.destroyAllWindows()
cap.release()
