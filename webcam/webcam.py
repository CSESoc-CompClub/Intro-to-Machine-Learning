# Simple program to continuously capture webcam content
import cv2
import sys

camera_id = 1           # needs access to a webcam (might be 0, might be 1, depends on machine)
window_name = 'frame'   # where to output image to
delay = 1               # how many milliseconds do we wait for a key press?

# gets camera
cap = cv2.VideoCapture(camera_id)

# Check if camera exists
if not cap.isOpened():
    sys.exit()

# Loop until quit
while True:
    # Read an image from the captured content
    ret, frame = cap.read()
    # Display the image
    cv2.imshow(window_name, frame)
    # Quit by pressing 'q' or 'esc' key
    if cv2.waitKey(delay) & 0xFF in (27, ord('q')):
        break

# Release used memory
cv2.destroyAllWindows()
cap.release()
