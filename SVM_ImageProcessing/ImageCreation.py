import PIL.Image
import PIL.ImageDraw

image = PIL.Image.new('RGB',(300,300),color=(40,100,190))
toolBox = PIL.ImageDraw.Draw(image)
toolBox.text((50,40),"Thinking Machines",fill=(255,255,255))
image.save("tm.png")
