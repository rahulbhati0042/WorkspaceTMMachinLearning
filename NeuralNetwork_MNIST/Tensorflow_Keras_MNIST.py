import tensorflow as tf
numberOfCategories = 10
numberOfRows = 28
numberOfColumns = 28
numberOfChannels = 1

inputshape = (numberOfRows,numberOfColumns,numberOfChannels)
(x_train,y_train),(x_test,y_test) = tf.keras.datasets.mnist.load_data()
#print(x_train.shape)
#print(y_train.shape)
#print(x_test.shape)
#print(y_test.shape)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128,activation="relu"))
model.add(tf.keras.layers.Dense(numberOfCategories,activation="softmax"))

model.compile(optimizer="sgd",loss="sparse_categorical_crossentropy",metrics=['accuracy'])

model.fit(x_train,y_train,epochs=10,verbose = 1,validation_data=(x_test,y_test))
model.summary()