
import cv2
import numpy as np
import urllib
import serial
#url = "http://10.202.14.114:4747"
url = "http://10.202.14.114:4747/mjpegfeed"
#url = "http://192.168.42.129:8080/video"
#url = 0
from darkflow.net.build import TFNet
options = {
    'model' : './cfg/tiny-yolo.cfg',
    'load' : './bin/yolov2-tiny2019.weights',
    'threshold' : 0.3,
    'gpu' : 1
}
print("allo")
tfnet = TFNet(options)
#image = cv2.imread('image.jpg')
#res = tfnet.return_predict(image)
cap = cv2.VideoCapture(0)
color = [tuple(255*np.random.rand(3)) for _ in range(10)]
countP = 0
countC = 0
meanP = []
meanC = []
                      
Arduino_Serial = serial.Serial('/dev/ttyACM1',9600) 

while(True):
    
    ret,frame = cap.read()
    frame = cv2.resize(frame, (640, 480)) 
    
    
    cv2.circle(frame,(0,300), 63, (0,0,255), -1)
    predictions = tfnet.return_predict(frame)
    
    for res in predictions:
        
        tl = (res['topleft']['x'], res['topleft']['y'])
        br = (res['bottomright']['x'], res['bottomright']['y'])
        label = res['label']
        
        # if label == 'person':
        #     print('count P ', len(res['label']))
        # if label == 'car':
        #     print('count C ', len(res['label']))
        # confidence = res['confidence']
        
        
        if label == 'person':
            print(predictions)
            print(res['label'])
            countP = len(predictions)
        elif label is not 'person' :
           countP = 0
        if label == 'car':
            countC = len(predictions)
        elif label is not 'car':
            countC = 0
        
        if label == "person" or label == "car":
            
            frame = cv2.rectangle(frame,tl,br,(255,0,255),5)

            frame = cv2.putText(frame,label,tl,cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
            
    frame = cv2.putText(frame,"number of person : " + str(countP),(20,20),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    frame = cv2.putText(frame,"nbr of cars : " + str(countC),(30,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    if (countP > 3):                 
        Arduino_Serial.write(b'3')
    if (countP <= 0):                  
        Arduino_Serial.write(b'0')
    
    if (countP > 2):
        Arduino_Serial.write(b'2')
    if (countP >= 1):
        Arduino_Serial.write(b'1')
    if (countC > 1):
        Arduino_Serial.write(b'3')
    
    #frame = cv2.resize(frame, (1280, 720)) 
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
