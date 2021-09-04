import os
import time
import cv2
from face_api import *
from maxValEmotion import *


def emomtionRet(path, param):
    if param:
        cap = cv2.VideoCapture(path)
        while (True):
            ret, frame = cap.read()
            if ret:
                cv2.imwrite("img.jpg", frame)
                break
        path = 'img.jpg' #'
        return image_response(path)
    elif  path  =='':  # tis a WEBCAM FEED
        channel = int(input("\033[44m enter 0 if you want to use built-in webcam r\n \033[36m 1 if you want to use "
            "external "))
        print("\033[42m \033[34m video capturing .....\033[0m")
        cap = cv2.VideoCapture(channel)
        if not cap.isOpened():
            print("\033[41m video stream not found ..")
            return None
        else:
            while (True):
                ret, frame = cap.read()
                cv2.imwrite("img.jpg",frame)
                break
        path='img.jpg'
        return image_response(path)
    else :# video path is given 
        val=  input("\033[43m trying to read from a video continue [Y/N]")
        if(val=='Y' or val=='y'):
            cap=cv2.VideoCapture(path)
            while(True):
                ret, frame = cap.read()
                if ret :
                    cv2.imwrite("img.jpg", frame)
                    break
                else:
                    print(" file not found terminating ...")
                    return None
        else :
            return None
        path = 'img.jpg'
        return image_response(path)
            

