import numpy as np
import matplotlib.pyplot as plt
numberOfSamples=3
numberOfFeature=2
numberOfOutputs=4
rateOfLearning = 0.0001
numberOfCycles = 10000
print(f"Number of samples {numberOfSamples}")
print(f"Number of features {numberOfFeature}")
print(f"Number of outputs {numberOfOutputs}")
print(f"Learning rate {rateOfLearning}")
print("="*50)

dataSetSize = (numberOfSamples,numberOfFeature)
print('dataSetSize :',dataSetSize)
np.random.seed(5949)
inputData = np.random.uniform(-10,10,dataSetSize)
print("input data : ",inputData)
print("Shape input data :",inputData.shape)
weights = np.random.uniform(-10,10,(dataSetSize[1],numberOfOutputs))
print("weights :",weights)
print("weights shape :",weights.shape)

expectedOutputData = np.matmul(inputData,weights)
print("expected output :",expectedOutputData)

neuralNetworkWeights = np.random.uniform(-5,5,(numberOfFeature,numberOfOutputs))
print('neuralNetworkWeights: ',neuralNetworkWeights)
print('neuralNetworkWeights shape: ',neuralNetworkWeights.shape)

someDataStructure = []
x = 1
while x <= numberOfCycles:
  neuralNetworkPredictions = np.matmul(inputData,neuralNetworkWeights)
  meanSquaredLoss=np.mean(np.square(expectedOutputData-neuralNetworkPredictions))
  someDataStructure.append(meanSquaredLoss)
  if x==1: print(f"Loss in first cycle {meanSquaredLoss}")
  deltaFactor = (neuralNetworkPredictions-expectedOutputData)/2
  deltaWeights = np.matmul(np.matrix.transpose(inputData),deltaFactor)
  neuralNetworkWeights=neuralNetworkWeights-(deltaWeights*rateOfLearning)
  x+=1
print(f"Loss after : {numberOfCycles} is {meanSquaredLoss}" )
print("Final weights to be userd")
print(neuralNetworkWeights)
plt.plot(someDataStructure)
plt.show()