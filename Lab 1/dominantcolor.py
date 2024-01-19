
## references a mix of
# https://github.com/opencv/opencv/blob/master/samples/python/kmeans.py K-means clustering
# https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097 Dominant Color
# https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html camera setup

import cv2
import numpy as np
from sklearn.cluster import KMeans

# Function to get dominant color using KMeans
def get_dominant_color(image, k=1):
    # Reshape the image to a flattened array of pixels
    pixels = image.reshape((-1, 3))
    # Use KMeans to cluster the pixels
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    # Get the dominant color
    dominant_color = kmeans.cluster_centers_.astype(int)[0]
    return dominant_color

# Open video capture
cap = cv2.VideoCapture(0)

# Create a new window for displaying the dominant color
cv2.namedWindow("Dominant Color", cv2.WINDOW_NORMAL)

while True:
    # Read frame from the video feed
    ret, frame = cap.read()

    # Get the dimensions of the frame
    height, width, _ = frame.shape

    # Define the central rectangle coordinates (adjust as needed)
    x1, y1 = int(width * 0.25), int(height * 0.25)
    x2, y2 = int(width * 0.75), int(height * 0.75)

    # Extract the central rectangle
    roi = frame[y1:y2, x1:x2]

    # Get the dominant color in the central rectangle
    dominant_color = get_dominant_color(roi)

    # Display the dominant color in a separate window
    dominant_color_display = np.zeros((100, 100, 3), dtype=np.uint8)
    dominant_color_display[:, :] = dominant_color
    cv2.imshow("Dominant Color", dominant_color_display)

    # Display the original video feed
    cv2.imshow("Video Feed", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()