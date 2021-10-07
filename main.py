from flask import Flask, render_template, url_for, redirect
from cli import *
import time
import webbrowser
import threading
app = Flask(__name__)

emotionVAl=val()
sys.path.insert(1, './src/')
# emotionVAl=[1,1,1,1,0]



@app.route('/')
def upload_file():
    return render_template('index.html', log=emotionVAl)

progressMeter = "[#######"
completionMeter = "[###################################################"  # 51

for i in range(100):
    if (i == 1 or i == 10 or i == 30):
        time.sleep(0.6)
    print('\r'+progressMeter, end='')
    time.sleep(0.15)
    if(i == 25):
        time.sleep(1.5)

    progressMeter += '#'
    if progressMeter == completionMeter:
        break

print(']')

def appRUN():
    print("opening server .....")
    progressMeter = "[#######"
    completionMeter = "[#####################"  # 51

    for i in range(100):


        print('\r'+progressMeter, end='')
        time.sleep(0.2)
       
        progressMeter += '#'
        if progressMeter == completionMeter:
            break
    app.run()

def openWindow():
    time.sleep(5)
    webbrowser.open_new('http://127.0.0.1:5000/')
 
t1 = threading.Thread(target=appRUN)
# t2 = threading.Thread(target=openWindow)
t1.start()
# t2.start()
t1.join()
# t2.join()




