import cv2
import string
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import matplotlib.font_manager
import numpy as np

import numpy
import sklearn.svm
import sklearn.model_selection

listOfFonts = matplotlib.font_manager.win32InstalledFonts()[:1]
exclude = ['webdings','wingding','WINGDNG2','WINGDNG3','symbol','segmdl2','REFSPCL','OUTLOOK','MTEXTRA','holomdl2','BSSYM7']

imagesList=[]
imgPath = "TextRecognition/assets/"

for f in listOfFonts:
  image = PIL.Image.new('RGB',(1664,192),color=(0,0,0))
  toolBox = PIL.ImageDraw.Draw(image)
  font = PIL.ImageFont.truetype(f, size=30)
  y=0
  x=0
  for i in range(10):
       toolBox.text((y,x),str(i), font = font)
       y +=64
  x+=64
  y=0     
  for j in string.ascii_lowercase:
      toolBox.text((y,x),str(j),fill='rgb(255,255,255)', font = font)
      y +=64
  x+=64
  y=0     
  for u in string.ascii_uppercase:
      toolBox.text((y,x),str(u),fill='rgb(255,255,255)', font = font)
      y +=64
  x+=64
  if(f.endswith(".ttf") or f.endswith(".TTF")):
      f=f[f.rindex("\\")+1:f.rindex(".")]
      e =True
      for ff in exclude:
          if(f ==ff):
              e= False
              print("exclude :",ff)
              break;
      if e :
          imgName=imgPath+f+'.png'
          image.save(imgName)
          imagesList.append(f+'.png')
          print('Image Saved :',f)

dataList=[]
#targetDataStatic=[
#'0','1','2','3','4','5','6','7','8','9','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@','@',
#'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
#'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
#]
targetDataStatic=['0','1','2','3']
targetList=[]
for img in imagesList:
    i=0
    imageData= cv2.imread(imgPath+img)
    for r in range(0,64,64):
        for c in range(0,256,64):
            d = imageData[r:r+64,c:c+64]
            dataList.append(d)
    
    for t in targetDataStatic:
        targetList.append(t)
           
totalImages = len(dataList)
sampleImage = dataList[0].reshape((totalImages,-1))

classified= sklearn.svm.SVC()
trainingData,testData,trainingTarget,testTarget= sklearn.model_selection.train_test_split(sampleImage,targetList,test_size=0.5)

print(trainingData)
print(testData)
print(trainingTarget)
print(testTarget)

classified.fit(trainingData,trainingTarget)
result = classified.predict(testData)
print("Actula Result :",testTarget)
print("Predicted Result :", result)




   

