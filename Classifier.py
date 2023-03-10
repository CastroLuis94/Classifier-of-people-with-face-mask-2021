# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12rzHcMqsU7_nwME4t7aLQPFI9-edWVQD
"""

import zipfile
import io

from google.colab import drive
drive.mount('/content/drive')

zip_ref = zipfile.ZipFile("/content/drive/MyDrive/dataPTargentina/bien_puesto.zip", 'r')
zip_ref.extractall("/content/drive/MyDrive/dataPTargentina/")
zip_ref.close()

zip_ref = zipfile.ZipFile("/content/drive/MyDrive/dataPTargentina/mal_puesto.zip", 'r')
zip_ref.extractall("/content/drive/MyDrive/dataPTargentina/")
zip_ref.close()

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

dir_with = "/content/drive/MyDrive/dataPTargentina/bien_puesto"
dir_without ="/content/drive/MyDrive/dataPTargentina/mal_puesto"

with_array = []
without_array = []
img_size=100

print(os.listdir(dir_with))

print(os.listdir(dir_without))
for img in os.listdir(dir_with):
  img = cv2.imread(os.path.join(dir_with,img))
  img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  img_gray_resize = cv2.resize(img_gray,(img_size,img_size))
  with_array.append([img_gray_resize])


for img in os.listdir(dir_without):
  img = cv2.imread(os.path.join(dir_without,img))
  img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  img_gray_resize = cv2.resize(img_gray,(img_size,img_size))
  without_array.append([img_gray_resize])

print(len(with_array))
print(len(without_array))

dir_with = "/content/drive/MyDrive/dataPTargentina/bien_puesto"
dir_without ="/content/drive/MyDrive/dataPTargentina/mal_puesto"

with_array = []
without_array = []
img_size=100

i = 0
for img in os.listdir(dir_with):
  print(i , end=" ")
  print(img)
  dirtemp= '/content/drive/MyDrive/dataPTargentina/Wmask/'+ str(img)
  img = cv2.imread(os.path.join(dir_with,img))
  img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  img_gray_resize = cv2.resize(img_gray,(img_size,img_size))
  cv2.imwrite( str(dirtemp),img_gray_resize)
  #with_array.append([img_gray_resize])
  i=i+1

print("________________________________________________________")
i = 0
for img in os.listdir(dir_without):
  if (i >= 2578 ):
    print(i , end=" ")
    print(img)
    dirtemp= '/content/drive/MyDrive/dataPTargentina/WOmask/'+ str(img)
    img = cv2.imread(os.path.join(dir_without,img))
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_gray_resize = cv2.resize(img_gray,(img_size,img_size))
    cv2.imwrite( str(dirtemp),img_gray_resize)
    #without_array.append([img_gray_resize])
  i=i+1

dir_with = "/content/drive/MyDrive/dataPTargentina/Wmask"
dir_without ="/content/drive/MyDrive/dataPTargentina/WOmask"
with_array = []
without_array = []


i = 0
for img in os.listdir(dir_with):
  if ( i % 100 == 0):
    print(i , end=" ")
  img = cv2.imread(os.path.join(dir_with,img))
  img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  with_array.append([img_gray])
  i=i+1
i = 0
for img in os.listdir(dir_without):
  if ( i % 100 == 0):
    print(i , end=" ")
  img = cv2.imread(os.path.join(dir_without,img))
  img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  without_array.append([img_gray])
  i=i+1

print(len(with_array))
print(len(without_array))

x00 = np.array(with_array)
x01 = np.array(without_array[:9925])


print(x00.shape)
print(x01.shape)
print(x1.shape)
print(x2.shape)

x0 = x1[0]
for img in x1[:1]:
  print(img)
  x0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(x0)

datos_train = []
img_size=100
for item in x00:
  item = np.array(item).reshape(img_size,img_size,1)
  datos_train.append([item,1])

for item in x01:
  item = np.array(item).reshape(img_size,img_size,1)
  datos_train.append([item,0])

print(len(datos_train))
datos_train[0]

X=[]
Y=[]

for imag, tag in datos_train:
  X.append(imag)
  Y.append(tag)

X = np.array(X).astype(float)/255
Y = np.array(Y)

print(X[0])

import tensorflow as tf
from tensorflow import keras

modeloDenso = tf.keras.models.Sequential([
                                          tf.keras.layers.Flatten(input_shape=(100,100,1)),
                                          tf.keras.layers.Dense(150,activation='relu'),
                                          tf.keras.layers.Dense(150,activation='relu'),
                                          tf.keras.layers.Dense(1,activation='sigmoid')

])

modeloCNN = tf.keras.models.Sequential([
                                          tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(100, 100, 1)),
                                          tf.keras.layers.MaxPooling2D(2,2),
                                          tf.keras.layers.Conv2D(64,(3,3), activation='relu'),
                                          tf.keras.layers.MaxPooling2D(2,2),
                                          tf.keras.layers.Conv2D(128,(3,3), activation='relu'),
                                          tf.keras.layers.MaxPooling2D(2,2),
                                        
                                          tf.keras.layers.Flatten(),
                                        tf.keras.layers.Dense(100,activation='relu'),
                                        tf.keras.layers.Dense(1,activation='sigmoid')

])

modeloCNN2 = tf.keras.models.Sequential([
                                          tf.keras.layers.Conv2D(32,(3,3), activation='relu', input_shape=(100,100,1)),
                                          tf.keras.layers.MaxPooling2D(2,2),
                                          tf.keras.layers.Conv2D(64,(3,3), activation='relu'),
                                          tf.keras.layers.MaxPooling2D(2,2),
                                          tf.keras.layers.Conv2D(128,(3,3), activation='relu'),
                                          tf.keras.layers.MaxPooling2D(2,2),
                                        
                                          tf.keras.layers.Dropout(0.5),
                                          tf.keras.layers.Flatten(),
                                        tf.keras.layers.Dense(250,activation='relu'),
                                        tf.keras.layers.Dense(1,activation='sigmoid')

])

modeloDenso.compile(optimizer='adam', 
                    loss='binary_crossentropy',
                    metrics=['accuracy'])

modeloCNN.compile(optimizer='adam', 
                    loss='binary_crossentropy',
                    metrics=['accuracy'])


modeloCNN2.compile(optimizer='adam', 
                    loss='binary_crossentropy',
                    metrics=['accuracy'])

from tensorflow.keras.callbacks import TensorBoard
tensorBoardDenso = TensorBoard(log_dir='logs/denso')
modeloDenso.fit(X,Y, batch_size=32,
                validation_split=0.15,
                epochs=100,
                callbacks=[tensorBoardDenso])

tensorBoardCNN = TensorBoard(log_dir='logs/cnn')
modeloCNN.fit(X,Y, batch_size=32,
                validation_split=0.15,
                epochs=100,
                callbacks=[tensorBoardCNN])

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir logs/

tensorBoardCNN2 = TensorBoard(log_dir='logs/cnn2')
modeloCNN2.fit(X,Y, batch_size=32,
                validation_split=0.15,
                epochs=100,
                callbacks=[tensorBoardCNN2])

plt.figure(figsize=(15,9))
for i in range(20):
  plt.subplot(4,5,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.imshow(X[i].reshape(img_size,img_size), cmap="gray")

#Realizar el aumento de datos con varias transformaciones. Al final, graficar 10 como ejemplo
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=15,
    zoom_range=[0.7, 1.4],
    horizontal_flip=True,
    vertical_flip=True
)

datagen.fit(X)

plt.figure(figsize=(20,8))

for imagen, etiqueta in datagen.flow(X, Y, batch_size=10, shuffle=False):
  for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(imagen[i].reshape(100, 100), cmap="gray")
  break

modeloDenso_AD = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(100, 100, 1)),
  tf.keras.layers.Dense(150, activation='relu'),
  tf.keras.layers.Dense(150, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])

modeloCNN_AD = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(100, 100, 1)),
  tf.keras.layers.MaxPooling2D(2, 2),
  tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2, 2),
  tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2, 2),

  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(100, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])

modeloCNN2_AD = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(100, 100, 1)),
  tf.keras.layers.MaxPooling2D(2, 2),
  tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2, 2),
  tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2, 2),

  tf.keras.layers.Dropout(0.5),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(250, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])

modeloDenso_AD.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy'])

modeloCNN_AD.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy'])

modeloCNN2_AD.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy'])

X_entrenamiento = X[:17000]
X_validacion = X[17000:]

y_entrenamiento = Y[:17000]
y_validacion = Y[17000:]

data_gen_entrenamiento = datagen.flow(X_entrenamiento, y_entrenamiento, batch_size=32)

tensorboardCNN2_AD = TensorBoard(log_dir='logs/cnn2_AD')

modeloCNN2_AD.fit(
    data_gen_entrenamiento,
    epochs=100, batch_size=32,
    validation_data=(X_validacion, y_validacion),
    steps_per_epoch=int(np.ceil(len(X_entrenamiento) / float(32))),
    validation_steps=int(np.ceil(len(X_validacion) / float(32))),
    callbacks=[tensorboardCNN2_AD]
)

len(Y)*.85

modeloCNN2_AD.save('WWO_Mask-cnn-ad.h5')

!pip install tensorflowjs

!mkdir carpeta_salida

!tensorflowjs_converter --input_format keras WWO_Mask-cnn-ad.h5 carpeta_salida

!ls carpeta_salida/

dir_temp="/content/myTest"

array_temp =[]
for img in os.listdir(dir_temp):
  print(img)
  img = cv2.imread(os.path.join(dir_temp,img))
  img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  img_gray_resize = cv2.resize(img_gray,(img_size,img_size))
  array_temp.append([img_gray_resize])

for item in array_temp:
  plt.figure()
  plt.imshow(np.squeeze(item), cmap="gray")
  plt.colorbar()
  plt.grid(False)
  plt.show()

datos_myTest = []
for item in array_temp:
  item = np.array(item).reshape(img_size,img_size,1)
  if ( i == 0 or i==3):
    datos_myTest.append([item,0])
  else:
    datos_myTest.append([item,1])

XX=[]
YY=[]

for imag, tag in datos_myTest:
  XX.append(imag)
  YY.append(tag)

XX = np.array(XX).astype(float)/255
YY = np.array(YY)


modeloCNN2_AD.predict(XX)

tensorboardCNN_AD = TensorBoard(log_dir='logs-new/cnn_AD')

modeloCNN_AD.fit(
    data_gen_entrenamiento,
    epochs=150, batch_size=32,
    validation_data=(X_validacion, y_validacion),
    steps_per_epoch=int(np.ceil(len(X_entrenamiento) / float(32))),
    validation_steps=int(np.ceil(len(X_validacion) / float(32))),
    callbacks=[tensorboardCNN_AD]
)

modeloCNN2_AD.save('WWO_Mask-cnn0-ad.h5')
!mkdir carpeta_salida2
!tensorflowjs_converter --input_format keras WWO_Mask-cnn0-ad.h5 carpeta_salida2