#vooting classifier

#classification 
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_moons

#making the datasets
x,y=make_moons(n_samples=1000,noise=0.2)
df={"x1":x[:,0],"x2":x[:,1],"y":y}
dataset= pd.DataFrame(df)

#making the graph to see linearity
sns.scatterplot(x="x1",y="x2",data=dataset,hue="y")

#making dependent and independent variable
x_a=dataset.iloc[:,:-1]
y_a=dataset["y"]

#importing the train and test split
from sklearn.model_selection import train_test_split

#making train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#importing the models
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

#checking the score
#dession tree
dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)
sc=dt.score(x_train,y_train)*100,dt.score(x_test,y_test)*100
#(100.0, 95.0)

#svm
sv=SVC()
sv.fit(x_train,y_train)
sc1=sv.score(x_train,y_train)*100,sv.score(x_test,y_test)*100
#(97.75, 96.0)

#gnb models
gnb=GaussianNB()
gnb.fit(x_train,y_train)
sc2=gnb.score(x_train,y_train)*100,gnb.score(x_test,y_test)*100
#(87.25, 88.0)

#importing the voting classifier
from sklearn.ensemble import VotingClassifier

li=[("dt1",DecisionTreeClassifier()),("sv1",SVC()),("gnb1",GaussianNB())]

#making the model
vc=VotingClassifier(li)
vc.fit(x_train,y_train)

#checking the score
sc3=vc.score(x_train,y_train)*100,vc.score(x_test,y_test)*100
#(97.625, 96.5)

#making the dataframe
prd={"dt":dt.predict(x_test),"svm":dt.predict(x_test),"gnb":gnb.predict(x_test),"vc":vc.predict(x_test)}
df1=pd.DataFrame(prd)
#print(df1)"""

#Regrssion practicle
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/cgpa_package_regression.csv")
he=dataset.head(3)

#making dependent and independent variable
x=dataset.iloc[:,:-1]
y=dataset["package"]

#importing the train and test split
from sklearn.model_selection import train_test_split

#making the train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#importing the models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

#making the models
#linear Regression
lr=LinearRegression()
lr.fit(x_train,y_train)
sc=lr.score(x_train,y_train)*100,lr.score(x_test,y_test)*100
#(93.95715737023005, 94.13428002999844)

#Decession Tree
dt=DecisionTreeRegressor()
dt.fit(x_train,y_train)
sc1=dt.score(x_train,y_train)*100,dt.score(x_test,y_test)*100
#(99.03743221379277, 93.54833281605993)

#SVR
sv=SVR()
sv.fit(x_train,y_train)
sc2=sv.score(x_train,y_train)*100,sv.score(x_test,y_test)*100
#(96.8520044289373, 95.9128024759528)

#imporitng the esemble model
from sklearn.ensemble import VotingRegressor

#making the list of estimater
li=[("lr1",LinearRegression()),("dt1",DecisionTreeRegressor()),("sv1",SVR())]

#making the voting model
vc=VotingRegressor(li)
vc.fit(x_train,y_train)

#checking the score
vc1=vc.score(x_train,y_train)*100,vc.score(x_test,y_test)*100
#(97.67896173187506, 95.68187613895222)

#making the dataframe and observing values
df={"lr":lr.predict(x_test),"dt":dt.predict(x_test),"svm":sv.predict(x_test),"vc":vc.predict(x_test)}
df1=pd.DataFrame(df)"""

#Baggging (bagging meta-Etimater,random forest)
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_moons

#making the dastaset
x,y=make_moons(n_samples=1000,noise=0.2)
df={"x1":x[:,0],"x2":x[:,1],"y":y}
dataset=pd.DataFrame(df)

#making the graph
sns.scatterplot(x="x1",y="x2",data=dataset,hue="y")

#mkaing dependent and independent variable
x=dataset.iloc[:,:-1]
y=dataset["y"]

#importing the train and test split
from sklearn.model_selection import train_test_split

#making the train and test split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#importing the models]
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

#making the model
bg=BaggingClassifier(estimator=SVC(),n_estimators=30)
bg.fit(x_train,y_train) 

#checking the score
sc=bg.score(x_train,y_train)*100,bg.score(x_test,y_test)*100
#(95.625, 94.0)

#random forest
rf=RandomForestClassifier(n_estimators=30)
rf.fit(x_train,y_train)
sc1=rf.score(x_train,y_train)*100,rf.score(x_test,y_test)*100
#(99.625, 95.5)"""

#regresisin practilce
"""import pandas as pd
import seaborn  as sns
import matplotlib.pyplot as plt

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/cgpa_package_regression.csv")
he=dataset.head(3)

#making the dependent and indepedent variable
x=dataset.iloc[:,:-1]
y=dataset["package"]

#importng the dataset
from sklearn.model_selection import train_test_split

#making the train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#importing the model
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

#making the model
bg=BaggingRegressor(estimator=LinearRegression(),n_estimators=40)
bg.fit(x_train,y_train)
sc=bg.score(x_train,y_train)*100,bg.score(x_test,y_test)*100
#(93.95708723581045, 94.13034738849156)

#random forest
rf=RandomForestRegressor(n_estimators=50)
rf.fit(x_train,y_train)
sc1=rf.score(x_train,y_train)*100, rf.score(x_test,y_test)*100
#(98.78596842959898, 94.54024526033567)"""