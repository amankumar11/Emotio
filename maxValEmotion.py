from flask import jsonify

def maxEmotioVal(obj):
    dict={}
    
    dict["anger"]=float(obj[0]["faceAttributes"]["emotion"]["anger"])
    dict["contempt"]=float(obj[0]["faceAttributes"]["emotion"]["contempt"])
    dict["sadness"]=float(obj[0]["faceAttributes"]["emotion"]["sadness"])
    dict["happiness"]=float(obj[0]["faceAttributes"]["emotion"]["happiness"])
    dict["surprise"]=float(obj[0]["faceAttributes"]["emotion"]["surprise"])
    return valueRet(dict)
    
def emotionArr(obj):
    dict=maxEmotioVal(obj)
    arr=[0,0,0,0,0]
 

    arr[0]=(float(obj[0]["faceAttributes"]["emotion"]["anger"]))
    arr[1]=(float(obj[0]["faceAttributes"]["emotion"]["contempt"]))
    arr[2]=(float(obj[0]["faceAttributes"]["emotion"]["sadness"]))
    arr[3]=(float(obj[0]["faceAttributes"]["emotion"]["happiness"]))
    arr[4]=(float(obj[0]["faceAttributes"]["emotion"]["surprise"]))
    return arr



def get_key(my_dict,val):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "NONE"

def display(dict):
    for x in dict:
        print(x)



def valueRet(dict):
    max =0.0;
    maxEmot=dict["anger"]

    for val in dict:
        # print(dict[val])        
        if(float(dict[val])>max):
            max=dict[val]
    
    return get_key(dict,max)
