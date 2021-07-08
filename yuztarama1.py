import cv2
cam = cv2.VideoCapture(0)
face_detection=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id = input("ID numarasını giriniz:")
sampleNum=0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        sampleNum=sampleNum+1
        cv2.imwrite("yuzler/Users."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('YUZ TARAMA',img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    elif sampleNum>20:
        break

cam.release()
cv2.destroyAllWindows()
