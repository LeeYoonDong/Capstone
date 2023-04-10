import os
import cv2
import numpy as np
#xml for face recognition
face_classifier = cv2.CascadeClassifier('/Users/dev/PycharmProjects/pythonProject/CvLbtTest/venv/haarcascade_frontalface_default.xml')
#Lower recognition rate, use "haarcascade_frontalface_extended"
# when object shooting resolution decreases

#Function that returns only face parts in the entire picture
def face_extractor(img):

    #Black and white treatment
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #FindFaceUse the detect of face_classifier.
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    #cant find face, return to None.
    if len(faces) == 0:
        return None

    #found face, get the x,y,w,h values
    #and process x,y is the lower left point.
    for(x,y,w,h) in faces:

        # Crop as much as face size and cut it in
        # If more than one face is detected, only the last face is left.
        cropped_face = img[y:y+h, x:x+w]
    #crop 한 얼굴사진을 리턴
    return cropped_face



cap = cv2.VideoCapture(0)

#img PATH
if not os.path.exists('/Users/dev/PycharmProjects/pythonProject/CvLbtTest/faces/s1'):
    os.makedirs('/Users/dev/PycharmProjects/pythonProject/CvLbtTest/faces/s1')
if not os.path.exists('/Users/dev/PycharmProjects/pythonProject/CvLbtTest/faces/s2'):
    os.makedirs('/Users/dev/PycharmProjects/pythonProject/CvLbtTest/faces/s2')
if not os.path.exists('/Users/dev/PycharmProjects/pythonProject/CvLbtTest/faces/s3'):
    os.makedirs('/Users/dev/PycharmProjects/pythonProject/CvLbtTest/faces/s3')
#Image count variable to save

slist = [1,2,3]
for i in slist:
    count = 0
    while True:

        #Take 1 picture
        ret, frame = cap.read()

        #Get a cropped face picture using the face detection
        if face_extractor(frame) is not None:
            count+=1

        #Resize the face image size to size 200×200
            face = cv2.resize(face_extractor(frame),(200,200))
        #Convert adjusted images into black and white pictures
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        #saved faces/user#.jpg
        # 윈도우즈에서 실행시 경로지정
           # file_name_path = 'training_data/s%d/user'%i+str(count)+'.jpg'
            file_name_path = '/Users/dev/PycharmProjects/pythonProject/CvLbtTest/faces/s%d/user%d.jpg' % (i, count)
           # file_name_path = '/Users/dev/PycharmProjects/pythonProject/CvLbtTest/faces/s%d' % i + str(count) + '.jpg'
            cv2.imwrite(file_name_path, face)




            #Display the face and the current number saved on the screen
            cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow('Face Cropper',face)
        else:
            print("Face not Found")
            pass

        if cv2.waitKey(1)==27 or count==100:
            break

cap.release()
cv2.destroyAllWindows()
print('Complete!!!')

