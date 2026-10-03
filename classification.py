#logistic regression model
"""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/logistic_regression_data.csv")
he=dataset.head(3)

#making the regression graph
#sns.scatterplot(x="Hours_Studied",y="Passed",data=dataset)

#making dependent and independent variables 
x=dataset[["Hours_Studied"]]
y=dataset["Passed"]

#importing the library for train test split
from sklearn.model_selection import train_test_split

#trianin the datsaer
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#importing the library for logistic regression
from sklearn.linear_model import LogisticRegression

#making the model
lr=LogisticRegression()
lr.fit(x_train,y_train)

#predicting the score
sc=lr.score(x_test,y_test)*100

#prdicting the data
sc1=lr.predict([[7]])

#making the graph
sns.scatterplot(x="Hours_Studied",y="Passed",data=dataset)
sns.lineplot(x="Hours_Studied", y=lr.predict(x),data=dataset,color='red')
plt.show()"""

#bineary classification model(multiple inputs)
"""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/multi_feature_logistic_data.csv")
he=dataset.head(3)

#making the graph to show speration of data
#sns.scatterplot(x="Hours_Studied",y="Mock_Score",data=dataset,hue="Passed") #it is not linearly seperable data so we will use logistic regression model

#making the dependent and independent variable
x=dataset[['Hours_Studied', 'Mock_Score']]
y=dataset["Passed"]

#importing the library for train test splitrain_test_split
from sklearn.model_selection import train_test_split

#making the train and test data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#Making the model of logistic regression
from sklearn.linear_model import LogisticRegression

#making the model
lr=LogisticRegression()
lr.fit(x_train,y_train)

#checking the score of the model
lr.score(x_test,y_test)*100
#100.0

#Graph for seperation of data through mlextend
from mlxtend.plotting import plot_decision_regions
plot_decision_regions(x.to_numpy(),y.to_numpy(),clf=lr)
plt.show()"""

#using the polynomial feature on the above dataset
"""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/multi_feature_logistic_data.csv")
he=dataset.head(3)

#making the dependent and independent variable
x=dataset[['Hours_Studied', 'Mock_Score']]
y=dataset["Passed"]

#polynomial feature
from sklearn.preprocessing import PolynomialFeatures

#making the model
pf=PolynomialFeatures(degree=2)
pf.fit(x)
pf.transform(x)

#seeing the shape
x.shape #(40, 2)

#importing the library for train test splitrain_test_split
from sklearn.model_selection import train_test_split

#making the train and test data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#Making the model of logistic regression
from sklearn.linear_model import LogisticRegression

#making the model
lr=LogisticRegression()
lr.fit(x_train,y_train)

#checking the score of the model
sc=lr.score(x_test,y_test)*100
print(sc)"""

#logistic Regression (Multiclass CLassification)
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/multiclass_student_data.csv")
he=dataset.head(3)

#checking the unique vlaue
un=dataset["Grade"].unique()

#making the graph
sns.pairplot(data=dataset,hue="Grade")

#making dependent and independent variable
x=dataset.iloc[:,:-1]
y=dataset["Grade"]

#making the train and Test split
from sklearn.model_selection import train_test_split

#performing the split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#OVR method
#importing the logistic regression
from sklearn.linear_model import LogisticRegression

#Assigining the ovr Method
lr=LogisticRegression()
lr.fit(x_train,y_train)

#checking the score
sc=lr.score(x_test,y_test)*100
#83.33333333333334"""

#handling inbalanced dataset
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/Social_Network_Ads.csv")
he=dataset.head(3)

#droping the column
dataset.drop(["User ID","Gender"], axis=1, inplace=True)
he=dataset.head(3)

#checking the count vlaues in column "purachesd"
un=dataset["Purchased"].value_counts()

#making dependent and independent variables
x=dataset.iloc[:,:-1]
y=dataset["Purchased"]
(y.ndim)
(x.shape)

#importing the train and test split
from sklearn.model_selection import train_test_split

#performing train and test split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#importing the logistic regression
from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()
lr.fit(x_train,y_train)

#checking the score
sc=lr.score(x_test,y_test)*100
#88.75

#predicting the data
pr=lr.predict([[19,19000]])#0 correct prediction
pr1=lr.predict([[47,25000]])#0 wrong prediction instead of 1
pr2=lr.predict([[30,135000]])#0 wrong prediction instead of 1

#handling imbalanced dataset(random under and random over sampling)
import pandas as pd

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/Social_Network_Ads.csv")
he=dataset.head(3)

#droping the column
dataset.drop(["User ID","Gender"], axis=1, inplace=True)
he=dataset.head(3)

#checking the count vlaues in column "purachesd"
un=dataset["Purchased"].value_counts()

#making dependent and independent variables
x=dataset.iloc[:,:-1]
y=dataset["Purchased"]

#importing the imblearn
from imblearn.under_sampling import RandomUnderSampler

#making object & sampling the data
ru=RandomUnderSampler()
ru_x,ru_y=ru.fit_resample(x,y)

#counting the values after sampling
cn=ru_y.value_counts()

#importing the test and train
from sklearn.model_selection import train_test_split

#making the train and test data
x_train,x_test,y_train,y_test=train_test_split(ru_x,ru_y,train_size=0.8,test_size=0.2,random_state=42)

#importing the logistic regression
from sklearn.linear_model import LogisticRegression

#making the object and fit it
lr=LogisticRegression()
lr.fit(x_train,y_train)

#checking the score
sc=lr.score(x_test,y_test)*100
#79.3103448275862

#prediction the score
#pr=lr.predict([[47,30000]])
#[1] right prediction
#pr1=lr.predict([[49,28000]])
#[1] right prediction

#random over sampling
from imblearn.over_sampling import RandomOverSampler

#making object and fitting it
ro=RandomOverSampler()
ro_x,ro_y=ro.fit_resample(x,y)

#seeing the value count
cn1=ro_y.value_counts()

#tran and test split
x_train1,x_test1,y_train1,y_test1=train_test_split(ro_x,ro_y,random_state=42,test_size=0.2,train_size=0.8)

#making model & fit the data
lr1=LogisticRegression()
lr1.fit(x_train1,y_train1)

#checking the score
sc1=lr1.score(x_test1,y_test1)*100
#84.46601941747572

#prediction of model
pr1=lr1.predict([[27,137000]])
print(pr1)#wrong prediction 0 instead of 1
pr2=lr1.predict([[47,30000]])
print(pr2)#[1]right prediction"""

#nave bayes programe
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mlxtend.plotting import plot_decision_regions

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/placement.csv")
he=dataset.head(3)

#checking the null vlaues
nl=dataset.isnull().sum()

#making the grapg for linear seperation
#sns.scatterplot(x="cgpa",y="iq",data=dataset,hue="placement")

#checking the dataset for normal distribution
#sns.kdeplot(data=dataset["iq"])

#making the independent and dependent variables
x=dataset.iloc[:,:-1]
y=dataset["placement"]

#importing the train and test split
from sklearn.model_selection import train_test_split

#making train & test
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#importing the library
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB

#making the model
gnb=GaussianNB()
gnb.fit(x_train,y_train)

#checking the score
sc=gnb.score(x_test,y_test)*100
#85.0 

#predicting the model accuruacy
pr=gnb.predict([[6.8,123]])
print(pr)

#making the model(multinomial)
mnb=MultinomialNB()
mnb.fit(x_train,y_train)

#checking the score
sc1=mnb.score(x_test,y_test)*100
#95.0

#making the model(binomial)
bnb=BernoulliNB()
bnb.fit(x_train,y_train)

#checking the score
sc2=bnb.score(x_test,y_test)*100
#50.0

#making the graph
plot_decision_regions(x.to_numpy(),y.to_numpy(),clf=gnb)
plt.show()"""

#hpyerparameter Tunning
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/polynomial_regression_data.csv")
he=dataset.head(3)

#making the dpendent and independent variable
x=dataset[["X"]]
y=dataset["y"]

#importing the train and test
from sklearn.model_selection import train_test_split

#making the train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#importing the decession tree
from sklearn.tree import DecisionTreeRegressor

#making model and fit
dt=DecisionTreeRegressor(splitter="random",max_depth=4,criterion='absolute_error') #permeter given by model
dt.fit(x_train,y_train)

#checking the score
sc=dt.score(x_train,y_train)*100,dt.score(x_test,y_test)*100
#(100.0, 91.76266625897458)  #before adding the perameter
##(95.69014822810443, 82.22830043410697) #after adding the peramemter(gridsearchcv)
#(98.60932510395034, 87.42613848563828) #after adding the permemter(randomsearch cv)

#importing the gridsearchcv and randomizedsearchsv
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV

#making the parameters
df={"criterion":["squared_error","absolute_error","poisson"],"splitter":["best","random"],"max_depth":[i for i in range(2,20)]}

#making model and fit
gd=GridSearchCV(DecisionTreeRegressor(),param_grid=df)#
gd.fit(x_train,y_train)

#RandomSearchcv
rd=RandomizedSearchCV(DecisionTreeRegressor(),param_distributions=df,n_iter=20)
rd.fit(x_train,y_train)

#checking the best peremeter
pr=rd.best_params_
print(pr)

pr1=gd.best_params_
print(pr1)

#checking the socres
sc=gd.best_score_,rd.best_score_
print(sc)"""

#Cross-validation in machine learning
"""import pandas as pd

#Loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/placement.csv")
he=dataset.head(3)

#making the dependent and independent variable
x=dataset.iloc[:,:-1]
y=dataset["placement"]

#mkaing the new dataset for a small data
new_dataset=dataset.head(10)

#importing the models
from sklearn.model_selection import LeaveOneOut,LeavePOut,KFold,StratifiedKFold

#makig the new varialbes
x_new=new_dataset.iloc[:,:-1]
y_new=new_dataset["placement"]

#making the model and fit
lo=LeaveOneOut()
for train,test in lo.split(x_new,y_new):
    print(train,test)

#leavepout
lv=LeavePOut(p=2)
for train,test in lv.split(x_new,y_new):
    print(train,test)

#kfold
k=KFold(n_splits=5)
for train,test in k.split(x_new,y_new):
    print(train,test)

#statisfiedkfold only work with clissification data 

#making the model for cross validation
from sklearn.linear_model import LinearRegression

#making a cross validation
from sklearn.model_selection import cross_val_score

#checking the acuuracy
p=cross_val_score(LinearRegression(),x,y,cv=KFold(n_splits=10))

#sorting the socre
print(p.sort())
print(p*100)
#[42.45130018 45.87341675 54.11583735 54.6949414  60.7231032  63.58421487
 #70.56616408 72.67242429 77.56680173 80.18020608]"""

#kmean clustering
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the datasset
dataset=pd.read_csv("C:/Users/User/Desktop/Iris.csv")
he=dataset.head(3)

#droping the "species" column for clustering
dataset.drop(["Id","Species"],axis=1,inplace=True)
he=dataset.head(3)

#making the graph to see linear seperation
sns.pairplot(data=dataset)

#importing the kmeans library
from sklearn.cluster import KMeans

#making clusters
wcss=[]
for i in range(2,21):
    km=KMeans(n_clusters=i,init='k-means++')
    km.fit(dataset)
    wcss.append(km.inertia_)

#making the graph for elbow diagrame
plt.figure(figsize=(10,5))
plt.plot([i for i in range(2,21)],wcss,marker="o")
plt.xlabel("no.of.clusters")
plt.ylabel("wcss")
plt.xticks([i for i in range(2,21)])
plt.grid(axis="x")
plt.show()

#prediction of dataset
kmn=KMeans(n_clusters=3)
dataset["predict"]=kmn.fit_predict(dataset)
he=dataset.head(3)
print(he)

#making graph for cluster
sns.pairplot(data=dataset,hue="predict")
plt.show()