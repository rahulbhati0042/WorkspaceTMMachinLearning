import sklearn.datasets
import numpy
import sklearn.svm
import sklearn.model_selection

digitData = sklearn.datasets.load_digits()
#print(digitData)
#print(len(digitData))
#print(type(digitData))
data = digitData.data
target = digitData.target
print(data)
print(type(data))
print(len(data))
print(data[0])
print(data[0].shape)
print(data.shape)
#print(target)
#print(type(target))
#print(len(target))
#print(target.shape)
#target_name= digitData.target_names
#print(target_name)
#description= digitData.DESCR
#print(description)
#print(digitData.images)
#print(digitData.images.shape)
#print(digitData.images[0])
totalImages = len(digitData.images)
print('*'*50)
print("total images")
print(totalImages)
sampleImage = digitData.images.reshape((totalImages,-1))
print('*'*50)
print(sampleImage)
#print(sampleImage)
print(sampleImage.shape)
print(sampleImage[0])
print(sampleImage[0].shape)

classified= sklearn.svm.SVC()
trainingData,testData,trainingTarget,testTarget= sklearn.model_selection.train_test_split(sampleImage,target,test_size=0.5)

#print(trainingData.shape)
#print(testData.shape)
#print(len(trainingData))
#print(len(testData))

classified.fit(trainingData,trainingTarget)
result = classified.predict(testData)
#print("Actula Result :",testTarget)
#print("Predicted Result :", result)