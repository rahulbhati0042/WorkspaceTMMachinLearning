import cv2
import string
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import matplotlib.font_manager
import numpy as np

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
for img in imagesList:
    i=0
    imageData= cv2.imread(imgPath+img)
    print(imageData)
    print(imageData.shape)
    print(imageData[0])
    print(imageData[0].shape)
    
    for j in imageData:
        dataList.append(j)

i=0
for d in dataList:
    if i==0:
        m = np.matrix(d)
    else:
        m = np.vstack([m, d])
    i=i+1
np.savetxt("matrixData",m)
dataSet=[]
dataSet.append(("data",m))
#print(dataSet)
#print(dataSet[0].reshape(1664,192))
