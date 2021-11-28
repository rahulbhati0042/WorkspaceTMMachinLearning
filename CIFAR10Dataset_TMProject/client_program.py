import sys
import requests as req
from PIL import Image
from PIL import ImageDraw
import json
import re
import os
import PIL.Image
import matplotlib.font_manager


# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
# Arguments passed
print("\nName of Python script:", sys.argv[0])
listOfFonts = matplotlib.font_manager.win32InstalledFonts()[:1]
print("\nFolder path:", sys.argv[1])
savedPath="G:\ThinkingMachine\WorkspaceTMMachinLearning\CIFAR10Dataset_TMProject\predictedImg"
print("\nPredicted Image Folder Path :",savedPath)
resp = req.request(method='POST', url="http://localhost:1001/uploadImages", data = sys.argv[1])
test=re.sub('\'','\"',resp.text)
dir = json.loads(test)

for key, value in dir.items():
    imgPath = os.path.join(sys.argv[1],key)
    img = Image.open(imgPath)
    toolBox = PIL.ImageDraw.Draw(img)
    x, y = 0,25
    font = PIL.ImageFont.truetype("G:\ThinkingMachine\WorkspaceTMMachinLearning\CIFAR10Dataset_TMProject\OpenSans-Bold.ttf", size=7)
    w, h = font.getsize(value)
    xx = 32-(x + w)
    toolBox.rectangle((xx, y, xx + w, y + h), fill='white')

    toolBox.text((xx, 22), value, fill='black',font=font)
    img.save(os.path.join(savedPath,value+"_"+key))
