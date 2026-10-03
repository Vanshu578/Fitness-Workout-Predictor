#single layer perception
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.plotting import plot_decision_regions

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/placement.csv")
he=dataset.head(3)

#seeing the graph of linearity
#sns.scatterplot(x="cgpa",y="iq",data=dataset,hue="placement")

#making the depednet andi indepedent variable
x=dataset.iloc[:,:-1]
y=dataset["placement"]

#imporitng the train and test
from sklearn.model_selection import train_test_split

#making the train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=10)

#importing the perceptron model
from sklearn.linear_model import Perceptron

#making the model
pr=Perceptron()
pr.fit(x_train,y_train)

#checking the score
sc=pr.score(x_train,y_train)*100,pr.score(x_test,y_test)*100
print(sc)

#making the decisison region
plot_decision_regions(x.to_numpy(),y.to_numpy(),clf=pr)
plt.show()"""

#multilayer perception 
"""from keras.src.regularizers import L2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/Churn_Modelling.csv")
he=dataset.head(3)

#droping the columns
dataset.drop(["RowNumber","CustomerId","Surname","Geography","Gender"],axis=1,inplace=True)

#seeing the null values
nl=dataset.isnull().sum()

#making the dependent and independent variable
x=dataset.iloc[:,:-1]
y=dataset["Exited"]

#performing the scalling of x
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
ss.fit_transform(x)

#creating the dataframe
x=pd.DataFrame(ss.fit_transform(x),columns=x.columns)

#importing the transorflow
import tensorflow
from keras.layers import Dense
from keras.models import Sequential

#chckeing the shape
sh=x.shape
#(10000, 8)

#imporitng the batch normalization 
from keras.layers import Dense,BatchNormalization,Dropout

#making the models and layers
ann=Sequential()
ann.add(Dense(6,input_dim=8,activation="relu",kernel_regularizer=L2(l2=0.01)))
ann.add(Dense(5,activation="relu"))
ann.add(Dense(4,activation="relu"))
ann.add(Dense(3,activation="relu"))
ann.add(Dense(2,activation="relu"))
ann.add(Dense(1,activation="sigmoid"))

#compiling the layers
ann.compile(optimizer='adam',loss="binary_crossentropy",metrics=['accuracy'])

#importing the tran and test
from sklearn.model_selection import train_test_split

#making the train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#seeing the shape of x_train
(x_train.shape)
#(8000, 8)

#making the graph
#importing the callbacks
from keras.callbacks import EarlyStopping

#importing the callback

#making the model and fit
hc=ann.fit(x_train,y_train,batch_size=100,epochs=50,validation_data=(x_test,y_test),callbacks=EarlyStopping())

#checking history
history_dict=hc.history

#train and testing accuracy
train_accuracy=history_dict["accuracy"]
test_accuracy=history_dict["val_accuracy"]

#importing the callbacks
from keras.callbacks import EarlyStopping

#checking the data into 0 and 1
prd=ann.predict(x_test)

#performing the loop
prd_data=[]
for i in prd:
    if i[0]>0.5:
        prd_data.append(1)
    else:
        prd_data.append(0)

#importing the accuracy
from sklearn.metrics import accuracy_score

#checking the score
#x_test
sc=accuracy_score(y_test,prd_data)*100
#80.35 (when the epoch is 10)

#x_train
prd1=ann.predict(x_train)

#performing the loop
prd_data1=[]
for i in prd1:
    if i[0]>0.5:
        prd_data1.append(1)
    else:
        prd_data1.append(0)

#checking the accuracy
sc1=accuracy_score(y_train,prd_data1)*100"""

#making the convutional netwrok
"""import tensorflow
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten
from keras.models import Sequential

#making model
cnn=Sequential()

#imporitng the conv2d and making layers
cnn.add(Conv2D(32,(3,3),input_shape=(64,64,3),activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2,2)))
cnn.add(Conv2D(16,(3,3),activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2,2)))
cnn.add(Flatten())

#making the ann network
cnn.add(Dense(64,activation='relu'))
cnn.add(Dense(32,activation='relu'))
cnn.add(Dense(16,activation='relu'))
cnn.add(Dense(8,activation='relu'))
cnn.add(Dense(4,activation='relu'))
cnn.add(Dense(1,activation='sigmoid'))

#compiling the model
cnn.compile(loss='binary_crossentropy',optimizer="adam")

#importing the image data generator
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#making the generators
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'C:/Users/User/Desktop/Train_Data',
        target_size=(64,64),
        batch_size=32,
        class_mode='binary')

test_generator = test_datagen.flow_from_directory(
        'C:/Users/User/Desktop/Test_Data',
        target_size=(64,64),
        batch_size=32,
        class_mode='binary')

cnn.fit(
        train_generator,
        epochs=15,
        validation_data=test_generator)

#imporintg the image for prediction
from keras.preprocessing import image
img=image.load_img("C:/Users/User/Desktop/cat_image1.jpg",target_size=(64,64))

#converting the img to array
img=image.img_to_array(img)
img=img/255.0

#flatten the image
import numpy as np
img=np.expand_dims(img,axis=0)

#predicting the data
p=cnn.predict(img)
print(p)

#loop for prediction
if p[0][0]<0.5:
    print("cat")
else:
    print("Dog")"""