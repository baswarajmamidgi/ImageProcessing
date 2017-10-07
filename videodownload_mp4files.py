import cv2
import requests

"""
Baswaraj mamidgi
8-10-2017
"""

face_cascade = cv2.CascadeClassifier('/media/baswarajmamidgi/YGU8FT/cascade.xml')

file=open('videofilesurl.txt','r')

lines=file.readlines()
for line in lines:
    data=line.split(",")
    #print(data[0]+':'+data[1]) data[0] file name  and data[1] video file url

    response = requests.get(data[1], stream=True)
    with open(data[0]+'.mp4', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)

    cap = cv2.VideoCapture(data[0]+'.mp4')
    count = 0

    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        eyes = face_cascade.detectMultiScale(gray, 1.1, 5)

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
