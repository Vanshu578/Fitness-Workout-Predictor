#practicing the stats
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as st

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/StudentsPerformance.csv")
he=dataset.head(3)

#calculating the mean ,median ,mode for the maths score
mn=dataset["math_score"].mean()
#66.089
md=dataset["math_score"].median()
#66.0
mod=dataset["math_score"].mode()[0]
#65

#making graph for the visualization of maths socre graph
#sns.histplot(x="math_score",data=dataset)
#tail is rightside

#for mean graph
#plt.plot([mn for i in range(0,300)],[i for i in range(0,300)])

#for median graph
#plt.plot([md for i in range(0,300)],[i for i in range(0,300)])

#visualizing the graph for score
#sns.histplot(x="math_score",data=dataset)
#plt.plot([mn for i in range(0,300)],[i for i in range(0,300)],color="red",label="mean")
#plt.plot([md for i in range(0,300)],[i for i in range(0,300)],color="blue",label="median")
#plt.legend()

#variablity and spread
#variance
vr=np.var(dataset["math_score"])
#229.68907899999996

#standard deviation
std=np.std(dataset["math_score"])
#15.155496659628149

#range(max_min)
min_r=dataset["math_score"].min()
max_r=dataset["math_score"].max()
ran=max_r-min_r
#100

#std of reading score
std1=np.std(dataset["reading_score"])
#14.592890015346516

#calculating the percentile and quartile(iqr)
#checking the null vlaues
nl=dataset.isnull().sum()
#no null vlaues

#cheking the percentile 
per=np.percentile(dataset["writing_score"],25),np.percentile(dataset["writing_score"],75)
#(np.float64(57.75), np.float64(79.0))
per1=np.percentile(dataset["writing_score"],50)
#69.0

md=dataset["writing_score"].median()
#69.0

#calculating the quartiles
#q1,Q3,Q2,iqr
q1=dataset["writing_score"].quantile(0.25)
q2=dataset["writing_score"].quantile(0.50)
q3=dataset["writing_score"].quantile(0.75)
#57.75 69.0 79.0
iqr=q3-q1
min_range=q1-(1.5*iqr)
max_range=q3+(1.5*iqr)
#21.25 25.875 110.875

mn1=dataset["writing_score"].min()
mn2=dataset["writing_score"].max()

#calculating the probabilty 
en=dataset["test_preparation_course"].unique()
cn=dataset["test_preparation_course"].value_counts() #none=642,completed=358
ln=len(dataset)
#1000
probability=(dataset["test_preparation_course"]=="completed").sum()/ln*100
#35.8%

cp=(dataset["test_preparation_course"]=="completed").sum()
#358
sc=(dataset["math_score"]>80).sum()
#176
probability1=(sc/cp)*100
#49.162011173184354

#visualizaing the skew and distribution
"""sns.histplot(x="reading_score",data=dataset)
plt.show()

#checking the skewness
sk=dataset["reading_score"].skew()
print(sk)#-0.25910451810923063

me1=dataset["reading_score"].mean()
md1=dataset["reading_score"].median()
mo1=dataset["reading_score"].mode()[0]
#69.169, 70.0, 72

if me1<md1<mo1:
    print("negetive skewed")
else:
    print("no skewed")
#negetive skewed""" 

#T test
#ho=u=67.0
#h1=u!=67.0
#n=1000
#df=999
#std=14.600191937252216
#p_u=67.0
#s_x=69.169
#s_std=14.600191937252216
#n=1000
#table=-1.7108820799094284
#t_table=st.t.ppf(0.05,24) 
#t_cal=(s_x-p_u)/(s_std/np.sqrt(n))


#2example
#ho=u0=u1
#h1=u0!=u1
#female=518
#male=482
#df=34
#female mean=63.633204633204635
#male mean=68.72821576763485
#std_fm_sq=239.98512355959164
#std_mm_sq=206.10269493879457
#t_table=2.0322445093177186
female_math=dataset[dataset["gender"]=="female"]["math_score"]
male_math=dataset[dataset["gender"]=="male"]["math_score"]
df=len(female_math)-len(male_math)-2
t_table=st.t.ppf(1-0.025,34)
female_mean=female_math.mean()
male_mean=male_math.mean()
#63.633204633204635 68.72821576763485
std_fm=female_math.std()
std_mm=male_math.std()
#15.49145324233952 14.356277196362383
std_fm_sq=std_fm*std_fm
std_mm_sq=std_mm*std_mm
#239.98512355959164 206.10269493879457
t_cal=(female_mean-male_mean)/(np.sqrt((std_fm_sq/len(female_math)+(std_mm_sq/len(male_math)))))
#-5.398000564160736
#if abs(t_table)<abs(t_cal):
    #print("h1 is right")
#else:
    #print("h0 is right")

#Linear regression practice
"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/StudentsPerformance.csv")
he=dataset.head(3)

#seeing the null values
nl=dataset.isnull().sum()

#giving the dependent and independent variable
x=dataset[["reading_score","writing_score"]]
y=dataset["math_score"]

#making the figure 
sns.scatterplot(x="reading_score",y="math_score",data=dataset,)
sns.scatterplot(x="writing_score",y="math_score",data=dataset)
plt.xlabel("reading_socre and writing_score")
plt.ylabel("maths_socre")
plt.title("scatter graph for x and y")
plt.show()

#importing the library for train and test split
from sklearn.model_selection import train_test_split

#giving train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#importing the linear regression librery
from sklearn.linear_model import LinearRegression

#fitting the data
lr=LinearRegression()
lr.fit(x_train,y_train)

#finding the score
sc=lr.score(x_test,y_test)*100
#68.25697127424625

#making the prediction
pr=lr.predict([[72.0,74.0]])
#[69.4100717]

#calculating the mse,mae,rmse
from sklearn.metrics import mean_absolute_error,mean_squared_error

#calcualting the mse
mse=mean_squared_error(y_test,lr.predict(x_test))
#77.24297821278955

#calculating the mae
mae=mean_absolute_error(y_test,lr.predict(x_test))
#7.351308782530509

#calculating the rmse
rmse=np.sqrt(mean_squared_error(y_test,lr.predict(x_test)))
#8.788798451027851"""

#question 2
"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/StudentsPerformance.csv")
#he=dataset.head(3)

#adding the column in the dataset
dataset["math_pass"]=(dataset["math_score"]>=50).astype(int)
he=dataset.head(3)

#making the dependent and independent variables
x=dataset[["reading_score","writing_score"]]
y=dataset["math_pass"]

#importing the train and test library 
from sklearn.model_selection import train_test_split

#making the train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#importing the logistic regression library
from sklearn.linear_model import LogisticRegression

#making the object and fitting the model
lr=LogisticRegression()
lr.fit(x_train,y_train)

#checking the modele prediction score
sc=lr.score(x_test,y_test)*100
#85.5

#checking the prediction
pr=lr.predict([[72.0,74.0]])
#[1]

#making the confussion matrix 
#importing the library
from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score

#confusion matrix
cf=confusion_matrix(y_test,lr.predict(x_test))
#[[ 14  20]
# [  9 157]]

pr1=precision_score(y_test,lr.predict(x_test))*100
#88.70056497175142

rr=recall_score(y_test,lr.predict(x_test))*100
#94.57831325301204

fscore=f1_score(y_test,lr.predict(x_test))*100
#91.54518950437318

#making the graph
sns.heatmap(cf,annot=True)
plt.show()"""

#using the titanic dataset for practice 
"""#Level 1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/Titanic-Dataset.csv")
he=dataset.head(3)

#checking the null vlaues
nl=dataset.isnull().sum()
#Age=177, Cabin=687, Embarked=2

#filling the null vlaues(Age ,cabin,Embarked)
dataset["Age"]=dataset["Age"].fillna(dataset["Age"].median())
dataset["Embarked"]=dataset["Embarked"].fillna(dataset["Embarked"].mode()[0])
nl=dataset.isnull().sum()

#droping the "Cabin" column
dataset.drop("Cabin",axis=1,inplace=True)
nl=dataset.isnull().sum()
#no null values after dropuing the column

#one hot encoding for the categorical columns
#taking a seperate variable for the encoding
en_data=dataset[["Sex","Embarked"]]
dm=pd.get_dummies(en_data).info()

#importing the one hot encoding library
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(drop="first")
ar=ohe.fit_transform(en_data).toarray()
df=pd.DataFrame(ar,columns=["Sex_male", "Embarked_Q", "Embarked_S"])

#adding the encoded columns to the original dataset
dataset["Sex_male"]=df["Sex_male"]
dataset["Embarked_Q"]=df["Embarked_Q"]
dataset["Embarked_S"]=df["Embarked_S"]

#checking the dataset
he=dataset.head(3)

#dropuing the unnecessary columns
dataset.drop(["PassengerId","Name","Sex","Ticket","Embarked"],axis=1,inplace=True)
he=dataset.head(3)

#making the dependent and independent variables
x=dataset.iloc[:,1:]
y=dataset["Survived"]

#making the train and test split
from sklearn.model_selection import train_test_split

#making the train and test split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#importing the logistic regreessin library
from sklearn.linear_model import LogisticRegression

#making the model and fitting the data
lr=LogisticRegression()
lr.fit(x_train,y_train)

#checking the score of the model
sc=lr.score(x_test,y_test)*100
#79.88826815642457

#predicting the model
pr=lr.predict([[3,22.0,1,7.25,0,0,1,0]])
#[0]

#Confusion matrix and other metrics
from sklearn.metrics import confusion_matrix

#making the confusion matrix
cf=confusion_matrix(y_test,lr.predict(x_test))
#[[89 16]
 #[20 54]]

#matrix graph
#sns.heatmap(cf,annot=True)

#model acuracy
ml=(89+54)/(89+54+16+20)

#handling the imbalanced dataset
#performing the rando munder and over samplng
#checking the value counts 
#vl=dataset["Survived"].value_counts()
#0    549
#1    342

#importing the moule for sampling
from imblearn.under_sampling import RandomUnderSampler

#making object and Sampling the data
ru=RandomUnderSampler()
ru_x,ru_y=ru.fit_resample(x,y)

#counting the values for the balanced dataset
vl=ru_y.value_counts()
#0    342
#1    342

#importing the train and test split
from sklearn.model_selection import train_test_split

#making the train and test 
x_train1,x_test1,y_train1,y_test1=train_test_split(ru_x,ru_y,train_size=0.8,test_size=0.2,random_state=42)

#making the logistic regression
from sklearn.linear_model import LogisticRegression

#making the model and fitting it
lr1=LogisticRegression()
lr1.fit(x_train1,y_train1)

#checking the model score
sc1=lr1.score(x_test1,y_test1)*100, lr1.score(x_train1,y_train1)*100
#81.02189781021897, 78.06215722120659

#checking the prediction
pr1=lr.predict([[1,38.0,1,0,71.2833,0.0,0.0,0.0]])
#[1] #correct prediction

#Random over sampling
from imblearn.over_sampling import RandomOverSampler

#making object  and fitting it
ro=RandomOverSampler()
ro_x,ro_y=ro.fit_resample(x,y)

#checking the value count
vl2=ro_y.value_counts()
#0    549
#1    549

#making train & test
x_train2,x_test2,y_train2,y_test2=train_test_split(ro_x,ro_y,test_size=0.2,train_size=0.8,random_state=42)

#making the model
lr2=LogisticRegression()
lr2.fit(x_train2,y_train2)

#checking the score
sc2=lr2.score(x_test2,y_test2)*100,lr2.score(x_train2,y_train2)*100
#80.45454545454545, 78.24601366742597

#checking the prediction socre
pr2=lr2.predict([[3,26.0,0,0,7.9250,0.0,0.0,1.0]])
#[1] correct prediction

#making the subset for x
x_subset=dataset[["Age","Fare"]]
y_subset=dataset["Survived"]

#checking the linear seperation
sns.kdeplot(data=dataset["Age"])
plt.show()

#train and test
from sklearn.model_selection import train_test_split

#making train and test
x_train3,x_test3,y_train3,y_test3=train_test_split(x_subset,y_subset,train_size=0.8,test_size=0.2,random_state=42)

#making a gassion and bernouli model 
#importing gassion model
from sklearn.naive_bayes import GaussianNB

#making the gassion model
gnb=GaussianNB()
gnb.fit(x_train3,y_train3)

#checking the score
sc3=gnb.score(x_test3,y_test3)*100
#77.09497206703911

#making the graph for gnb
from mlxtend.plotting import plot_decision_regions
#plot_decision_regions(x_subset.to_numpy(),y_subset.to_numpy(),clf=gnb)
#plt.show() #non linear seperation

#making the model of bernolui model
from sklearn.naive_bayes import BernoulliNB

#making the model and fiting it
bnb=BernoulliNB()
bnb.fit(x_train3,y_train3)

#checking the score
sc4=bnb.score(x_test3,y_test3)*100,bnb.score(x_train3,y_train3)*100
#58.659217877094974, 62.35955056179775

#making the model for bnb
#plot_decision_regions(x_subset.to_numpy(),y_subset.to_numpy(),clf=bnb)
#plt.show()"""

#practice No.2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/Churn_Modelling.csv")

#showing the shape
sh=dataset.shape
print(sh)