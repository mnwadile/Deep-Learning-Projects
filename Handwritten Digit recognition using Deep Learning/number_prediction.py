import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras
 
import matplotlib.pyplot as plt
#%matplotlib inline

# To load dataset
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Length and shape of array
print(len(X_train))
print(len(X_test))
print(X_train[1].shape)
print(X_train[0])

# To plot arrray
plt.matshow(X_train[0])

# Value of digit
print(y_train[0])

# To normalize array
X_test = X_test / 255
X_train = X_train / 255

# value of array after normalizing
print(X_train[0])
plt.matshow(X_train[0])

# Flattening the array
X_train_flattened = X_train.reshape(len(X_train), 28*28)
X_test_flattened = X_test.reshape(len(X_test), 28*28)
print(X_test_flattened.shape)

#Deep learning model
model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(784,), activation='sigmoid')
    ])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train_flattened, y_train, epochs=5)

#To evaluate model
model.evaluate(X_test_flattened, y_test)

# To predict result
y_predicted = model.predict(X_test_flattened)
y_predicted[0]

plt.matshow(X_test[0])

np.argmax(y_predicted[0])

y_predicted_labels = [np.argmax(i) for i in y_predicted]
y_predicted_labels[:5]

# Confusion matrix
cm = tf.math.confusion_matrix(labels=y_test, predictions=y_predicted_labels)
print(cm)
 
# To plot confusion matrix
import seaborn as sn
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')

# Using flatten layer i.e without using X_train_flattened
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(10, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10)

model.evaluate(X_test,y_test)

print(model)

# To predict result
y_predicted = model.predict(X_test)
y_predicted[0]

plt.matshow(X_test[0])

np.argmax(y_predicted[0])

y_predicted_labels = [np.argmax(i) for i in y_predicted]
y_predicted_labels[:5]

# Confusion matrix
cm = tf.math.confusion_matrix(labels=y_test, predictions=y_predicted_labels)
print(cm)
 
# To plot confusion matrix
import seaborn as sn
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')






















