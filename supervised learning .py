"""#train test Split
import pandas as pd

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")
he=dataset.head(3)

#Giving the input data
input_data=dataset.iloc[:,:-1]

#giving the output data
output_data=dataset["Loan_Status"]

#Making 4 variables to store the train & test dataset
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(input_data,output_data,test_size=0.25)

#seeing shape to see actual splitting of data
x_train=x_train.shape
print(x_train)
y_train=y_train.shape
print(y_train)
x_test=x_test.shape
print(x_test)
y_test=y_test.shape
print(y_test)"""

#Regreesion anaylysis
#Linear Regression
"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/SHES.csv")
he=dataset.head(3)

#seeing null vlaues
nl=dataset.isnull().sum()

#giving dependent and independent variable
x=dataset[["HoursStudied"]]
y=dataset["Score"]

#plotting the graph
sns.scatterplot(x="HoursStudied",y="Score",data=dataset)

#importing the another library
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#training and testing data
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2 ,train_size=0.8,random_state=42)

#fitting the data
lr=LinearRegression()
lr.fit(x_train,y_train)

#predicting the data
pr=lr.predict([[4.2]])


#finding the accuracy score
sc=lr.score(x_test,y_test)*100
print(sc)
#finding the m vlaue(cofficient) and c vlaue(interception)
cf=lr.coef_
inc=lr.intercept_

#putting the value in equation(y=mx+c)
y=11.05172414*4.2+(- 29.181034482758626)

#making graph for linear regeression
sns.scatterplot(x="HoursStudied",y="Score",data=dataset)
plt.plot(dataset["HoursStudied"], lr.predict(x))
plt.show()"""

#Multiple linear regression
"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/regression_dataset.csv")
he=dataset.head(3)

#checking the null vlaues
nl=dataset.isnull().sum()

#checking the correlation
sns.heatmap(data=dataset.corr(),annot=True)
plt.show()

#giving dependent and independent variable
x=dataset.iloc[:,:-1]
y=dataset["Exam_Score"]

#importing the another library
from sklearn.model_selection import train_test_split

#seeing the shape of the dataset
sh=dataset.shape

#assigning the train and test data
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#impoting the linear regression library
from sklearn.linear_model import LinearRegression

#making the object of linear regression
lr=LinearRegression()

#fitting the data
lr.fit(x_train,y_train)

#Seeing ther score
sr=lr.score(x_test,y_test)*100
 #99.57431730064867

#finding the m vlaue(cofficient) and c vlaue(interception)
cf=lr.coef_
inc=lr.intercept_
#[11.75986509  0.19713322 -0.30303541] 33.97470489038803

#predicting the data
#predicting on the equation y=m1x1+m2x2+m3x3+c
#y=11.75986509*hours_studied+0.19713322*previous_score-0.30303541*hours_sleep+33.97470489038803
pr=lr.predict(x_test)"""

#polynomial regression (on hold) (pura nahi hua)
"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/polynomial_regression_data.csv")
he=dataset.head(3)
dc=dataset.columns

#graphs for predicting the data
plt.scatter(dataset["X"],dataset["y"])

#making the dependent and independent variables
x=dataset[["X"]]
y=dataset["y"]

#importing the train test split library
from sklearn.model_selection import train_test_split

#giving the train and test data
x_train,x_test,y_test,y_train=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

from sklearn.preprocessing import PolynomialFeatures

#making the object of polynomial regression
pf=PolynomialFeatures(degree=2)

#fitting and transforming the data
x_train=pf.fit_transform(x_train)
x_test=pf.transform(x_test)

#imporitng the linear regression library
from sklearn.linear_model import LinearRegression

#fitting the model
lr=LinearRegression()
lr.fit(x_train,y_train)

#checking the model acuracy
sc=lr.score(x_test,y_test)*100
print(sc)"""

#lasso regularization and ridge regularization
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/regularization_practice_data.csv")
he=dataset.head(3)

#graph for correlation
#plt.figure(figsize=(10,10))
#sns.heatmap(data=dataset.corr(),annot=True)

#seperating the columns
x=dataset.iloc[:,:-1]
y=dataset["House_Price"]

#scalling the dataset
sc=StandardScaler()
sc.fit(x)
x=pd.DataFrame(sc.transform(x),columns=x.columns)

#train and test split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#importing the linear regression library
from sklearn.linear_model import LinearRegression,Lasso,Ridge

#making the model
lr=LinearRegression()
lr.fit(x_train,y_train)

#checking the score
sc=lr.score(x_test,y_test)*100
#98.84846836494813

#making hte linear regression graph
"""plt.figure(figsize=(15,5))
plt.bar(x.columns,lr.coef_)
plt.xlabel("Features")
plt.ylabel("Coefficients")
plt.title("Linear Regression Coefficients")"""

#making the lasso regression model
la=Lasso(alpha=0.5)
la.fit(x_train,y_train)
sc=la.score(x_test,y_test)*100
#98.84159739135843

#making the lasso regression graph
"""plt.figure(figsize=(15,5))
plt.bar(x.columns,la.coef_)
plt.title("LASSO REGRESSION GRAPH")
plt.xlabel("Columns")
plt.ylabel("Coef")"""

#Ridge Model
ri=Ridge(alpha=0.5)
ri.fit(x_train,y_train)
sc=ri.score(x_test,y_test)*100
#98.82487957430709

#making the graph for model
plt.bar(x.columns,ri.coef_)
plt.title("RIDGE REGRESSION GRAPH")
plt.xlabel("Columns")
plt.ylabel("Coef")

#Linear Regression MSE,MAE.RMSE
from sklearn.metrics import mean_squared_error,mean_absolute_error
mean_squared_error(y_test,lr.predict(x_test)) #166.88789731458814
mean_absolute_error(y_test,lr.predict(x_test)) #11.232067961502667
np.sqrt(mean_squared_error(y_test,lr.predict(x_test))) #12.918509872062959

#Ridge Regression MSE,MAE.RMSE
mean_squared_error(y_test,ri.predict(x_test)) #170.30654735462875
mean_absolute_error(y_test,ri.predict(x_test)) #11.407929581789855
np.sqrt(mean_squared_error(y_test,ri.predict(x_test))) #13.050155070137242

#Lasso Regression MSE,MAE.RMSE
mean_squared_error(y_test,la.predict(x_test)) #167.8836861405179
mean_absolute_error(y_test,la.predict(x_test)) #167.8836861405179
np.sqrt(mean_squared_error(y_test,la.predict(x_test))) #12.956993715384673

#comparring the cofficent
df=pd.DataFrame({"Col_Name":x.columns, "LinearRegression":lr.coef_,"Lasso":la.coef_,"Ridge":ri.coef_})
