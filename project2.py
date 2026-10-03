import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/AI_Usage_and_Impact_on_Students_and_Professionals.csv")
he=dataset.head(3)

#checking the null values
nl=dataset.isnull().sum()

#seeing the data types of the columns
dt=dataset.info()

#changing the datatypes(Age)
un=dataset["Age"].value_counts()
dataset["Age"] = dataset["Age"].astype(str).str.replace("yrs", "").astype(float)
un1=dataset["Age"].value_counts()

dt=dataset.info()

#seeing the gedenr column
un=dataset["Gender"].value_counts()
dataset["Gender"] = dataset["Gender"].astype(str).str.lower().str.strip()
gender_mapping = {
    "m": "male",
    "male": "male",
    "f": "female",
    "female": "female",
    "other": "other",
    "non-binary": "other",
    "nan": "unknown",
}
dataset["Gender"] = dataset["Gender"].map(gender_mapping).fillna("unknown")
#print(dataset["Gender"].value_counts())

#Country column
un=dataset["Country"].value_counts()
dataset["Country"] = dataset["Country"].astype(str).str.lower().str.strip()
country_mapping = {
    "india": "india",
    "united states": "united states",
    "united states of america": "united states",
    "canada": "canada",
    "pakistan": "pakistan",
    "united kingdom": "united kingdom",
    "u.k.": "united kingdom",
    "philippines": "philippines",
    "brazil": "brazil",
    "australia": "australia",
    "nigeria": "nigeria",
    "germany": "germany",
    "france": "france",
    "kenya": "kenya",
    "nan": "unknown",
}
dataset["Country"] = dataset["Country"].map(country_mapping).fillna("unknown")
#print(dataset["Country"].value_counts())

#usertype column
un=dataset["Education_Level"].value_counts()
dataset["Education_Level"] = (
    dataset["Education_Level"].astype(str).str.lower().str.strip()
)
edu_mapping = {
    "high school": "high school",
    "hs": "high school",
    "diploma": "diploma",
    "undergraduate": "bachelor's",
    "undergrad": "bachelor's",
    "bachelor's": "bachelor's",
    "bachelors": "bachelor's",
    "bachelor's degree": "bachelor's",
    "ba/bsc": "bachelor's",
    "master's": "master's",
    "masters": "master's",
    "master's degree": "master's",
    "ma/msc": "master's",
    "phd": "phd",
    "ph.d.": "phd",
    "nan": "unknown",
}
dataset["Education_Level"] = (
    dataset["Education_Level"].map(edu_mapping).fillna("unknown")
)

#print(dataset["Education_Level"].value_counts())

#Profession
un=dataset["AI_Tool"].value_counts()
dataset["AI_Tool"] = dataset["AI_Tool"].astype(str).str.lower().str.strip()
tool_mapping = {
    "chatgpt": "chatgpt",
    "chat gpt": "chatgpt",
    "google gemini": "gemini",
    "gemini": "gemini",
    "microsoft copilot": "copilot",
    "copilot": "copilot",
    "claude": "claude",
    "perplexity ai": "perplexity",
    "grammarly": "grammarly",
    "meta ai": "meta ai",
    "deepseek": "deepseek",
    "nan": "unknown",
}
dataset["AI_Tool"] = dataset["AI_Tool"].map(tool_mapping).fillna("unknown")
#print(dataset["AI_Tool"].value_counts())

#AI_Purpose
un=dataset["AI_Usage_Hours_Per_Day"].value_counts()
dataset["AI_Usage_Hours_Per_Day"] = (
    dataset["AI_Usage_Hours_Per_Day"]
    .astype(str)
    .str.replace("hrs", "", regex=False)
    .str.strip()
)
dataset["AI_Usage_Hours_Per_Day"] = pd.to_numeric(
    dataset["AI_Usage_Hours_Per_Day"], errors="coerce"
)
dataset["AI_Usage_Hours_Per_Day"] = dataset["AI_Usage_Hours_Per_Day"].fillna(
    dataset["AI_Usage_Hours_Per_Day"].median()
)
#print(dataset["AI_Usage_Hours_Per_Day"].describe())

#Time saved hours per week
dataset["Time_Saved_Hours_Per_Week"] = (
    dataset["Time_Saved_Hours_Per_Week"]
    .astype(str)
    .str.replace("hrs", "", regex=False)
    .str.strip()
)
dataset["Time_Saved_Hours_Per_Week"] = pd.to_numeric(
    dataset["Time_Saved_Hours_Per_Week"], errors="coerce"
)
dataset["Time_Saved_Hours_Per_Week"] = dataset[
    "Time_Saved_Hours_Per_Week"
].fillna(dataset["Time_Saved_Hours_Per_Week"].median())
#print(dataset["Time_Saved_Hours_Per_Week"].describe())

#Work_or_Study_Hours_Per_Day
dataset["Work_or_Study_Hours_Per_Day"] = (
    dataset["Work_or_Study_Hours_Per_Day"]
    .astype(str)
    .str.replace("hrs", "", regex=False)
    .str.strip()
)
dataset["Work_or_Study_Hours_Per_Day"] = pd.to_numeric(
    dataset["Work_or_Study_Hours_Per_Day"], errors="coerce"
)
dataset["Work_or_Study_Hours_Per_Day"] = dataset[
    "Work_or_Study_Hours_Per_Day"
].fillna(dataset["Work_or_Study_Hours_Per_Day"].median())
#print(dataset["Work_or_Study_Hours_Per_Day"].describe())

#Monthly_AI_Cost
dataset["Monthly_AI_Cost"] = (
    dataset["Monthly_AI_Cost"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.strip()
)

# 2. Convert to numeric values, turning any invalid text or empty spots into NaN
dataset["Monthly_AI_Cost"] = pd.to_numeric(
    dataset["Monthly_AI_Cost"], errors="coerce"
)

# 3. Fill missing values with the median of the column
dataset["Monthly_AI_Cost"] = dataset["Monthly_AI_Cost"].fillna(
    dataset["Monthly_AI_Cost"].median()
)

# 4. Check the summary to verify it's clean and numeric
#print(dataset["Monthly_AI_Cost"].describe())

#MMonthly_Income
dataset["Monthly_Income"] = (
    dataset["Monthly_Income"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)
dataset["Monthly_Income"] = pd.to_numeric(
    dataset["Monthly_Income"], errors="coerce"
)
dataset["Monthly_Income"] = dataset["Monthly_Income"].fillna(
    dataset["Monthly_Income"].median()
)
#print(dataset["Monthly_Income"].describe())

#seeing the null
dataset["Age"]=dataset["Age"].fillna(dataset["Age"].mode()[0],inplace=True)
dataset["Profession"]=dataset["Profession"].fillna(dataset["Profession"].mode()[0],inplace=True)
dataset["AI_Purpose"]=dataset["AI_Purpose"].fillna(dataset["AI_Purpose"].mode()[0],inplace=True)
dataset["Tasks_Performed"]=dataset["Tasks_Performed"].fillna(dataset["Tasks_Performed"].mode()[0],inplace=True)
dataset["Productivity_Score"]=dataset["Productivity_Score"].fillna(dataset["Productivity_Score"].median(),inplace=True)
dataset["Accuracy_Rating"]=dataset["Accuracy_Rating"].fillna(dataset["Accuracy_Rating"].mode()[0],inplace=True)
dataset["Satisfaction_Score"]=dataset["Satisfaction_Score"].fillna(dataset["Satisfaction_Score"].mode()[0],inplace=True)
dataset["Would_Recommend"]=dataset["Would_Recommend"].fillna(dataset["Would_Recommend"].mode()[0],inplace=True)

#seeing the null
nl=dataset.isnull().sum()

#seeing the duplicates
dc=dataset.duplicated().sum()
#12
sh=dataset.shape
#(300, 19)

#removing the duplicates
dp=dataset.drop_duplicates(inplace=True)
dataset = dataset.reset_index(drop=True)
sh=dataset.shape
#(288, 19)

#Gender, Country, Education_Level, AI_Tool, and AI_Purpose(encoding)
#performing one_hot enmcoding on(Gender,Country,AI_Tool,AI_Purpose)
data=dataset[["Gender","Country","AI_Tool","AI_Purpose"]]

#imporitng the OneHotEncoder
from sklearn.preprocessing import OneHotEncoder

#making the model
on=OneHotEncoder(drop="first")
ar=on.fit_transform(data)
df=pd.DataFrame(ar.toarray(),columns=on.get_feature_names_out(["Gender","Country","AI_Tool","AI_Purpose"]))

#inserting the new columns into dataset
dataset=pd.concat([dataset,df],axis=1)

#seeing the dataset
he=dataset.head(3)

#performing the  ordinal encoding on Education_Level column
from sklearn.preprocessing import OrdinalEncoder

#seeing the unique values of Education_Level\
un=dataset["Education_Level"].value_counts()

#seeting the order
data1=[["high school", "diploma", "bachelor's", "master's", "phd", "unknown"]]

#making the model
oen=OrdinalEncoder(categories=data1)

#replacing it with the encoded values
dataset["Education_Level"] = oen.fit_transform(dataset[["Education_Level"]])

#seeing the dataset
he=dataset.head(3)

#making the train and test split
x=dataset.drop(columns=["User_ID","User_Type","Profession","Tasks_Performed","Productivity_Score","Would_Recommend","Country","Gender","AI_Tool","AI_Purpose"])
y=dataset["Productivity_Score"]

#importing the train and test
from sklearn.model_selection import train_test_split

#regression models
#makin gthe linear regression model
from sklearn.linear_model import LinearRegression

#scalling the data
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(x)
x=pd.DataFrame(sc.transform(x),columns=x.columns)

#making the train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#making the model
lr=LinearRegression()
lr.fit(x_train,y_train)

#checking the score
score=lr.score(x_test,y_test)*100
#61.32320584421102(befor scalling)
#61.32320584421063(after scalling)

#mse,r2
from sklearn.metrics import mean_squared_error, r2_score

#checking the score
me=mean_squared_error(y_test, lr.predict(x_test))
#1.206987313077405
r2=r2_score(y_test, lr.predict(x_test))
#0.6132320584421102

#print(dataset["Would_Recommend"].head(3))

#classification model
#perfoming the ordinal encoding on(Would_Recommend)
from sklearn.preprocessing import OrdinalEncoder

#checking the values
vl=dataset["Would_Recommend"].value_counts()

#giving the data
data2=[["No", "Maybe", "Yes"]]

#making the model
oen2=OrdinalEncoder(categories=data2)

#inserting the encoded values
dataset["Would_Recommend"] = oen2.fit_transform(dataset[["Would_Recommend"]])

#seeing the data
#print(dataset["Would_Recommend"].head(3))

#making the logistic regression model
from sklearn.linear_model import LogisticRegression

#making the x and y
x1=dataset.drop(columns=["User_ID","User_Type","Profession","Tasks_Performed","Would_Recommend","Country","Gender","AI_Tool","AI_Purpose"])
y1=dataset["Would_Recommend"]

#making the train and test split
x1_train,x1_test,y1_train,y1_test=train_test_split(x1,y1,test_size=0.2,train_size=0.8,random_state=42)

#performing the scalling
sc1=StandardScaler()
x1_train_scaled=sc1.fit_transform(x1_train)
x1_test_scaled=sc1.transform(x1_test)

#making the model
lr1=LogisticRegression(max_iter=5000,C=10.0)
lr1.fit(x1_train_scaled,y1_train)

#seeing the score
score1=lr1.score(x1_test_scaled,y1_test)*100
#62.06896551724138(before scalling)
#51.724137931034484(after scalling)

#RandomForestRegression model
from sklearn.ensemble import RandomForestClassifier

#making the x and y
x3=dataset.drop(columns=["User_ID","User_Type","Profession","Tasks_Performed","Would_Recommend","Country","Gender","AI_Tool","AI_Purpose"])
y3=dataset["Would_Recommend"]

#making the train and test
x_train3,x_test3,y_train3,y_test3=train_test_split(x3,y3,test_size=0.2,train_size=0.8,random_state=42)

#making the model
rf=RandomForestClassifier(class_weight='balanced',random_state=42)
rf.fit(x_train3,y_train3)

#checking the model score
sc2=rf.score(x_test3,y_test3)*100
#53.44827586206896
#60.3448275862069(after balancing)

#making a confussion matrix
from sklearn.metrics import confusion_matrix

#making the matirx
cf=confusion_matrix(y_test3,rf.predict(x_test3))

#making the kneighbour 
x4=dataset.drop(columns=["User_ID","User_Type","Profession","Tasks_Performed","Would_Recommend","Country","Gender","AI_Tool","AI_Purpose"])
y4=dataset["Would_Recommend"]

#peroforming the scalling
ss=StandardScaler()
ss.fit(x4)
x4=pd.DataFrame(ss.transform(x4),columns=x4.columns)

#making the train and test
x4_train,x4_test,y4_train,y4_test=train_test_split(x4,y4,test_size=0.2,train_size=0.8,random_state=42)

#importing the kneighbour
from sklearn.neighbors import KNeighborsClassifier

#making the model
knn=KNeighborsClassifier()
knn.fit(x4_train,y4_train)

#checking the socre
sc3=knn.score(x4_test,y4_test)*100
#50.0

#making the svm(classification model)
from sklearn.svm import SVC

#making model and fit
sv=SVC(kernel='linear')
sv.fit(x4_train,y4_train)

#checking the score
sc4=sv.score(x4_test,y4_test)*100
#55.17241379310344

#making the graph
models = ["Linear Reg", "Logistic Reg", "Random Forest", "KNN", "SVM"]
score_g=[score,score1,sc2,sc3,sc4]
plt.bar(models,score_g)
plt.xlabel("models")
plt.ylabel("accuracy")
plt.show()