
## references a mix of
# https://www.youtube.com/watch?v=rKcwcARdg9M&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn&index=3 camera and video capture
# https://github.com/opencv/opencv/blob/master/samples/python/kmeans.py K-means clustering
# https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097 dominant color
# https://www.youtube.com/watch?v=ddSo8Nb0mTw&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn&index=6 color detection/threshold

import cv2
import numpy as np
from sklearn.cluster import KMeans


def getdominantColor(image, k=1):
    # immage becomes a single array
    pixels = image.reshape((-1, 3))
    
    # clustering the image (k=1 means just into one dominant)
    clt = KMeans(n_clusters=k)
    clt.fit(pixels)
    
    # return dominant color
    dominantColor = clt.cluster_centers_.astype(int)[0]
    return dominantColor

# video capture
cap = cv2.VideoCapture(0)

# dominant color window
cv2.namedWindow("Dominant Color", cv2.WINDOW_NORMAL)

while True:
    # frame dimentsions
    ret, frame = cap.read()
    height, width, _ = frame.shape
    #central rectangle
    x1, y1 = int(width * 0.25), int(height * 0.25)
    x2, y2 = int(width * 0.75), int(height * 0.75)
    roi = frame[y1:y2, x1:x2]

    # central rectangle with dominant color
    dominantColor = getdominantColor(roi)
    dominant_color_display = np.zeros((100, 100, 3), dtype=np.uint8)
    dominant_color_display[:, :] = dominantColor
    cv2.imshow("Dominant Color", dominant_color_display)

    cv2.imshow("Video Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()