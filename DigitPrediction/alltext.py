import cv2
import string
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
listOfFonts = ['Handwritingg','Oswald-VariableFont']
image = PIL.Image.new('RGB',(500,50),color=(0,0,0))
toolBox = PIL.ImageDraw.Draw(image)
text=''
y=0
for f in listOfFonts:
  font = PIL.ImageFont.truetype('DigitPrediction/fonts/'+f+'.ttf', 15)
  
  for i in range(10):
      text = text+str(i)
  for j in string.ascii_lowercase:
      text = text+str(j)
  for k in string.ascii_uppercase:
      text = text+str(k)

  toolBox.text((0,y),text+"\n",fill='rgb(255,255,255)', font = font)
  text=''
  y= y+15
imgName='DigitPrediction/alltext.JPG'
image.save(imgName)
print('Image Saved')
