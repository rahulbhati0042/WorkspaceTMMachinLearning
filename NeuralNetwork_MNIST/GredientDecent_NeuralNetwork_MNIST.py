import mnist
import numpy as np

class Layer:
  def __init__(self,inputsize,layerSize,activationFunction,derivatedActivationFunction):
    #ndarray with weight vlaues
    self.weights = np.random.standard_normal((inputsize,layerSize))
    #ndarray with bias value(which will be added to weighted sum)
    self.bias = np.random.standard_normal(layerSize)
    #number of neurons on layer
    self.size = layerSize
    #activation function
    self.activationFunction= activationFunction
    #derivated action function
    self.derivatedActivationFunction=derivatedActivationFunction
    #vector to store input data for backward propagation
    self.input = None
    #vector to store output data for backward propagation
    self.output = None
    #the derivative of the loss with respect to Weights
    self.derivatedWeights = None
    #the derivative of the loss with respect to Bias
    self.derivatedBias = None

  def forward(self,x):
    z = np.dot(x,self.weights)+self.bias
    self.output = self.activationFunction(z)
    self.input = x
    return self.output

  def backward(self,derivatedLoss): #derivated loss with respect to layers output
    #this function is for backpropagation
    # it will compute the necessary derivatives
    #will store the comuter derivatives
    #will return the derivated loss with respect to input for further backpropatation
    derivatedOutput= self.derivatedActivationFunction(self.output)
    deltaFactor = derivatedLoss*derivatedOutput
    oneVectorForBias=np.ones(derivatedLoss.shape[0])
    self.derivatedWeights=np.dot(self.input.T,deltaFactor)
    self.derivatedBias=np.dot(oneVectorForBias,derivatedLoss)
    derivatedLossWithRespectToInput=np.dot(deltaFactor,self.weights.T)
    return derivatedLossWithRespectToInput
  
  def updateParameters(self,rateOfLearning):
    self.weights=self.weights-(self.derivatedWeights*rateOfLearning)
    self.bias = self.bias - (self.derivatedBias*rateOfLearning)

  #sigmoid function
def sigmoid(x):
   return 1/(1+np.exp(-x))

def sigmoid_derivated(x):
   return x*(1-x)

def L2Loss(predicted,actual):
   return np.sum(np.square(predicted-actual))

def L2Loss_derivated(predicted,actual):
   return 2*(predicted-actual)

class NeuralNetwork:
  def __init__(self,inputsize,outputsize,size_of_hidden_layers,lossFunction,derivatedLossFunction):
    self.layersizes =[inputsize,*size_of_hidden_layers,outputsize]
    self.layers= [Layer(self.layersizes[i],self.layersizes[i+1],sigmoid,sigmoid_derivated) for i in range(len(self.layersizes)-1)]
    self.lossFunction=lossFunction
    self.derivatedLossFunction=derivatedLossFunction

  def forward(self,x):
    for layer in self.layers: x = layer.forward(x)
    return x;

  def backward(self,derivatedLoss):
    for layer in reversed(self.layers): #we need to go backwards derivatedLoss
        derivatedLoss = layer.backward(derivatedLoss)
    return derivatedLoss

  def updateParameters(self,rateOfLearning):
    for layer in self.layers:
      layer.updateParameters(rateOfLearning)

  def feedforward(self,inputData,actualOutputData):
    correct = 0 
    for e in range(len(inputData)):
        output = self.forward(inputData[e])
        predictedClass=np.argmax(output)
        if predictedClass == actualOutputData[e]: correct+=1
    return correct/len(inputData)

  def trainTheNetwork(self,input_data,actual_output_data,rateOfLearning,numberOfCycles,setsize,test_data,test_label):
    numberOfSplits = len(input_data) #setsize
    for e in range(numberOfCycles):
      for f in range(numberOfSplits):
        startIndex=f*setsize
        endIndex=startIndex+setsize
        dataSet=input_data[startIndex:endIndex]
        outputDataSet=actual_output_data[startIndex:endIndex]
        predictions=self.forward(dataSet)
        loss= self.lossFunction(predictions,outputDataSet)
        derivatedLoss=self.derivatedLossFunction(predictions,outputDataSet)
        self.backward(derivatedLoss)
        self.updateParameters(rateOfLearning)
      accurecy=self.processAccuracy(test_data,test_label)
      print(f"Cycle :{e+1}, Accuracy :{accurecy}%")
    return loss

  def processAccuracy(self,inputData,actualOutputData):
    correct=0
    for e in range(len(inputData)):
      output=self.forward(inputData[e])
      predictedClass=np.argmax(output)
      if predictedClass==actualOutputData[e]: correct+=1
    return (correct/len(inputData))*100


mnist.temporary_dir = lambda: "NeuralNetwork_MNIST\dataset"

x_training_data,y_training_label = mnist.train_images(),mnist.train_labels()
x_test_data,y_test_label = mnist.test_images(),mnist.test_labels()

x_training_data =   x_training_data.reshape(-1,28*28)
#Flatton matrix to vector
x_test_data =   x_test_data.reshape(-1,28*28)
number_of_categories = 10
y_training_label = np.eye(number_of_categories)[y_training_label]

lossDS=[]
np.random.seed(25)
nn = NeuralNetwork(x_training_data.shape[1],number_of_categories,(100,50,20),L2Loss,L2Loss_derivated)
#print(nn.feedforward(x_test_data,y_test_label)**100)
nn.trainTheNetwork(x_training_data,y_training_label,0.0001,500,64,x_test_data,y_test_label)
