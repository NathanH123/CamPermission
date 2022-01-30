from tkinter import Frame
import cv2
import time
import random

start_time = time.time() 
 
def takeSnapshot():
    number = random.randint(0,100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame= videocaptureobject.read()
        imagename = "Picture"+ str(number)+".png"
        cv2.imwrite(imagename, frame)
        start_time = time.time
        result = False
    return imagename
    videocaptureobject.release()
    cv2.destoryAllWindows()
takeSnapshot()