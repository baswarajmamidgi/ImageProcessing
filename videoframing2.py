

import numpy as np
import cv2

"""
Baswaraj mamidgi
18-9-2017
"""

eye_cascade = cv2.CascadeClassifier('/media/baswarajmamidgi/YGU8FT/cascade.xml')

cap = cv2.VideoCapture('/media/baswarajmamidgi/YGU8FT/videoplayback.mp4')
count = 0

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        image = img[y:y+h,x:x+w]
        #cv2.imwrite("frames/frame%d.jpg" % count, image)
        count += 1

    cv2.imshow('img', img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
