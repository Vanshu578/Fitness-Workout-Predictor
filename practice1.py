import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/customer_churn_practice.csv")
he=dataset.head(3)

#checking the null vlaues
nl=dataset.isnull().sum()

#filling the null vlaues
#age
dataset["age"]=dataset["age"].fillna(dataset["age"].mean())
nl=dataset.isnull().sum()

#catogorical data fill with mode

#city
dataset["city"]=dataset["city"].fillna(dataset["city"].mode()[0])
nl=dataset.isnull().sum()

#catogorical data fill with mode

#education
dataset["education"]=dataset["education"].fillna(dataset["education"].mode()[0])
nl=dataset.isnull().sum()

#catogorical data fill with mode

#annual_income
dataset["annual_income"]=dataset["annual_income"].fillna(dataset["annual_income"].median())
nl=dataset.isnull().sum()

#median to be fill in the contuinues data

#satisfaction_score
dataset["satisfaction_score"]=dataset["satisfaction_score"].fillna(dataset["satisfaction_score"].mode()[0])
nl=dataset.isnull().sum()

#data is in 1,2,3,4 format so mode is a right choice 

#iqr and z score (annual_income and monthly_charges)
sh=dataset.shape
#(615, 15)

#seeing the ouliers present in it
#sns.boxplot(x="annual_income",data=dataset)
#lt.show()
#outliers are present in "annual_income"

#sns.boxplot(x="monthly_charges",data=dataset)
#ouliers are present

#Using IQR
#quartile 1
q1=dataset["annual_income"].quantile(0.25)
q1_mc=dataset["monthly_charges"].quantile(0.25)

#quartlie 3
q3=dataset["annual_income"].quantile(0.75)
q3_mc=dataset["monthly_charges"].quantile(0.75)

#finding the iqr,min,max
iqr=q3-q1
min_range=q1-(1.5*iqr)
max_range=q3+(1.5*iqr)

iqr_mc=q3_mc-q1_mc
min_range_mc=q1_mc-(1.5*iqr_mc)
max_range_mc=q3_mc+(1.5*iqr_mc)

#removing the ouliers
new_dataset=dataset[dataset["annual_income"]<=max_range]
sh1=new_dataset.shape
#(605, 15)

new_dataset1=dataset[dataset["monthly_charges"]<=max_range_mc]
sh2=new_dataset1.shape
#(611, 15)

#boxplot diagrame after removing the ouliers
#sns.boxplot(x="annual_income",data=new_dataset)


#sns.boxplot(x="monthly_charges",data=new_dataset1)


#taking the z score method
min_range_z=dataset["annual_income"].mean()-(3*dataset['annual_income'].std())
max_range_z=dataset["annual_income"].mean()+(3*dataset["annual_income"].std())

min_range_z1=dataset["monthly_charges"].mean()-(3*dataset["monthly_charges"].std())
max_range_z1=dataset["monthly_charges"].mean()+(3*dataset["monthly_charges"].std())

#removing the outliers
new_dataset2=dataset[dataset["annual_income"]<=max_range_z]
new_dataset3=dataset[dataset["monthly_charges"]<=max_range_z1]
sh3=new_dataset2.shape,new_dataset3.shape
#((609, 15), (611, 15))

#making the boxplot
#sns.boxplot(x="annual_income",data=new_dataset2)
#plt.show()

#sns.boxplot(x="monthly_charges",data=new_dataset3)
#plt.show()

#phase 2
#contract_type using One-Hot Encoding
#education using Ordinal Encoding
#city using dummy variables while actively avoiding the Dummy Variable Trap

#one-hot encoding
#imporitng the encoder
from sklearn.preprocessing import OneHotEncoder

#seeting the column
en_data=dataset[["contract_type"]]

#making the object
ohe=OneHotEncoder(drop='first')
ar=ohe.fit_transform(en_data)

#making the dataframe
df=pd.DataFrame(ar.toarray(),columns=ohe.get_feature_names_out(["contract_type"]))

#checking the dataset
he1=df.head(3)

#inserting the encoded column 
dataset=pd.concat([dataset,df],axis=1)

#deleteing the old column
dataset=dataset.drop(columns=["contract_type"])

#oridnal encoding("education")
un=dataset["education"].unique()
#['Bachelors', 'Masters', 'High School', 'PhD']

#seeitng the order
en_daat_ord=[["High School","Bachelors","Masters","PhD"]]

#geting the library
from sklearn.preprocessing import OrdinalEncoder

#giving the setted order
oen=OrdinalEncoder(categories=en_daat_ord)

#replacing it with the original dataset
dataset['education']=dataset['education']=oen.fit_transform(dataset[["education"]])

#seeing the dataset
he=dataset.head(10)

#dummy variables(city)
en_data_dm=dataset[["city"]]

#dummy variables
dm=pd.get_dummies(en_data_dm,drop_first=True).astype("int")

#inserting the data in original dataset
dataset=pd.concat([dataset,dm],axis=1)

#droping the city column
dataset=dataset.drop(columns=["city"])

#showing the dataset
he=dataset.head(5)

#Standardization (StandardScaler) and Normalization (MinMaxScaler) on annual_income, monthly_charges, and age
#Standardization on annual_income, monthly_charges, and age
#importnig the library
from sklearn.preprocessing import StandardScaler

#fititng the model
ss=StandardScaler()
ss.fit(dataset[["annual_income"]])

ss1=StandardScaler()
ss1.fit(dataset[["monthly_charges"]])

ss2=StandardScaler()
ss2.fit(dataset[["age"]])

#making the results fiot into the original dataset
dataset["annual_income_ss"]=dataset["annual_income_ss"]=pd.DataFrame(ss.transform(dataset[["annual_income"]]),columns=['x'])
dataset["monthly_charges_ss"]=dataset["monthly_charges_ss"]=pd.DataFrame(ss1.transform(dataset[["monthly_charges"]]),columns=['x'])
dataset["age_ss"]=dataset["age_ss"]=pd.DataFrame(ss2.transform(dataset[["age"]]),columns=['x'])

#seeing the dataset
he=dataset.head(3)

#normalization
#importing the library
from sklearn.preprocessing import MinMaxScaler

#fiiting the model
ms=MinMaxScaler()
ms.fit(dataset[["annual_income"]])

ms1=MinMaxScaler()
ms1.fit(dataset[["monthly_charges"]])

ms2=MinMaxScaler()
ms2.fit(dataset[["age"]])

#making the results fiot into the original dataset
dataset["annual_income_mm"]=dataset["annual_income_mm"]=pd.DataFrame(ms.transform(dataset[["annual_income"]]),columns=['x'])
dataset["monthly_charges_mm"]=dataset["monthly_charges_mm"]=pd.DataFrame(ms1.transform(dataset[["monthly_charges"]]),columns=['x'])
dataset["age_mm"]=dataset["age_mm"]=pd.DataFrame(ms2.transform(dataset[["age"]]),columns=['x'])

#seeing the dataset
he=dataset.head(3)

#corelation matrix (total_spend)
inf=dataset.info()
print(inf)

#performing the corelation
dc=dataset.corr(numeric_only=True)[["total_spend"]]

#seeing the graph
#plt.figure(figsize=(10,5))
#sns.heatmap(dc,annot=True)

#(Covariance vs. Correlation)
#tenure_months and total_spend
dc1=dataset["total_spend"].cov(dataset["annual_income"])

#seeing the graph
#sns.heatmap(dc1,annot=True)

#train and test split
from sklearn.model_selection import train_test_split

#dependent and independent
x=dataset.drop(columns=["customer_id","churn","signup_date","gender","annual_income","monthly_charges","age"])
y=dataset["churn"]

#making the train and test 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#checking the shape
sh4=x_train,y_train.shape
#[492 rows x 19 columns], (492,))
sh5=x_test,y_test.shape
#[123 rows x 19 columns], (123,))

#simple linear regression
x1=dataset[["monthly_charges_ss"]]
y1=dataset["total_spend"]

#importing tyhe train and test
from sklearn.model_selection import train_test_split

#making the train and test
x_train1,x_test1,y_train1,y_test1=train_test_split(x1,y1,train_size=0.8,test_size=0.2,random_state=42)

#importing the linear regression
from sklearn.linear_model import LinearRegression

#making the model and fit
lr=LinearRegression()
lr.fit(x_train1,y_train1)

#checking the score
ls=lr.score(x_test1,y_test1)*100

#taking the mse,mae,rmse
from sklearn.metrics import mean_absolute_error,mean_squared_error

#mse
mn=mean_squared_error(y_test1,lr.predict(x_test1))
#mae
me=mean_absolute_error(y_test1,lr.predict(x_test1))
#rmse
rm=np.sqrt(mean_squared_error(y_test1,lr.predict(x_test1)))

#checking the result
#373605304.1513807

#14715.615515740452

#19328.87229383496

#Multiple Linear Regression for total_spend. Report R² and Adjusted R². Why is Adjusted R² better when adding features
#multiple linear model
from sklearn.linear_model import LinearRegression

#making the x and y
x2=dataset.drop(columns=["customer_id","churn","signup_date","gender","annual_income","monthly_charges","age","total_spend"])
y2=dataset["total_spend"]

#importing the train and test split
from sklearn.model_selection import train_test_split

#making the train and test
x_train2,x_test2,y_train2,y_test2=train_test_split(x2,y2,test_size=0.2,train_size=0.8,random_state=42)

#making the multilnear model
lr1=LinearRegression()
lr1.fit(x_train2,y_train2)

#checking the score
lr_sc=lr1.score(x_test2,y_test2)*100,lr1.score(x_train2,y_train2)*100
#(92.17690147305771, 90.38208293253528)

#making the mse,mae,rmse
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

#mse
ms1=mean_squared_error(y_test2,lr1.predict(x_test2))
#print(ms1)#28552530.187892426

#mae
ma1=mean_absolute_error(y_test2,lr1.predict(x_test2))
#print(ma1)#4038.023752007118

#rmse
rm1=np.sqrt(mean_squared_error(y_test2,lr1.predict(x_test2)))
#5343.456763920938

#r2
y_pred=lr1.predict(x_test2)
rsq= r2_score(y_test2,y_pred)
#0.921769014730577

#(Polynomial Regression)
#Polynomial Regression (Degree 2 and Degree 3) on tenure_months $\rightarrow$ total_spend.
#making the dependent and independent varialbe
x3=dataset[["tenure_months"]]
y3=dataset["total_spend"]

#importing the library
from sklearn.preprocessing import PolynomialFeatures
pf=PolynomialFeatures(degree=3)

#fit and transform
pf.fit(x3)
x3=pf.transform(x3)

#imporitng the train and test
from sklearn.model_selection import train_test_split

#making the train and test
x_train3,x_test3,y_train3,y_test3=train_test_split(x3,y3,test_size=0.2,train_size=0.8,random_state=42)

#imporintg the linear library
from sklearn.linear_model import LinearRegression

#fitting the data and model
lr2=LinearRegression()
lr2.fit(x_train3,y_train3)

#checking the model accuracy
lr_sc1=lr2.score(x_test3,y_test3)*100
#84.52619194846069 (on dgree 2)
#84.26686500950193 (on  degree 3)

#making the coef(m value) and intercept(c vlaue)
mv=lr2.coef_
#[  0.         776.40769939   1.1900733 ](on degree 2)
#[ 0.00000000e+00  9.48081378e+02 -5.33685909e+00  6.23643587e-02] (on degree 3)
mv1=lr2.intercept_
#724.5606409059801(on degree 2)
#-185.81077944008211 (on degree 3)

#Logistic Regression model to predict the binary target churn
x4=dataset.drop(columns=["customer_id","churn","signup_date","gender","annual_income","monthly_charges","age","total_spend"])
y4=dataset["churn"]

#importing the model
from sklearn.model_selection import train_test_split

#making the train and test
x_train4,x_test4,y_train4,y_test4=train_test_split(x4,y4,train_size=0.8,test_size=0.2,random_state=42)

#importing the model and fiting it
from sklearn.linear_model import LogisticRegression

#fititng the model
lr3=LogisticRegression()
lr3.fit(x_train4,y_train4)

#checking the socre
lr_sc2=lr3.score(x_train4,y_train4)*100
#90.2439024390244

#confussin matrix
#imporitng the library
from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score

#making the conffusion matrix
cn=confusion_matrix(y_test4,lr3.predict(x_test4))
#[[110   1]
#[ 11   1]]

#making the heatmap
sns.heatmap(cn,annot=True)

#precision socre
pc=precision_score(y_test4,lr3.predict(x_test4))*100
#50.0
rc=recall_score(y_test4,lr3.predict(x_test4))*100
#8.333333333333332
fc=f1_score(y_test4,lr3.predict(x_test4))*100
#14.285714285714285