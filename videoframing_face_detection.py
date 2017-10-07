import cv2
import urllib2

"""
Baswaraj mamidgi
8-10-2017
"""

face_cascade = cv2.CascadeClassifier('/home/baswarajmamidgi/OpenCV/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')

file=open('videofilesurl.txt','r') #text file which contains all the urls see the format of text file

lines=file.readlines()
for line in lines:
    data=line.split(",")
    #print(data[0]+':'+data[1]) data[0] file name  and data[1] video file url

    response = urllib2.urlopen(data[1])
    with open(data[0]+'.webm', 'wb') as f:
        f.write(response.read())

    cap = cv2.VideoCapture(data[0]+'.webm')
    count = 0

    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in face:
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
