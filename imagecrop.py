import os
import cv2


def resize_files():
    files=os.listdir("/home/baswarajmamidgi/PycharmProjects/vision/joint_pos")

    count=0
    for file in files:

        try:
            img=cv2.imread("/home/baswarajmamidgi/PycharmProjects/vision/joint_pos/"+file,cv2.IMREAD_GRAYSCALE)
            image=cv2.resize(img,(20,20))

            cv2.imwrite("/home/baswarajmamidgi/PycharmProjects/vision/joint_new_pos/pos"+str(count)+".jpg",image)
            count+=1
        except Exception as e:
            print(str(e))

    print count


def create_bgn():
    for file in os.listdir('/home/baswarajmamidgi/PycharmProjects/vision/joint_neg'):

        name='joint_neg/'+file+'\n'
        with open('bg_joint.txt','a') as f:
            f.write(name)


def create_bg():
    for file in os.listdir('/home/baswarajmamidgi/PycharmProjects/vision/joint_pos'):
        print file

        name='joint_pos/'+file+' 1 0 0 20 20\n'
        with open('info_joint.txt','a') as f:
            f.write(name)


create_bgn()
create_bg()