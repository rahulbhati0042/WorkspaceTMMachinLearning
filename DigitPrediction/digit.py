import cv2
import numpy
from PIL import Image,ImageFont, ImageDraw
imageSize = (50,50)
newImage = numpy.zeros((imageSize[1],imageSize[0],3))
print(newImage.shape)
r = 0
while r<10:
  c = 0
  while c<10:
    newImage[r][c][0]=0
    newImage[r][c][1]=0
    newImage[r][c][2]=0
    c+=1
  r+=1
imgPath = "DigitPrediction/assets/bg.jpg"
cv2.imwrite(imgPath,newImage) #retrun true false
listOfFonts = ['CarreOne','CarreTwo','CombinumeralsBold','CombinumeralsOGR','Crashnumberinggothic','Crashnumberingserif'
,'digital','digital_italic','digital_mono','digital_mono_italic','DigitalDisplayRegular','Handwritingg','KrFirstYearsDings'
,'Oswald-VariableFont']
color = 'rgb(255, 255, 255)' # white color
for f in listOfFonts:
  font = ImageFont.truetype('DigitPrediction/fonts/'+f+'.ttf', 30)
  for i in range(10):
      text = str(i)
      image = Image.open(imgPath)
      draw = ImageDraw.Draw(image)
      draw.text((0,30),text,fill=color, font = font)
      imgName='DigitPrediction/assets/'+text+'/'+f+'_'+text+'.JPG'
      image.save(imgName)
print('Done')
