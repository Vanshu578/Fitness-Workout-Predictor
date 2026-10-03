import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/Titanic-Dataset.csv")
he=dataset.head(3)

#seeing the null vlaues
nl=dataset.isnull().sum()
#age=177,cabin=687,embarked=2

#seeing the shape
sh=dataset.shape
#(891, 12)

#seeing the duplicated row
dc=dataset.duplicated().sum()
#0

#describing the dataset
ds=dataset.describe()

#seeing the datatypes
inf=dataset.info()

#filling the null values
dataset["Age"]=dataset["Age"].fillna(dataset["Age"].mode()[0],inplace=True)
dataset["Embarked"]=dataset["Embarked"].fillna(dataset["Embarked"].mode()[0],inplace=True)
dataset.drop(columns=["Cabin","Name","PassengerId","Ticket"],inplace=True)

#seeing the dataset
nl=dataset.isnull().sum()
he=dataset.head(3)

#seeing the outliers
sns.boxplot(x="Age",data=dataset)#massive ouliners

sns.boxplot(x="Fare",data=dataset)#massive ouliners

sns.boxplot(x="Parch",data=dataset)#little outliers"

#encoding the dataset
from sklearn.preprocessing import OneHotEncoder

#making the model
data=dataset[["Sex","Embarked"]]
oh=OneHotEncoder(drop="first")
ar=oh.fit_transform(data)
df=pd.DataFrame(ar.toarray(),columns=oh.get_feature_names_out(["Sex","Embarked"]))

#inserting in original dataset
dataset=pd.concat([dataset,df],axis=1)

#making the train and test
x=dataset.drop(columns=["Survived","Sex","Embarked"])
y=dataset["Survived"]

#importing the train and test
from sklearn.model_selection import train_test_split

#making the train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#making a model(linear regression)
sns.heatmap(data=dataset.corr(numeric_only=True),annot=True)

#imporitng the model
from sklearn.linear_model import LinearRegression

#making the model
lr=LinearRegression()
lr.fit(x_train,y_train)

#checking the score
sc=lr.score(x_test,y_test)*100
#44.135662311626

#imporitng random forest classifier
from sklearn.ensemble import RandomForestClassifier

x1=dataset.drop(columns=["Survived","Sex","Embarked"])
y1=dataset["Survived"]

x_train1,x_test1,y_train1,y_test1=train_test_split(x1,y1,test_size=0.2,train_size=0.8,random_state=42)

#making the random forest classifier
rc=RandomForestClassifier(max_depth=5,min_samples_split=2,n_estimators=100)
rc.fit(x_train1,y_train1)

#checking the socre
sc1=rc.score(x_test1,y_test1)*100
#81.56424581005587(before)
#81.56424581005587(after)

#hyper perameter tunning
from sklearn.model_selection import GridSearchCV

#making the perameters(random forest regression)
df1={'n_estimators': [50, 100, 200],'max_depth': [None, 5, 10, 15],'min_samples_split': [2, 5]}

#making the model
gd1=GridSearchCV(RandomForestClassifier(random_state=42),param_grid=df1)
gd1.fit(x_train1,y_train1)

#seeing the best parameters
pc1=gd1.best_params_
#{'max_depth': 5, 'min_samples_split': 2, 'n_estimators': 100}

#seeing the score
sc4=gd1.best_score_
#0.8356544863587118

#making the prediction
prd=rc.predict(x_test1)
result=pd.DataFrame({'prediction':prd,'Actual':y_test1.values})

#making x and y
x2=dataset.drop(columns=["Survived","Sex","Embarked"])
y2=dataset["Survived"]

#making the train and test
x_train2,x_test2,y_train2,y_test2=train_test_split(x2,y2,test_size=0.2,train_size=0.8,random_state=42)

#imporintg the model
from sklearn.linear_model import LogisticRegression

#mqaking the model
lc=LogisticRegression(C=1,max_iter=500,solver='liblinear')
lc.fit(x_train2,y_train2)

#checking the model
pr1=lc.score(x_test2,y_test2)*100
#79.88826815642457

#hyper perameter tunning
from sklearn.model_selection import GridSearchCV

#making the perameter(logistic regression)
df2={'C': [0.01, 0.1, 1, 10, 100],'solver': ['liblinear', 'lbfgs'],'max_iter': [500, 1000]}

#making the model
gd2=GridSearchCV(LogisticRegression(random_state=42),param_grid=df2)
gd2.fit(x_train2,y_train2)

#seeing the best peramameter
pc2=gd2.best_params_
#{'C': 1, 'max_iter': 500, 'solver': 'liblinear'}
#seeing the best socre
sc5=gd2.best_score_
#0.7977149610952428

#making the prediction
prd1=lc.predict(x_test2)
result1=pd.DataFrame({'prediction':prd1,'Actual':y_test2.values})

#making the decession tree
x3=dataset.drop(columns=["Survived","Sex","Embarked"])
y3=dataset["Survived"]

#imporing the scaller
from sklearn.preprocessing import StandardScaler

#making the model
sc=StandardScaler()
sc.fit(x3)
x3=pd.DataFrame(sc.transform(x3),columns=x3.columns)

#making the train and test
x_train3,x_test3,y_train3,y_test3=train_test_split(x3,y3,test_size=0.2,train_size=0.8,random_state=42)

#importing the model
from sklearn.tree import DecisionTreeClassifier

#making the object and fit
dt=DecisionTreeClassifier(criterion="entropy",max_depth=3,splitter='best')
dt.fit(x_train3,y_train3)

#checking the score
sc2=dt.score(x_test3,y_test3)*100
#76.53631284916202(before)
#79.88826815642457(after)

#making the prediction
prd2=dt.predict(x_test3)
result2=pd.DataFrame({'prediction':prd2,'Actual':y_test3.values})

#hyper perameter tunning
from sklearn.model_selection import GridSearchCV

#making the parameters
df={"criterion": ["gini", "entropy"],"splitter": ["best", "random"],"max_depth":[i for i in range(2,20)]}

#making model and fit
gd=GridSearchCV(DecisionTreeClassifier(),param_grid=df)
gd.fit(x_train3,y_train3)

#seeing the best parameter
pc=gd.best_params_

#best socre
sc3=gd.best_score_

#making the prediction
prd3=rc.predict(x_test3)
result3=pd.DataFrame({'prediction':prd3,'Actual':y_test3.values})

#making the model prediction graphs
models=['LinearRegression','logistic regression','DessionTree','RandomForest']
score=[44.14,pr1,sc2,sc1]
plt.bar(models,score,color=['orange','blue','green','red'])
plt.xlabel('Models')
plt.ylabel('Score')
plt.title('Model Comparison')
plt.ylim(0,100)
plt.show()    