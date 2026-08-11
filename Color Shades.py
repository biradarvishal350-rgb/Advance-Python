import cv2
import numpy as np

# Create a blank color image (300x400)
img = np.zeros((300, 400, 3), dtype=np.uint8)

# Fill each horizontal strip with a different color (BGR format)

img[0:50, :] = (128, 130, 128)      # Purple
img[50:100, :] = (70, 165, 255)    # Orange
img[100:150, :] = (132, 142, 165)   # Brown
img[150:200, :] = (203, 192, 255) # Pink
img[200:250, :] = (128, 128, 128) # Gray
img[250:300, :] = (10, 128, 128)   # Olive

# Display the image
cv2.imshow("Different Colors", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
