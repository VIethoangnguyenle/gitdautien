from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense,Activation,Dropout,Flatten,MaxPooling2D,Conv2D
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential,save_model
from tensorflow.keras import backend as K
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.optimizers import Adadelta
# from tensorflow.keras.estimator 
#load data
(x_train,y_train) , (x_test,y_test) = mnist.load_data()

print(x_train.shape , y_train.shape)

x_train = x_train.reshape(x_train.shape[0],28,28,1)
x_test = x_test.reshape(x_test.shape[0],28,28,1)
inputShape = (28,28,1)

num_classes = 10
#convert class vectors to binary class matrices
y_train = to_categorical(y_train,num_classes=num_classes)
y_test = to_categorical(y_test,num_classes=num_classes)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255
x_test /= 255

print('x_train shape',x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

#create model
model = Sequential()
    #32 kernel, kernel size (3,3),strike = 1 => 26x26x32
model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape = inputShape))
    #64 kernel, kernel size (3,3) stride = 1 => 24x24x64
model.add(Conv2D(64,kernel_size=(3,3),activation='relu'))
    #23x23x64
model.add(MaxPooling2D(pool_size=(2,2)))
    #eliminate some connect
model.add(Dropout(0.2))
model.add(Flatten())
#create network
model.add(Dense(256,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes,activation='softmax'))

model.compile(loss=categorical_crossentropy,optimizer=Adadelta(),metrics=['accuracy'])

batch_size = 128
epochs = 12
model.fit(x_train,y_train,batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(x_test,y_test))
print("The model has successfully trained")
model.save('mnist.h5')
print("Saving the model as mnist.h5")
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

