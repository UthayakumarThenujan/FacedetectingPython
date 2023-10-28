import cv2
from random import randrange
import math

# load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(
    "C:\\Users\\Uthayakumar Thenujan\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
)

# Choose an image for the face detection
img = cv2.imread("E:\\Desktop(5.2.2023)\\Python\\Facedetection\\RDJ6.jpg")

# Conver color Graysal

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# FaceDetect coordinates
Face_Coordinates = trained_face_data.detectMultiScale(gray_img)
# FaceDetect coordinates Length
lenght_Face_Coordinates = len(Face_Coordinates)

# Rectangle
i = 0
min = 1000
while lenght_Face_Coordinates > i:
    j = 0
    (x, y, w, h) = Face_Coordinates[i]
    while lenght_Face_Coordinates - 1 > j:
        if j != i:
            (x1, y1, w1, h1) = Face_Coordinates[j]
            distance = math.sqrt(
                (((2 * x + w) / 2) - ((2 * x1 + w1) / 2)) ** 2
                + (((2 * y + h) / 2) - ((2 * y1 + h1) / 2)) ** 2
            )
            if min > distance:
                min = distance
                i1 = i
                j1 = j
                (xd, yd, wd, hd) = Face_Coordinates[i]
                (xd1, yd1, wd1, hd1) = Face_Coordinates[j]

        j = j + 1
    i = i + 1

count = 0
for x, y, w, h in Face_Coordinates:
    if (count == i1 or count == j1) and lenght_Face_Coordinates > 2:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
        cv2.putText(
            img,
            "Close",
            (x, y - 4),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )
        # cv2.line(img,(xd+wd,yd+hd),(xd1,yd1),(0,0,255),5)
    else:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    count = count + 1


cv2.imshow("First Face Detection", img)
cv2.waitKey()


print("Code Completed")
