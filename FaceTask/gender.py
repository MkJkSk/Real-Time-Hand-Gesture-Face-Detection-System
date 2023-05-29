from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np

def main():
    face_classifier=cv2.CascadeClassifier('haarcascades_models/haarcascade_frontalface_default.xml')
    gender_model = load_model('gender_model_50epochs.h5')

    gender_labels = ['Male', 'Female']

    wCam, hCam = 1200, 680
    cap=  cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    while True:
        ret,frame=cap.read()
        labels=[]

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)    
        faces=face_classifier.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray=gray[y:y+h,x:x+w]
            roi_gray=cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

            #Gender
            roi_color=frame[y:y+h,x:x+w]
            roi_color=cv2.resize(roi_color,(200,200),interpolation=cv2.INTER_AREA)
            gender_predict = gender_model.predict(np.array(roi_color).reshape(-1,200,200,3))
            gender_predict = (gender_predict>= 0.5).astype(int)[:,0]
            gender_label=gender_labels[gender_predict[0]] 
            gender_label_position=(x,y+h+50)
            cv2.putText(frame,gender_label,gender_label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            
        cv2.imshow('Gender', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()