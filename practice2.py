import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/practice_dataset_v2.csv")
he=dataset.head(3)

#checking the null values
nl=dataset.isnull().sum()

#filling the null vlaues
#age
dataset["age"]=dataset["age"].fillna(dataset["age"].mode()[0])
nl=dataset.isnull().sum()

#eudcation
dataset["education"]=dataset["education"].fillna(dataset["education"].mode()[0])
nl=dataset.isnull().sum()

#annual_income
dataset["annual_income"]=dataset["annual_income"].fillna(dataset["annual_income"].median())
nl=dataset.isnull().sum()

#cities
dataset["cities"]=dataset["cities"].fillna(dataset["cities"].mode()[0])
nl=dataset.isnull().sum()

#satisfaction_scores
dataset["satisfaction_scores"]=dataset["satisfaction_scores"].fillna(dataset["satisfaction_scores"].mode()[0])
nl=dataset.isnull().sum()

#seeing the dataset
he=dataset.head(3)

#handling the otliers
#using the iqr method(annual_income aur monthly_charges)
#ns.boxplot(x="annual_income",data=dataset)

#seeing the shape 
sh=dataset.shape
#(700, 13)

#finding the fitst quantile
q1=dataset["annual_income"].quantile(0.25)
#46799.1811281871

q3=dataset["annual_income"].quantile(0.75)
#65967.44530418387

#finding the iqr,min,max
iqr=q3-q1
min_range=q1-(1.5*iqr)
max_range=q3+(1.5*iqr)

#removing the outliers from dataset
dataset=dataset[dataset["annual_income"]<=max_range]
dataset=dataset[dataset["annual_income"]>=min_range]

#resenting the index
dataset = dataset.reset_index(drop=True)

#seeing the shape
sh=dataset.shape

#seeing the boxplot
#sns.boxplot(x="annual_income",data=dataset)

#ouliers removal of (monthly_charges)
#using the z-socre
#sns.boxplot(x="monthly_charges",data=dataset)

#no ouliers are present in monthly_charges

#coreelation of (total_spend)
dc=dataset.corr(numeric_only=True)[["total_spend"]]

#ploting the heatmap
#sns.heatmap(dc,annot=True)
#plt.show()

#one hot encoding (contract_types)
data=dataset[["contract_types"]]

#importing the one hot encoding
from sklearn.preprocessing import OneHotEncoder

#fiting the model
oc=OneHotEncoder(drop="first")
ar=oc.fit_transform(data)

#making the dataframe
df=pd.DataFrame(ar.toarray(),columns=oc.get_feature_names_out(["contract_types"]))

#seeing the dataframe
he=df.head(3)

#inserting the encoded columns
dataset=pd.concat([dataset,df],axis=1)

#seeing the dataset
he=dataset.head(3)

#Ordinal Encoding(education)
from sklearn.preprocessing import OrdinalEncoder

#seeing the unique values
un=dataset["education"].unique()

#setting the orders
data1=[["High School","Bachelors","Masters","PhD"]]

#fititng the model
on=OrdinalEncoder(categories=data1)

#replacing it with the original data
dataset['education']=dataset["education"]=on.fit_transform(dataset[["education"]])

#seeing the dataset
he=dataset.head(3)

#dummy variables(cities)
data3=dataset[["cities"]]
un=dataset["cities"].unique()

#making the dummy variables
inf=pd.get_dummies(data3,drop_first=True).astype("int")

#inseerting in dataset
dataset=pd.concat([dataset,inf],axis=1)

#seeing the dataset
he=dataset.head(3)

#StandardScaler and MinMaxScaler(annual_income and monthly_charges)
from sklearn.preprocessing import StandardScaler

#making the model and fit
ss=StandardScaler()
ss.fit(dataset[["annual_income"]])

ss1=StandardScaler()
ss1.fit(dataset[["monthly_charges"]])

#trnasforming the data
ss.transform(dataset[["annual_income"]])
ss1.transform(dataset[["monthly_charges"]])

#filling the data into original dataset
dataset["annual_income_ss"]=dataset["annual_income_ss"]=pd.DataFrame(ss.transform(dataset[["annual_income"]]),columns=['x'])
dataset["monthly_charges_ss"]=dataset["monthly_charges_ss"]=pd.DataFrame(ss1.transform(dataset[["monthly_charges"]]),columns=['x'])

#seeing the dataset
he=dataset.head(3)

#MinMaxScaler(annual_income and monthly_charges)
from sklearn.preprocessing import MinMaxScaler

#making the model and fit
mm=MinMaxScaler()
mm.fit(dataset[["annual_income"]])

mm1=MinMaxScaler()
mm1.fit(dataset[["monthly_charges"]])

#tranforming the data
mm.transform(dataset[["annual_income"]])
mm1.transform(dataset[["monthly_charges"]])

#filling the data in original dataset
dataset["annual_income_mm"]=dataset["annual_income_mm"]=pd.DataFrame(mm.transform(dataset[["annual_income"]]),columns=["x"])
dataset["monthly_charges_mm"]=dataset["monthly_charges_mm"]=pd.DataFrame(mm1.transform(dataset[["monthly_charges"]]),columns=["x"])

#seeing the dataset
he=dataset.head(3)

#Multiple Linear Regression for total_spend
#making the dependent and independent variable
x=dataset.drop(columns=["customer_id", "churn", "contract_types", "cities", "education", "annual_income", "monthly_charges", "age", "total_spend"])
y=dataset["total_spend"]

#importing the train and test split
from sklearn.model_selection import train_test_split

#making the train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#making the multiple linear model
from sklearn.linear_model import LinearRegression

#making the object
lr=LinearRegression()

#fitting the model
lr.fit(x_train,y_train)

#checking the score
sc=lr.score(x_test,y_test)*100
#85.10305258973439

#finding the m vlaue and c value
mv=lr.coef_
#[ 9.39996681e-01  6.59160824e+01  2.28644400e+01  7.31512417e+01
 #-4.78544358e+01  1.06878022e+02 -2.95145864e+01 -4.76866899e+01
 #-8.08321312e+01  2.16632942e+01 -2.11672585e+01  1.03184945e+03
 #-4.16862140e+00  3.00870156e+02]

cv=lr.intercept_
#-394.80486804826387

#predicting the output
pc=lr.predict(x_test)

#Rsquare,mse,mae,rmse
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

#making the solutions
ms=mean_squared_error(y_test,lr.predict(x_test))
#509308.4522144668

me=mean_absolute_error(y_test,lr.predict(x_test))
#[ 9.39996681e-01  6.59160824e+01  2.28644400e+01  7.31512417e+01
#-4.78544358e+01  1.06878022e+02 -2.95145864e+01 -4.76866899e+01
#8.08321312e+01  2.16632942e+01 -2.11672585e+01  1.03184945e+03
#-4.16862140e+00  3.00870156e+02]

rm=np.sqrt(mean_squared_error(y_test,lr.predict(x_test)))
#713.6584983130705

r_score=r2_score(y_test,lr.predict(x_test))
#0.851030525897343

#polynomial reggression
x1=dataset[["tenure_months"]]
y1=dataset["total_spend"]

#importing the model
from sklearn.preprocessing import PolynomialFeatures

#making the model
pf=PolynomialFeatures(degree=2)

#fitting the model
pf.fit(x1)
x1=pf.transform(x1)

#importing the train and test 
from sklearn.model_selection import train_test_split

#making the train and test
x_train1,x_test1,y_train1,y_test1=train_test_split(x1,y1,train_size=0.8,test_size=0.2,random_state=42)

#imporitng the linear library
from sklearn.linear_model import LinearRegression

#fititng the data for model
lr1=LinearRegression()
lr1.fit(x_train1,y_train1)

#checking the accuracy
sc1=lr1.score(x_test1,y_test1)*100
#52.00481247301661(on degree 2)

#making the graph of regression
#prd=lr1.predict(x1)
#plt.scatter(dataset["tenure_months"],dataset["total_spend"])
#plt.plot(dataset["tenure_months"],prd,c='red')
#plt.show()

#calculating the r2 and rmse
from sklearn.metrics import mean_squared_error,r2_score

#performing the calculation
rm1=np.sqrt( mean_squared_error(y_test1,lr1.predict(x_test1)))
#1280.9749762607287

r_score1=r2_score(y_test1,lr1.predict(x_test1))
#0.520048124730166

#logistic Regression
#making the dependent and independent varialbe
x2=dataset.drop(columns=["customer_id", "churn", "contract_types", "cities", "education", "annual_income", "monthly_charges", "age", "total_spend"])
y2=dataset["churn"]

#importing the train and test
from sklearn.model_selection import train_test_split

#making the train and test
x_train2,x_test2,y_train2,y_test2=train_test_split(x2,y2,test_size=0.2,train_size=0.8,random_state=42)

#importing the regression
from sklearn.linear_model import LogisticRegression

#fititng the model
lg=LogisticRegression(class_weight="balanced")
lg.fit(x_train2,y_train2)

#checking the prediction
sc2=lg.score(x_test2,y_test2)*100
#76.97841726618705

#confussion matrix
from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score

#making the matrix
cf=confusion_matrix(y_test2,lg.predict(x_test2))
#[[427   0]
#[128   1]]

#making the heatmap 
sns.heatmap(cf,annot=True)

#making the precsision score,recall socre,fi socre
pr=precision_score(y_test2,lg.predict(x_test2))*100
print(pr)

rc=recall_score(y_test2,lg.predict(x_test2))*100
print(rc)

f_score=f1_score(y_test2,lg.predict(x_test2))*100
print(f_score)