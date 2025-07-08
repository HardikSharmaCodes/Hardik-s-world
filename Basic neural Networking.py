import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

(xtrain, ytrain) , (xtest, ytest) = keras.datasets.mnist.load_data()

xtrain = xtrain.reshape(-1,784)/255
xtest = xtest.reshape(-1,784)/255

model = keras.Sequential([

layers.Dense(392, activation = "relu", input_shape =(784,)),
layers.Dense(128, activation = "relu",),
layers.Dense(64, activation = "relu",),
layers.Dense(10, activation = "softmax")

])

model.compile(
    optimizer= "adam",
    loss= "sparse_categorical_crossentropy",
    metrics=['accuracy']
)

model.fit(xtrain, ytrain, epochs= 10, batch_size=32)
testloss, testAccuracy= model.evaluate(xtest,ytest)
print(f"test accuracy: {testAccuracy}")
prediction = model.predict(xtest[:1])
predicted_digit = np.argmax(prediction)
print(f"The model predicts this digit is: {predicted_digit}")
