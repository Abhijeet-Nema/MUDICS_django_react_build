from django.shortcuts import render

# Create your views here.
import numpy as np
from keras.models import load_model
import cv2
from keras.preprocessing import image
from keras_preprocessing.image import img_to_array
from time import sleep
import statistics as st
from mudics.settings import BASE_DIR
face_classifier = cv2.CascadeClassifier(r"C:\Mudic\core\haarcascade_frontalface_default.xml")
classifier =load_model(r"C:\Mudic\core\h.h5")

class expression:
    def detection(self):
        
        emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral',  'Surprise','Sad']

        cap = cv2.VideoCapture(0)
        output=[]

        count=0
        while (count<30):
            _, frame = cap.read()
            labels = []
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray)
    
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
                roi_gray = gray[y:y+h,x:x+w]
                roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
        
                if np.sum([roi_gray])!=0:
                    roi = roi_gray.astype('float')/255.0
                    roi = img_to_array(roi)
                    roi = np.expand_dims(roi,axis=0)
                    prediction = classifier.predict(roi)[0]
                    label=emotion_labels[prediction.argmax()]
                    label_position = (x,y)
                    cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                    output.append(label)
            
                else:
                    cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                count+=1
        
            cv2.imshow('Emotion Detector',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        final_output = st.mode(output)
        return final_output

