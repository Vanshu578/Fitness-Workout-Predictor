#Missing values and how to find it

"""import pandas as pd  #importing the assential libraries
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv") #load dataset
he=dataset.head(3)  #displaying the three data of starting
sh=dataset.shape    #displaying the shape(rows and columns)
nl=dataset.isnull().sum() #displaying the total numm values of columns
percentage_column=(dataset.isnull().sum()/dataset.shape[0])*100 #displaying the null values of each columns in percentage %
total_null=dataset.isnull().sum().sum() #displaying the total null values of dataset
total_null_percentage=(dataset.isnull().sum().sum()/(dataset.shape[0]*dataset.shape[1])) # displaying the total null vlaues in percentage
nonull=dataset.notnull().sum().sum() #displaying the not null vlaues
print(nonull)"""

#handling missing values(drop)

"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dataset = pd.read_csv("C:/Users/User/Desktop/loan.csv")
he=dataset.head(4)
sh=dataset.shape
sns.heatmap(dataset.isnull())
dataset.drop(columns=["Credit_History"],inplace=True)
new_data=dataset.shape
d_row=dataset.dropna(inplace=True)
new_null=dataset.isnull().sum().sum()
new_data1=dataset.shape
n_percentage=((614-523)/614)*100
print(n_percentage)"""

#Handling Missing Vlaues (inputing category data)
"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
d1=pd.read_csv("C:/Users/User/Desktop/loan.csv")
info=d1.info()
for i in d1.select_dtypes(include="str").columns:
    d1[i]=d1[i].fillna(d1[i].mode()[0],inplace=True)
print(d1.isnull().sum())"""

#Handling Missing Vlaues(Scikit-learn)
"""import pandas as pd
d1=pd.read_csv("C:/Users/User/Desktop/loan.csv")
h1=d1.head(3)
nl=d1.isnull().sum()
seeing_columns=d1.select_dtypes(include="float64").columns
from sklearn.impute import SimpleImputer
si=SimpleImputer(strategy="mean")
ar=si.fit_transform(d1[['CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
       'Credit_History']])
nd=pd.DataFrame(ar,columns=d1.select_dtypes(include="float64").columns)
print(nd.isnull().sum())"""

#handling missing value with the (inputing category data) & (Scikit-learn)
"""import pandas as pd
d1=pd.read_csv("C:/Users/User/Desktop/loan.csv")
h1=d1.head(3)
nl=d1.isnull().sum()
seeing_columns=d1.select_dtypes(include="float64").columns
for i in d1.select_dtypes(include="str").columns:
    d1[i]=d1[i].fillna(d1[i].mode()[0],inplace=True)
from sklearn.impute import SimpleImputer
si=SimpleImputer(strategy="mean")
ar=si.fit_transform(d1[['CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
       'Credit_History']])
nd=pd.DataFrame(ar,columns=d1.select_dtypes(include="float64").columns)
d1[['CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
       'Credit_History']]=nd
print(d1.isnull().sum())"""

#one hot Encoding & dammy variables
#used to convert categorical data into numerical form
##not working
"""import pandas as pd
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")
h1=dataset.head(3)
dataset['Gender']=dataset['Gender'].fillna(dataset['Gender'].mode()[0],inplace=True)
dataset['Married']=dataset['Married'].fillna(dataset['Married'].mode()[0],inplace=True)
en_data=dataset[["Gender","Married"]]
dm=pd.get_dummies(en_data)
dm_info=pd.get_dummies(en_data).info()
from sklearn.preprocessing import OneHotEncoder
oHe=OneHotEncoder()
ar=oHe.fit_transform(en_data).toarray()
ar1=pd.DataFrame(ar,columns=['Gender_Female','Gender_Male','Married_No','Married_Yes'])
oHe=OneHotEncoder(drop="first")
print(oHe)"""

#Label encoding
"""import pandas as pd
df=pd.DataFrame({"name":['wscube','cow','cat','dog','block']})
#importing the library
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
le.fit_transform(df["name"])
df["en_name"]=le.fit_transform(df["name"])


#setting the new dataset
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")
dl=dataset["Property_Area"].unique()
la=LabelEncoder()
la.fit(dataset["Property_Area"])
la1=la.transform(dataset["Property_Area"])
la2=dataset["Property_Area"]=la.transform(dataset["Property_Area"])
print(dataset["Property_Area"].unique())"""

#ordinal Encoding(Sciki Learn , Map Function)
"""import pandas as pd
df=pd.DataFrame({"Size":["s","m","i","xi","s","m","i","s","s","i","xi","m"]})
ord_data=[["s","m","i","xi"]]

#importing the library
from sklearn.preprocessing import OrdinalEncoder
oe=OrdinalEncoder(categories=ord_data)
oe.fit(df[["Size"]])
df["Size_en"]= oe.transform(df[["Size"]])

ord_data1={"s":0,"m":1,"i":2,"xi":3}
df["Size"].map(ord_data1)
df["Size_en_map"]=df["Size"].map(ord_data1)
print(df)"""

#performing the ordinal encoding on a dataset
"""import pandas as pd
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")
hi=dataset.head(3)

#cheking the vlaues
vl=dataset["Property_Area"].unique()

#setting the order
en_data_ord=[["Rural","Semiurban","Urban"]]

#getting the library
from sklearn.preprocessing import OrdinalEncoder

#giving the setted order
oen=OrdinalEncoder(categories=en_data_ord)

#preplacing it with the original dataset
dataset["Property_Area"] = oen.fit_transform(dataset[["Property_Area"]])

#seeing the original dataset
hi1=dataset.head(10)
print(hi1)"""

#Outliner programe
"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Getting the database
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")

#seeing the first 3 data
he=dataset.head(3)

#seeing the dataset maximum and minimum values
dc=dataset.describe() #actualy a part of removal of outliners

#seeing the ouliner of "coapplicantincome" with boxplot
plt.figure(figsize=(10,4))
sns.boxplot(x="CoapplicantIncome",data=dataset)
plt.show()"""

#Outliner Removal using iqr
#data distribution is high and it is not working properly 
"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")
he=dataset.head(3)

#describing the dataset to see the ouliers
dc=dataset.describe()

#seeing the shape of dataset
sh=dataset.shape

#seeing the null values
nl=dataset.isnull().sum()
#coaaplicantincome has no null vlaue

#seeing the oultiers with a help of box-plot
sns.boxplot(x="CoapplicantIncome",data=dataset)

#finding the first quantile(q1)
q1=dataset["CoapplicantIncome"].quantile(0.25)

#rfinding the third quantile(q3)
q3=dataset["CoapplicantIncome"].quantile(0.75)

#Calculating the iqr,min_range,max_range
iqr=q3-q1
min_range=q1-(1.5*iqr)
max_range=q3+(1.5*iqr)

#Removing the ouliers from dataset
new_dataset=dataset[dataset["CoapplicantIncome"]<=max_range]

#seeing the shape of new dataset
sh1=new_dataset.shape

#boxplot for the new dataset after removing the ouliers
sns.boxplot(x="CoapplicantIncome",data=new_dataset)
plt.show()"""

#removing the ouliers with direct method
"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importing the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")
he=dataset.head(3)
sh=dataset.shape

#seeing the graph for outliers with boxplot
sns.boxplot(x="CoapplicantIncome",data=dataset)

#Removing the ouliers with direct method
min_range=dataset["CoapplicantIncome"].mean()-(3*dataset['CoapplicantIncome'].std())
max_range=dataset["CoapplicantIncome"].mean()+(3*dataset['CoapplicantIncome'].std())

#Removing the outliers
new_dataset=dataset[dataset["CoapplicantIncome"]<=max_range]

#seeing the graph after removal of outliers
sns.boxplot(x="CoapplicantIncome",data=new_dataset)

#seeing the new dataset
he1=new_dataset.head(3)

#describing the new dataset
dc1=new_dataset.describe()

#seeing the shape of new dataset
sh1=new_dataset.shape

#removing the ouliers form iqr method
#calculating the first quatrile
q1=new_dataset["CoapplicantIncome"].quantile(0.25)

#calculating the second quartile
q3=new_dataset["CoapplicantIncome"].quantile(0.75)

#calculating the iqr,min,max range
iqr=q3-q1
min_range=q1-(1.5*iqr)
max_range=q3+(1.5*iqr)

#removijg the outliers
new_dataset1=new_dataset[new_dataset["CoapplicantIncome"]<=max_range]

#seeing the shape of dataset after removing the outliers
sh2=new_dataset1.shape
sh1=new_dataset.shape

#seeing the boxplot graph
sns.boxplot(x="CoapplicantIncome",data=new_dataset1)
plt.show()"""

#removing the outliers with the z_score
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")
hi=dataset.head(3)

z_score=(dataset["CoapplicantIncome"]-dataset["CoapplicantIncome"].mean())/(dataset["CoapplicantIncome"].std())

dataset["z_score"]=z_score
dataset[dataset["z_score"]<3]
print(dataset)"""

#feature scaling (standardization)
"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importing the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")
he=dataset.head(3)

#checking the null vlaues
nl=dataset.isnull().sum()

#seeing the ouliers with distplot
sns.displot(dataset["ApplicantIncome"])

#describing the dataset
dc=dataset.describe()

#importing the library
from sklearn.preprocessing import StandardScaler

#fitting the dataset
ss=StandardScaler()
ss.fit(dataset[["ApplicantIncome"]])

#transform the data
ss.transform(dataset[["ApplicantIncome"]])

#filling the result into orignal dataset
dataset["ApplicantIncome_ss"]=pd.DataFrame(ss.transform(dataset[["ApplicantIncome"]]),columns=["x"])

#checking the dataset
he1=dataset.head(3)

#making the subplot for both the graph
plt.figure(figsize=(10,7))
sns.displot(dataset["ApplicantIncome_ss"])

sns.displot(dataset["ApplicantIncome"])
plt.show()"""

#feature scaling(normalization)
"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importing the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")
he=dataset.head(3)

#checking the null vlaues
nl=dataset.isnull().sum()

#describing the dataset
dc=dataset.describe()

#seeing the graph for dataset
sns.displot(dataset["CoapplicantIncome"])

#importing the library
from sklearn.preprocessing import MinMaxScaler

#fitting the data
ms=MinMaxScaler()
ms.fit(dataset[["CoapplicantIncome"]])

#transforming the dataset
dataset["CoapplicantIncome_min"]=ms.transform(dataset[["CoapplicantIncome"]])
he1=dataset.head(3)

#plotting the graphs
plt.figure(figsize=(10,5))
sns.displot(dataset["CoapplicantIncome_min"])
plt.show()"""

#removing the duplicate value
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importing the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")
he=dataset.head(3)

#seeing the duplicated value
dp=dataset.duplicated()

#seeign the shape of dataset
sh=dataset.shape

#removing the duplicate value
dataset.drop_duplicates(inplace=True)

#seeing the shape after removing the duplicated value
sh1=dataset.shape
print(sh1) #no change in the shape after removing the duplicate value"""

#replace and data type change

"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importing the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")
he=dataset.head(3)

#seeing the info of the dataset
inf=dataset.info()

#seeing null vlaues in dataset
nl=dataset.isnull().sum()

#seeing the unique values of "dependent" columns
vl=dataset["Dependents"].value_counts()

#feeling the null vlaues
dataset["Dependents"]=dataset["Dependents"].fillna(dataset["Dependents"].mode()[0],inplace=True)

#seeing the null vlaues after filling the column
nl1=dataset.isnull().sum()

#Replacing the data
dataset["Dependents"]=dataset["Dependents"].replace("3+","3",inplace=True)
vl=dataset["Dependents"].value_counts()

#changing the datatype form object to int64
dataset["Dependents"]=dataset["Dependents"].astype("int64")
inf=dataset.info()
print(inf)"""

#function transformer
"""import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#importing the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/loan.csv")
dataset.head(3)

#seeinf the null vlaues
nl=dataset.isnull().sum()

#plotting the graph with distplot
#sns.displot(dataset["CoapplicantIncome"])

#removing the otliers
q1=dataset["CoapplicantIncome"].quantile(0.25)
q3=dataset["CoapplicantIncome"].quantile(0.75)
iqr=q3-q1
min_r=q1-(1.5*iqr)
max_r=q3+(1.5*iqr)

dataset=dataset[dataset["CoapplicantIncome"]<=max_r]

#checking the graph
#sns.boxplot(x="CoapplicantIncome",data=dataset)

#importing the library
from sklearn.preprocessing import FunctionTransformer

#makin a function
ft=FunctionTransformer(func=np.log1p)

#fitting the data
ft.fit(dataset[["CoapplicantIncome"]])

#trnasforming the data
dataset["CoapplicantIncome_tf"]=ft.transform(dataset[["CoapplicantIncome"]])

#making subplot for both graph
plt.subplot(1,2,1)
sns.displot(dataset["CoapplicantIncome"])
plt.title("Before")

plt.subplot(1,2,2)
sns.displot(dataset["CoapplicantIncome_tf"])
plt.title("After")
plt.show()"""