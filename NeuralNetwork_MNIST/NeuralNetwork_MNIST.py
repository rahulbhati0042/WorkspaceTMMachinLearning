import mnist
import numpy as np
class Layer:
  def __init__(self,inputsize,layersize,activationFunction):
    self.weights = np.random.rand(inputsize,layersize)
    print("weights :",self.weights,self.weights.shape)
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
    print("LayerSize :",self.layersizes)
    self.layers= [Layer(self.layersizes[i],self.layersizes[i+1],sigmoid) for i in range(len(self.layersizes)-1)]

  def forward(self,x):
    
    for layer in self.layers:
      print("Layers in loop Length :",len(x))
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
output_dataset = nn.forward(x_training_data[0])

print("Output Data Set : What our network produced")
print(output_dataset)
print("what was expected : ",y_training_label[0])
print(output_dataset==y_training_label[0])

print("-"*50)
print(x_test_data.shape)
print(y_test_label.shape)
print("-"*50)
#print(x_test_data[0])
print("-"*50)
print(y_test_label[0])
print("-"*50)
#print(x_test_data[1])
print("-"*50)
print(y_test_label[1])