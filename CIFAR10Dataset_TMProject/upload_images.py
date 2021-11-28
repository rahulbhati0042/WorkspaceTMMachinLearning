from http.server import HTTPServer,BaseHTTPRequestHandler
import os
import cv2
import tensorflow as tf

from keras.models import load_model
import numpy as np

class helloHandler(BaseHTTPRequestHandler):

    def do_POST(self):
         cifar_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

         if self.path.endswith('/uploadImages'):
            content_length = int(self.headers['Content-Length'])
            body = (self.rfile.read(content_length)).decode('utf-8')
            
            files = os.listdir(body)
            model =load_model('G:\ThinkingMachine\WorkspaceTMMachinLearning\CIFAR10Dataset_TMProject\model\my_first_model.h5')
 
            print('@@ Model loaded')
            dir_Response = {}
            for f in files:
                imagefile=os.path.join(body, f)
                print("filane name :",imagefile)
                imageData= cv2.imread(imagefile)
                cv2.imwrite("G:/ThinkingMachine/WorkspaceTMMachinLearning/CIFAR10Dataset_TMProject/imgs/"+f,imageData)
                #test_image = load_img("G:/ThinkingMachine/WorkspaceTMMachinLearning/CIFAR10Dataset_TMProject/imgs/"+f) # load image 
                print("@@ Got Image for prediction")
                predImageData=imageData.reshape(1,32*32*3)
                predImageData = (predImageData-np.mean(predImageData))/np.std(predImageData)
                pred = model.predict(predImageData) 
                print("Predicted Result :",pred)
                pred = np.argmax(pred)
                print("Predicted Data :",pred)
                print("Predicted Label:",cifar_classes[pred])
                dir_Response[f]=cifar_classes[pred]

            
                
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(dir_Response).encode())
        
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


