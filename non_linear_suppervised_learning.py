#decession tree 
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/Social_Network_Ads.csv")
he=dataset.head(3)

#droping 2 columns
dataset.drop(["User ID","Gender"],axis=1,inplace=True)
he=dataset.head(3)

#checking the null vlaues
nl=dataset.isnull().sum()

#making dependent and independent variable
x=dataset.iloc[:,:-1]
y=dataset["Purchased"]

#scalling the dataset
from sklearn.preprocessing import StandardScaler

#mkaing the object ,fitting andn transforming the dataset
sc=StandardScaler()
x=pd.DataFrame(sc.fit_transform(x), columns=x.columns)

#seeing the linear seperation of dataset
#sns.scatterplot(x="Age",y="EstimatedSalary",hue="Purchased",data=dataset)
#non linear seperation of dataset

#importing the train and test split
from sklearn.model_selection import train_test_split

#performing train & test split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#importing the decission tree classifier
from sklearn.tree import DecisionTreeClassifier

#making the object and fitting the model
dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)

#checking the score
sc=dt.score(x_test,y_test)*100
#83.75

#making the dession tree
from sklearn.tree import plot_tree
plt.figure(figsize=(20,15))
plot_tree(dt)
plt.show()
#
#2 model
dt1=DecisionTreeClassifier(criterion="entropy")
dt1.fit(x_train,y_train)

#checking the score for 2 modle
sc1=dt1.score(x_test,y_test)*100
#83.75 #no major defreence

#making teh graph for non-linear seperation
#from mlxtend.plotting import plot_decision_regions

#making the graph for it 
#plot_decision_regions(x.to_numpy(),y.to_numpy(),clf=dt)
plt.show()"""

#decission tree("pre puring")
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/Social_Network_Ads.csv")
he=dataset.head(3)

#droping 2 columns
dataset.drop(["User ID","Gender"],axis=1,inplace=True)
he=dataset.head(3)

#checking the null vlaues
nl=dataset.isnull().sum()

#making dependent and independent variable
x=dataset.iloc[:,:-1]
y=dataset["Purchased"]

#scalling the dataset
from sklearn.preprocessing import StandardScaler

#mkaing the object ,fitting andn transforming the dataset
sc=StandardScaler()
x=pd.DataFrame(sc.fit_transform(x), columns=x.columns)

#importing the train and test split
from sklearn.model_selection import train_test_split

#performing train & test split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#importing the decission tree classifier
from sklearn.tree import DecisionTreeClassifier

#making the object and fitting the model
dt=DecisionTreeClassifier(max_depth=2)
dt.fit(x_train,y_train)

#checking the score
sc=dt.score(x_test,y_test)*100,dt.score(x_train,y_train)*100
#(90.0, 93.4375)[5]
#(91.25, 91.875)[2]
print(sc)

#making the tree
from sklearn.tree import plot_tree
plt.figure(figsize=(20,20))
plot_tree(dt)
plt.show()

#making the decision regions 
#making teh graph for non-linear seperation
from mlxtend.plotting import plot_decision_regions

#making the graph for it 
#plot_decision_regions(x.to_numpy(),y.to_numpy(),clf=dt)

#Dession Tree(post Puring)
#gives all the score and we have to check it
for i in range(1,20):
    dt1=DecisionTreeClassifier(max_depth=i)
    dt1.fit(x_train,y_train)
    #print(dt1.score(x_train,y_train)*100,dt1.score(x_test,y_test)*100,i) """

#decission tree(Regression)
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/house_price_regression_dataset.csv")
he=dataset.head(3)

#making the pair plot to see the linearty
#sns.pairplot(data=dataset)

#checking the null
nl=dataset.isnull().sum()
#no null

#making the dependent and independent variable
x=dataset.iloc[:,:-1]
y=dataset["House_Price"]

#importing the train and test split
from sklearn.model_selection import train_test_split

#making train and test split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#making decission tree
from sklearn.tree import DecisionTreeRegressor,plot_tree

#making the tree
dt=DecisionTreeRegressor()
dt.fit(x_train,y_train)

#checking the score
sc=dt.score(x_test,y_test)*100,dt.score(x_train,y_train)*100
#(91.72786565347258, 100.0)

#graph for tree
plot_tree(dt)
plt.show()"""

#k_nearestNeighbour(Classification)
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/Social_Network_Ads.csv")
he=dataset.head(3)

#checking the null values
nl=dataset.isnull().sum()

#droping the columns 
dataset.drop(["User ID","Gender"],axis=1,inplace=True)
he=dataset.head(3)

#making dependent and independent variable
x=dataset.iloc[:,:-1]
y=dataset["Purchased"]

#seeing the graph for seperation
sns.scatterplot(x="Age",y="EstimatedSalary",data=dataset,hue="Purchased")

#scalling the dataset
from sklearn.preprocessing import StandardScaler

#filling and transforming the data
sc=StandardScaler()
sc.fit(x)
x=pd.DataFrame(sc.transform(x),columns=x.columns)
#data is scalled

#importing the train and test split
from sklearn.model_selection import train_test_split

#making the train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#importing the kneighbour ilbrary
from sklearn.neighbors import KNeighborsClassifier

#making the model and fiting it
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)

#checking the score
sc=knn.score(x_test,y_test)*100,knn.score(x_train,y_train)*100
#91.25, 92.5

#checking neighbour value from loop
for i in range(1,30):
    knn1=KNeighborsClassifier(n_neighbors=i)
    knn1.fit(x_train,y_train)
    #print(knn1.score(x_train,y_train)*100,knn1.score(x_test,y_test)*100,i)

#checking the prediction
pr=knn.predict([[0.797057,-0.844019]])

#making the decession regions
from mlxtend.plotting import plot_decision_regions

#making the graph
plot_decision_regions(x.to_numpy(),y.to_numpy(),clf=knn)
plt.show()"""

#Knearestneighbour(Regression)
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/placement.csv")
he=dataset.head(3)

#checkig the null vlaues
nl=dataset.isnull().sum()

#making dpedent and independent variable
x=dataset.iloc[:,:-1]
y=dataset["placement"]

#importing the train and test
from sklearn.model_selection import train_test_split

#making train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#importing the kneighbourregression
from sklearn.neighbors import KNeighborsRegressor

#making the model
knn=KNeighborsRegressor(n_neighbors=5)
knn.fit(x_train,y_train)

#checking the score
sc=knn.score(x_test,y_test)*100
print(sc)"""

#support vector machine(Classification)
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/placement.csv")
de=dataset.head(3)

#seeing the linear seperation
#sns.scatterplot(x="cgpa",y="iq",data=dataset,hue="placement")

#making the dependent and independent variable
x=dataset.iloc[:,:-1]
y=dataset["placement"]

#importing the train and test split
from sklearn.model_selection import train_test_split

#making the train and test split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

#importing the svm
from sklearn.svm import SVC

#making the model and bit
sv=SVC(kernel="linear")
sv.fit(x_train,y_train)

#checking the score
sc=sv.score(x_test,y_test)*100,sv.score(x_train,y_train)*100
#(95.0, 91.25)

#making the linear line 
from  mlxtend.plotting import plot_decision_regions

#mking thr graph
plot_decision_regions(x.to_numpy(),y.to_numpy(),clf=sv)
plt.show()"""

#support vecotr machine(regression)
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/polynomial_regression_data.csv")
he=dataset.head(3)

#seeing the lineaity of dataset
#sns.scatterplot(x="X",y="y",data=dataset)

#making the dependent and independent variable
x=dataset[["X"]]
y=dataset["y"]

#importing the train and test split
from sklearn.model_selection import train_test_split

#making the train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=42)

#importnig the svm
from sklearn.svm import SVR

#making the model
sv=SVR(kernel='poly')
sv.fit(x_train,y_train)

#cheking the score
sc=sv.score(x_test,y_test)*100,sv.score(x_train,y_train)*100
#(95.46185922622065, 93.81217510117544)"poly"

#making decission line
sns.scatterplot(x="X",y="y",data=dataset)
plt.plot(dataset["X"],sv.predict(x),color="red")
plt.show()"""