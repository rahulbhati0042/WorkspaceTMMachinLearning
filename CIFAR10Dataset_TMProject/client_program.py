import sys
import requests as req
from PIL import Image
from PIL import ImageDraw
import json
import re
import os
import PIL.Image
import base64
import json 

URL = "http://localhost:1001/uploadImages"

def imageProcessing(result):
    print("@ Image Processing...")
    for key, value in result.items():
        imgPath = os.path.join(sys.argv[1],key)
        img = Image.open(imgPath)
        toolBox = PIL.ImageDraw.Draw(img)
        x, y = 0,25
        font = PIL.ImageFont.truetype("OpenSans-Bold.ttf", size=7)
        w, h = font.getsize(value)
        xx = 32-(x + w)
        toolBox.rectangle((xx, y, xx + w, y + h), fill='white')
        toolBox.text((xx, 22), value, fill='black',font=font)
        img.save(os.path.join("PredictedImage",value+"_"+key))

def uploadImage(imgPath,imgName):
    with open(imgPath, 'rb') as f:
        im_bytes = f.read() 
    im_b64 = base64.b64encode(im_bytes).decode("utf8")
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = json.dumps({"image": im_b64,"filename" : imgName})
    response = req.request("POST",  url=URL,  data=payload, headers=headers)
    return response

def main():


    #Arguments passed - input folder path
    uploadFolderPath=sys.argv[1]
    print("@ Folder path:", uploadFolderPath)
    files = os.listdir(uploadFolderPath)
    for file in files:
        imgPath = os.path.join(uploadFolderPath,file)
        print("Image Path :",imgPath)
        rs = uploadImage(imgPath,file)
        print("@ Response :", rs.text)
        result=re.sub('\'','\"',rs.text)
        result = json.loads(result)
        imageProcessing(result)


if __name__ == '__main__':
    main()

