import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import joblib

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/fast_food_cheat_meal_workout_burn.csv")
he=dataset.head(3)

#Phase 1

#checking the null vlaues
nl=dataset.isnull().sum()
#0 null vlaues

#checking the duplicates 
dp=dataset.duplicated().sum()
#0 duplicates


#Calculating the mean , median ,mode and standard deviation
# Mean
mn=np.mean(dataset["total_calories"])
#1602.574375
mn=np.mean(dataset["fat_grams"])
#80.061375
mn=np.mean(dataset["protein_grams"])
#54.03725
mn=np.mean(dataset["running_burn_time_min"])
#117.9175375

#Median
md=np.median(dataset["total_calories"])
#1479.0
md=np.median(dataset["fat_grams"])
#74.0
md=np.median(dataset["protein_grams"])
#48.0
md=np.median(dataset["running_burn_time_min"])
#107.4

#Standard Deviation
sd=np.std(dataset["total_calories"])
#672.0860703573311
sd=np.std(dataset["fat_grams"])
#34.28649308560698
sd=np.std(dataset["protein_grams"])
#30.68842391582696
sd=np.std(dataset["running_burn_time_min"])
#55.488164469426216

#qr Range
r=np.percentile(dataset["total_calories"],25),np.percentile(dataset["total_calories"],50),np.percentile(dataset["total_calories"],75)
#(np.float64(1080.0), np.float64(1479.0), np.float64(2008.0))
r=np.percentile(dataset["fat_grams"],25),np.percentile(dataset["fat_grams"],50),np.percentile(dataset["fat_grams"],75)
#(np.float64(53.0), np.float64(74.0), np.float64(100.0))
r=np.percentile(dataset["protein_grams"],25),np.percentile(dataset["protein_grams"],50),np.percentile(dataset["protein_grams"],75)
#(np.float64(30.0), np.float64(48.0), np.float64(71.0))
r=np.percentile(dataset["running_burn_time_min"],25),np.percentile(dataset["running_burn_time_min"],50),np.percentile(dataset["running_burn_time_min"],75)
#(np.float64(76.1), np.float64(107.4), np.float64(147.5))

#range
max_r=dataset["total_calories"].max()
min_r=dataset["total_calories"].min()
#2850

max_r=dataset["fat_grams"].max()
min_r=dataset["fat_grams"].min()
#158

max_r=dataset["protein_grams"].max()
min_r=dataset["protein_grams"].min()
#125

max_r=dataset["running_burn_time_min"].max()
min_r=dataset['running_burn_time_min'].min()
#410.2

#Data Visualization
#seeing the correlation
#plt.figure(figsize=(5,4))
#sns.heatmap(data=dataset[["total_calories","fat_grams","protein_grams","running_burn_time_min"]].corr(),annot=True)
#plt.show()

#Distribution graphs( workout_shock_tier)
#plt.figure(figsize=(9, 5))
#sns.countplot(data=dataset, x="")
#plt.title("Workout Shock Tier Distribution")
#plt.show()

#Distribution graphs(fitness_level)
#plt.figure(figsize=(9, 5))
#sns.countplot(data=dataset, x="fitness_level")
#plt.title("fitness_level")
#plt.show()

#Phase 2

#Encoding of Columns(fast_food_chain,meal_category,consumer_gender,fitness level)
data=dataset[["fast_food_chain","meal_category","consumer_gender"]]

#Importing The Encoder
from sklearn.preprocessing import OneHotEncoder
oh=OneHotEncoder(drop="first")
ar=oh.fit_transform(data)
df=pd.DataFrame(ar.toarray(),columns=oh.get_feature_names_out(["fast_food_chain","meal_category","consumer_gender"]))

#inserting the columns in dataset
dataset=pd.concat([dataset,df],axis=1)

#seeing the info
inf=dataset.info()
print(inf)
#columns are encoded

#using ordinal Encoding(fitness level)
un=dataset["fitness_level"].unique()
#['Moderately Active', 'Sedentary', 'Highly Trained']

#performing the Encoding
data=[["Sedentary","Moderately Active","Highly Trained"]]

#importing the encoder
from sklearn.preprocessing import OrdinalEncoder

#making the encoding
oe=OrdinalEncoder(categories=data)

#replacing it with original data
dataset["fitness_level"]=dataset["fitness_level"]=oe.fit_transform(dataset[["fitness_level"]])

#droping the unnecessery column
dataset.drop(columns=["order_id"],inplace=True)

#seeing the data
inf=dataset.info()

#performing the label encoding(workout_shock_tier)
un=dataset["workout_shock_tier"].unique()
#[          'High Sweat Penalty', 'Extreme / Half-Marathon Toll',
       # 'Severe Cardio Deficit',                'Moderate Burn']

#imporintg the encoding
from sklearn.preprocessing import LabelEncoder

#making the encoder
ll=LabelEncoder()
ll.fit(dataset["workout_shock_tier"])
ll.transform(dataset["workout_shock_tier"])

#inserting it in original dataset
dataset["workout_shock_tier"]=dataset["workout_shock_tier"]=ll.transform(dataset["workout_shock_tier"])

#seeing the dataset
dataset["workout_shock_tier"].unique()
#[1 0 3 2]

#-------------------------------------------------Regression------------------------------------------------------------
#making the models
x=dataset.drop(columns=["net_caloric_surplus","cycling_burn_time_min",
"walking_burn_time_min","running_burn_time_min",
"hiit_burn_time_min","thermic_effect_calories",
"fast_food_chain","meal_category",
"consumer_gender","fitness_level"])

y=dataset["running_burn_time_min"]

#Importing the train and test
from sklearn.model_selection import train_test_split

#making the train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

# 1 Linear Regression
from sklearn.linear_model import LinearRegression

#making the model
le=LinearRegression()
le.fit(x_train,y_train)

#checking the score
score=le.score(x_test,y_test)*100
#94.14521829480064

# 2 RandomForestRegression
from sklearn.ensemble import RandomForestRegressor

#making the model
rf=RandomForestRegressor()
rf.fit(x_train,y_train)

#checking the score
rf_score=rf.score(x_test,y_test)*100
#97.77823782277677

# 3 Decision Tree Regression
from sklearn.tree import DecisionTreeRegressor

#making the model
dt=DecisionTreeRegressor(max_depth=5,random_state=42)
dt.fit(x_train,y_train)

#checking the socre
dt_socre=dt.score(x_test,y_test)*100
#93.97543227214766

#Checking the metrics
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
mn=mean_absolute_error(y_test,le.predict(x_test))
#3.550134875442595
mn=mean_absolute_error(y_test,rf.predict(x_test))
#3.403284374999997
mn=mean_absolute_error(y_test,dt.predict(x_test))
#4.522749999999999

ms=mean_squared_error(y_test,le.predict(x_test))
#19.323411335005318
ms=mean_squared_error(y_test,rf.predict(x_test))
#18.433860437499987
ms=mean_squared_error(y_test,dt.predict(x_test))
#34.3499375

r2=r2_score(y_test,le.predict(x_test))
#0.9934495498648729
r2=r2_score(y_test,rf.predict(x_test))
#0.9937956075481428
r2=r2_score(y_test,dt.predict(x_test))
#0.9883844720617744

# Graphs
#making the linear regression graph
#cs=pd.Series(le.coef_,index=x.columns).sort_values()
#cs.plot(kind="barh",color="blue")
#plt.title("Linear Regression")
#lt.xlabel("Cofecient")
#lt.ylabel("features")
#lt.show()

#making the graph of Decession tree regression
#from sklearn.tree import plot_tree
#plot_tree(dt,feature_names=x.columns,filled=True,rounded=True,fontsize=10)
#plt.title("Decession tree regression")
#plt.show()

#RandomForestRegression graph
#importance=rf.feature_importances_
#feature=pd.Series(importance,index=x.columns).sort_values()
#feature.tail(15).plot(kind="barh",color="green")
#plt.title("RandomforestRegression")
#plt.xlabel("importance")
#plt.ylabel("columns")
#plt.show()

#----------------------------------------------Classisfication----------------------------------------------------------
#Making The Model
x1=dataset.drop(columns=["net_caloric_surplus",
"cycling_burn_time_min","walking_burn_time_min",
"running_burn_time_min","hiit_burn_time_min",
"thermic_effect_calories","fast_food_chain",
"meal_category","consumer_gender",
"fitness_level","workout_shock_tier"])

y1=dataset["workout_shock_tier"]

#making the train and test split
x_train,x_test,y_train,y_test=train_test_split(x1,y1,test_size=0.2,train_size=0.8,random_state=42)

#scalling the data
from sklearn.preprocessing import StandardScaler

#making the scaler
ss=StandardScaler()

#scaling thed data
x_train_scaled=ss.fit_transform(x_train)
x_test_scaled=ss.transform(x_test)

# 1 Logistic Regression
from sklearn.linear_model import LogisticRegression

#making the model
lr=LogisticRegression()
lr.fit(x_train_scaled,y_train)

#Checking the socre
lr_socre=lr.score(x_test_scaled,y_test)*100
#91.125

#performing a Cross Validation
from sklearn.model_selection import cross_val_score

#checking the accuracy
cv_score=cross_val_score(LogisticRegression(max_iter=1000),x_train_scaled,y_train,cv=5)

#Soritng the score
cv_score.sort()
#[88.125    88.515625 89.21875  89.921875 90.234375]

#Maiking the Confussion Matrix
from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score

#making the metrixs
cf=confusion_matrix(y_test,lr.predict(x_test_scaled))

#Seeing the Heatmap
sns.heatmap(cf,annot=True)

#precision score
lr_pr=precision_score(y_test,lr.predict(x_test_scaled),average='weighted')*100
#91.11508348888172

#Recall Score
lr_re=recall_score(y_test,lr.predict(x_test_scaled),average='weighted')*100
#91.125

#F1 Score
lr_f1=f1_score(y_test,lr.predict(x_test_scaled),average='weighted')*100
#91.10252994848918

# 2 Decession Tree Classifier
from sklearn.tree import DecisionTreeClassifier

#Making the Model
dtc=DecisionTreeClassifier(criterion='entropy',max_depth=6,splitter='best')
dtc.fit(x_train_scaled,y_train)

#Checking the score
dtc_score=dtc.score(x_test_scaled,y_test)*100
#88.9375

#Performing the Hyperperameter tunning
from sklearn.model_selection import GridSearchCV

#making the tunning
df={"criterion":["gini","entropy","log_loss"],
    "splitter":["best","random"],
    "max_depth":[i for i in range(2,20)]}

#making the model and fit
gd=GridSearchCV(DecisionTreeClassifier(),param_grid=df)
gd.fit(x_train_scaled,y_train)

#seeing the best parameter
gd_param=gd.best_params_
#{'criterion': 'entropy', 'max_depth': 6, 'splitter': 'best'}

#seeing the socre
gd_score=gd.best_score_
#87.54687499999999

#Making the tree graph
from sklearn.tree import plot_tree
#plot_tree(dtc)

#checking the cross validation
cv_score=cross_val_score(DecisionTreeClassifier(max_depth=6),x_train_scaled,y_train,cv=5)

#Soritng the score
cv_score.sort()
#[85.9375   85.9375   87.109375 87.421875 88.046875]

# 3 Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

#making the model
rd=RandomForestClassifier()
rd.fit(x_train_scaled,y_train)

#checking the score
rd_score=rd.score(x_test_scaled,y_test)*100
#90.125

#making the confussion matrixs
cf1=confusion_matrix(y_test,rd.predict(x_test_scaled))

#Confussion matrixs
#sns.heatmap(cf1,annot=True)

#precession score
rd_pr=precision_score(y_test,rd.predict(x_test_scaled),average='weighted')*100
#89.85918059639012

#Recall Score
rd_rc=recall_score(y_test,rd.predict(x_test_scaled),average='weighted')*100
#89.8125

#fi_score
rd_f1=f1_score(y_test,rd.predict(x_test_scaled),average='weighted')*100
#89.72647214189868

#Checking the cross validation
cv_score=cross_val_score(RandomForestClassifier(),x_train_scaled,y_train,cv=5)

#sorting the score
cv_score.sort()
#[87.421875 87.5      88.359375 88.671875 88.828125]

#Comapare the scores with graphs
##curacies = [91.125, dtc_score, rd_score]
#plt.figure(figsize=(8, 5))
#sns.barplot(x=models, y=accuracies)
#plt.title('Model Accuracy Comparison', fontsize=14)
#plt.ylabel('Accuracy (%)', fontsize=12)
#plt.xlabel('Classification Model', fontsize=12)
#plt.ylim(0, 100)
#plt.show()

#models = ['Linear Regression', 'Decision Tree Regression', 'Random Forest Regression ']
#accuracies = [94.14521829480064, 93.97543227214766, 97.77823782277677]
#plt.figure(figsize=(8, 5))
#sns.barplot(x=models, y=accuracies)
#plt.title('Model Accuracy Comparison', fontsize=14)
#plt.ylabel('Accuracy (%)', fontsize=12)
#plt.xlabel('Regression Model', fontsize=12)
#plt.ylim(0, 100)
#plt.show()

#Saving the models
#Regression
joblib.dump(le, 'linear_regression.pkl')
joblib.dump(rf, 'random_forest_regression.pkl')
joblib.dump(dt, 'decession_tree_regression.pkl')

#Saiving the Scaller
joblib.dump(ss, 'standard_scaler.pkl')

#Classification
joblib.dump(lr, 'logistic_regression.pkl')
joblib.dump(dtc, 'decession_tree_classification.pkl')
joblib.dump(rd, 'random_forest_classification.pkl')

print("All Model Saved Succefully!")