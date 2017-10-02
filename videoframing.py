import numpy as np
import cv2

"""
Baswaraj mamidgi
18-9-2017
"""



face_cascade = cv2.CascadeClassifier('cascade.xml')
eye_cascade = cv2.CascadeClassifier('/home/baswarajmamidgi/OpenCV/opencv-3.3.0/data/haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture("eyevideo.mp4")
count=0

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        """"
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            image=img[ey:ey+ew,ex:ex+eh]
            cv2.imwrite("frames/frame%d.jpg" % count, image)
            count += 1
        """

    cv2.imshow('img', img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
