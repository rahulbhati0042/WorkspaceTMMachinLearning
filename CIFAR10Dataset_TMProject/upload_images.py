from http.server import HTTPServer,BaseHTTPRequestHandler
import os
from os import listdir
from os.path import isfile, join
import io
import cv2
from keras.preprocessing.image import load_img

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/uploadImages'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write('upload Images'.encode())

        else:
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write('Hello Control'.encode())

    def do_POST(self):
         if self.path.endswith('/uploadImages'):
            content_length = int(self.headers['Content-Length'])
            body = (self.rfile.read(content_length)).decode('utf-8')
            
            files = os.listdir(body)
            
            for f in files:
                
                imagefile=os.path.join(body, f)
                print("filane name :",imagefile)
                imageData= cv2.imread(imagefile)
                print(imageData)
                #imagefile1=os.path.join("CIFAR10Dataset_TMProject/imgs/", f)
                #print("file name new :",imagefile1)
                cv2.imwrite("D:/RahulBhati/Machine_Learning_Data/ThinkingMachine/WorkspaceTMMachinLearning/CIFAR10Dataset_TMProject/imgs/"+f,imageData)
                            
            
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write('Post upload Images'.encode())
        
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


