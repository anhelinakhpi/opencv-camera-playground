import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 300)

if not cap.isOpened():
    print("Camera not available")
    exit()

mode = 0
#0 = norm
#1 =greyscale
#2 = edges

prev_time = 0

while True:
    success, frame = cap.read()
    
    if not success:
        break

    #FPS calc
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time

    #processing
    if mode == 1:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        display = frame
        title = "Grayscale Camera"
    elif mode == 2:
        frame = cv2.Canny(frame, 100, 200)
        display = frame
        title = "Edge Detection"
    else:
        display = frame
        title = "Normal Camera"

    #FPS text
    cv2.putText(
        display,
        f"FPS: {int(fps)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Camera", display)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        mode = 0
    elif key == ord('2'):
        mode = 1
    elif key == ord('3'):
        mode = 2
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()