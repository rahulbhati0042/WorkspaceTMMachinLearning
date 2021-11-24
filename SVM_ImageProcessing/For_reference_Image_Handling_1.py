import cv2
#Read image
imageData= cv2.imread("SVM_ImageProcessing/assets/color1.jpg")
print(imageData)
print(type(imageData))
print(imageData.shape)
print(imageData[0][0])

#Write image - black and withe - Now we will convert image into greyscale (means back end white).
for r in range(imageData.shape[0]):
    for c in range(imageData.shape[1]):
        rgb =imageData[r][c]
        red = int(rgb[0])
        gree = int(rgb[1])
        blue = int(rgb[2])
        average = int((red+gree+blue)/3)
        imageData[r][c]=(average,average,average)
        #print(imageData[r][c])
cv2.imwrite("SVM_ImageProcessing/assets/color1_blackAndwhite.jpg",imageData)