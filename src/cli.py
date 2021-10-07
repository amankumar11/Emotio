import argparse
import os
import cv2
import sys
from flask import Flask, render_template, url_for,redirect
from face_api import *
from emotion_value import *
from video_verify import *
import glob
import enquiries

app = Flask(__name__)

def checkImage(path): # function to check if the opened file is valid or not 
    if path=='':
        return
    ext = os.path.splitext(path)
    allowedExtensionsImage = ['.jpg', 'png', '.jpeg', '.mp4', '.wav']

    if not ext[1] in allowedExtensions:
        print("\033[36m wrong or no file found r\n")
        raise Exception(
            " \033[44m \033[01m   incorrect extension given " + ext[1])


os.system(" cat ./static/assets/logo.txt | lolcat") # outputs the magnus logo
sys.stdout.flush()


parser = argparse.ArgumentParser(
    prog='PROG', usage='%(prog)s [options]',
    description='\033[32m Program to find the music playlist based on the highest scoring emotion in the passed image/video visit docx for more info:   https://google.com ')

parser.add_argument(
    '--cli', help='\033[31m  output data to the command prompt only')
args = parser.parse_args()

path = ''
options = ['Path to saved Image', 'Path to saved video ', 'webcam-feed']
choice = enquiries.choose('Choose one of these options: ', options)
if enquiries.confirm('continue with the selected option ?'):
    pass

print(choice)
param=False
if choice == "Path to saved Image":
    path = input("enter the path ...... r\n  ->")
    param =True
elif choice == "Path to saved video ":
    path = input("enter the path ...... r\n  ->")
    param=True
checkImage(path)

def val():
    return emotionArr(emomtionRet(path, param))
    

