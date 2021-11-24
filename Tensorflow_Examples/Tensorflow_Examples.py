import tensorflow as tf
print(f"Tensor flow version :{tf.__version__}")
print(f"Tensor flow Keras Version :{tf.keras.__version__}")

if tf.executing_eagerly():
    print("Things are being executed in eagerly fashion")
else:
    print("Things are being executed in graph fashion")

print(f"If GPU is being used :{tf.test.is_gpu_available()}")


## Constants Example Variable
#Example-#2: Tensorflow Constants

a = tf.constant(10)
b = tf.constant(20)
c = tf.add(a,b)
print(c)
d = tf.subtract(c,a)
print(d)

# Arithmatic Operation

a = tf.Variable(10)
tf.print(a)
a.assign(20)
tf.print(a)
print(a)

b = tf.Variable(30)
c = tf.greater(b,a) # retrun 1 if greater then else 0
tf.print(c)

d = tf.constant(-40)
tf.print(tf.abs(d))

####### Mathematical Operation
#Example-#4: Mathematical Operation - Scaler, Vector, Matrix, shape, rank
import tensorflow as tf
a = tf.Variable(20)
b = tf.Variable([10,20])
c = tf.Variable([[10,20],[30,40]],dtype=tf.uint64)
tf.print("Scaler :",a)
tf.print("Vector :",b)
tf.print("Matrix :",c)
print(a)
print(b)
print(c)
print(a.shape)
tf.print(tf.rank(a))

#Tensor flow Operations -> with matrix, converting data type to another data type like numpy datatype, etc
import tensorflow as tf
a = tf.Variable([[[10,20,30],[40,50,60],[70,80,90],[100,110,120]]])
tf.print(a)
print(a.shape)
print("-"*50)
b = tf.reshape(a,[2,6])
tf.print(a)
print("-b-"*50)
tf.print(b)
print(b.shape)
k = b[1,2]
tf.print("k :",k)
print(k)
print("k.dtype :",k.dtype)
print(type(k))
k2 = k.numpy()
print(k2)
print(type(k2))
k3 = a.numpy()
print(k3)
print(type(k3))

#Example-#3: Ragged Function
a = tf.Variable([[10,20,30],[40,50,60],[70,80,90],[100,110,120]])
tf.print(a)
print(a.shape)

a = tf.ragged.constant([[10,20,30],[40,50,60],[70,80,90],[100,110,120]])
tf.print(a)
print(type(a))
