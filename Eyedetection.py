import cv2

"""
Baswaraj mamidgi
21-9-2017
"""



eye_cascade = cv2.CascadeClassifier('data/cascade.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray,20,20)

    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'eye', (x, y), font, 0.5,(0,255,255),2,cv2.LINE_AA)


    cv2.imshow('img', img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
