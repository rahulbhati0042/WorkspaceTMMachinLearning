from genericpath import samefile
from http.server import HTTPServer,BaseHTTPRequestHandler
import os
import cv2
import tensorflow as tf
import json
import base64
import PIL.Image as Image
import io

from keras.models import load_model
import numpy as np

class helloHandler(BaseHTTPRequestHandler):

    def saveImg(self,request):
        print("@ Saveimg function calling...")
        img_bytes = base64.b64decode(request['image'].encode('utf-8'))
        # convert bytes data to PIL Image object
        image = Image.open(io.BytesIO(img_bytes))
        imgFile=os.path.join("rowimages",request["filename"])
        image.save(imgFile)
        return self.predictImg(imgFile,request["filename"])

    def predictImg(self,imgFile,filename):
        print("@ predictImg funciton calling...")
        print("@ Image Path :",imgFile)
        imageData= cv2.imread(imgFile)
        predImageData=imageData.reshape(1,32*32*3)
        predImageData = (predImageData-np.mean(predImageData))/np.std(predImageData)
        pred = self.model.predict(predImageData) 
        print("@ Predicted Result :",pred)
        pred = np.argmax(pred)
        print("@ Predicted Data :",pred)
        print("@ Predicted Label:",self.cifar_classes[pred])
        dir_Response = {}
        dir_Response[filename]=self.cifar_classes[pred]
        return dir_Response

    def do_POST(self):
         self.cifar_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog',
          'frog', 'horse', 'ship', 'truck']
         self.model =load_model('model\my_first_model.h5')
 
         print('@@ Model loaded')
         if self.path.endswith('/uploadImages'):
            content_length = int(self.headers['Content-Length'])
            
            request = (self.rfile.read(content_length))
            dir = json.loads(request)
            predictedResult = self.saveImg(dir) 
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(predictedResult).encode())
        
         else:
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write('Post Hello Control'.encode())

def main():
    PORT = 1001
    server = HTTPServer(('',PORT),helloHandler)
    print("Server running on :",PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()


