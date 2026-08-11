import cv2
import numpy as np

# Create a white canvas
img = np.ones((500, 500, 3), dtype=np.uint8) * 255

points = []

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global points, img

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

        # Draw the clicked point
        cv2.circle(img, (x, y), 4, (0, 0, 255), -1)

        # Draw rectangle after 4 points are clicked
        if len(points) == 4:
            cv2.line(img, points[0], points[1], (255, 0, 0), 2)
            cv2.line(img, points[1], points[2], (255, 0, 0), 2)
            cv2.line(img, points[2], points[3], (255, 0, 0), 2)
            cv2.line(img, points[3], points[0], (255, 0, 0), 2)

cv2.namedWindow("Draw Rectangle")
cv2.setMouseCallback("Draw Rectangle", draw_rectangle)

while True:
    cv2.imshow("Draw Rectangle", img)

    key = cv2.waitKey(1) & 0xFF

    # Press 'r' to reset
    if key == ord('r'):
        img = np.ones((500, 500, 3), dtype=np.uint8) * 255
        points = []

    # Press 'q' to quit
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
