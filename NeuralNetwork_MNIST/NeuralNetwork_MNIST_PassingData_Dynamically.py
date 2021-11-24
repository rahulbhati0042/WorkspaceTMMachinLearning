import mnist
import numpy as np
class Layer:
  def __init__(self,inputsize,layersize,activationFunction):
    self.weights = np.random.rand(inputsize,layersize)
    #print("weights :",self.weights,self.weights.shape)
    self.bias = layersize
    self.activationFunction= activationFunction
  def forward(self,x):
    z = np.dot(x,self.weights)+self.bias
    return self.activationFunction(z)

#Sigmoid Activation Function
def sigmoid(x):
  return 1/(1+np.exp(-x))

class NeuralNetwork:
  def __init__(self,inputsize,outputsize,size_of_hidden_layers):
    self.layersizes =[inputsize,*size_of_hidden_layers,outputsize]
    #print("LayerSize :",self.layersizes)
    self.layers= [Layer(self.layersizes[i],self.layersizes[i+1],sigmoid) for i in range(len(self.layersizes)-1)]

  def forward(self,x):
    
    for layer in self.layers:
      #print("Layers in loop Length :",len(x))
      x = layer.forward(x)
    return x;


mnist.temporary_dir = lambda: "NeuralNetwork_MNIST\dataset"
x_training_data,y_training_label = mnist.train_images(),mnist.train_labels()
x_test_data,y_test_label = mnist.test_images(),mnist.test_labels()

x_training_data =   x_training_data.reshape(-1,28*28)
#Flatton matrix to vector
x_test_data =   x_test_data.reshape(-1,28*28)

number_of_categories = 10
y_training_label = np.eye(number_of_categories)[y_training_label]

np.random.seed(60)
print(x_training_data.shape)
print(x_training_data.shape[1])
nn = NeuralNetwork(x_training_data.shape[1],number_of_categories,(100,50,20))
#dynamically passing data:
correct =0;
for i in range(len(x_test_data)):
  output = nn.forward(x_test_data[i])
  predictedClass = np.argmax(output)
  if predictedClass ==y_test_label[i]:
    correct +=1
  
print('-'*50)
print("correct count :",correct)
print('-'*50)
p = (correct /len(x_test_data))*100
print("count Percentage :",p)