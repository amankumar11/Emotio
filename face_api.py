import requests
import json
from flask import jsonify


def image_response(path):
    key = '904a6a032d1642908cadf606221da745'
    url = "https://akshit.cognitiveservices.azure.com/face/v1.0/detect"
    params = {"returnFaceAttributes": "emotion"}
    headers = {
        'content-type': "application/octet-stream",
        'Ocp-Apim-Subscription-Key': "904a6a032d1642908cadf606221da745"}

    path_image = path
    with open(path_image, 'rb') as f:
        data = f.read()
    response = requests.request(
        "POST", url, data=data, headers=headers, params=params)
    data = response.json()
    # print (data)
    return data

                                                                                                                                        


if __name__ == '__main__':
    image_response('image_example.jpg')
