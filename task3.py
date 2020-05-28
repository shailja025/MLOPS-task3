#!/bin/bash
import sys
i=int(sys.argv[1])
def main(i):
   from keras.layers import Convolution2D 
   from keras.layers import MaxPooling2D
   from keras.layers import Dense
   from keras.layers import Flatten
   from keras.models import Sequential
   from keras.preprocessing.image import ImageDataGenerator
   print("import successfully")
   model=Sequential()
   pool=(2,2)
   model.add(Convolution2D(filters=32,
                            kernel_size=(3,3),
                            input_shape=(224,224,3)))
   model.add(MaxPooling2D(pool_size=(2,2)))  
   for j in range(1,i+1):
        pool=(2,2)
        if i > 3:
            pool=(1,1)
        model.add(Convolution2D(filters=32,
                  kernel_size=(3,3),
                  activation='relu'))
        model.add(MaxPooling2D(pool_size=pool))
   model.add(Flatten())
   model.add(Dense(units=128, activation='relu'))
   for j in range(4,i):
           model.add(Dense(units=128,activation='relu'))
   model.add(Dense(units=1,activation='sigmoid'))
   model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
    
   train_datagen = ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
   test_datagen = ImageDataGenerator(rescale=1./255)
   training_set = train_datagen.flow_from_directory('/code_test/Dataset/',
                  target_size=(224, 224),
                  batch_size=20,
                  class_mode='binary')
   test_set = test_datagen.flow_from_directory('/code_test/Dataset/',
                  target_size=(224, 224),
                  batch_size=20,
                  class_mode='binary')
                   
   result= model.fit(training_set,
                  steps_per_epoch=20,
                  epochs=i,
                  validation_data=test_set,
                  validation_steps=20)        
   model.summary()
   accuracy=result.history['accuracy'][-1]*100
   print("current accuracy=", accuracy)
   sys.stdout=open("a.txt","w")
   print(int(result.history['accuracy'][-1]*100))
   sys.stdout.close()
   
main(i)
