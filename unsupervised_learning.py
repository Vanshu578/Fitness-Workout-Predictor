#kmean clustering
"""import pandas as pd
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
#plt.show()

#prediction of dataset
kmn=KMeans(n_clusters=3)
dataset["predict"]=kmn.fit_predict(dataset)
he=dataset.head(3)
print(kmn.labels_)

#making graph for cluster
sns.pairplot(data=dataset,hue="predict")
#plt.show()"""

#hierarchical clustering
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/Iris.csv")
he=dataset.head(3)

#droping the columns
dataset.drop(["Id","Species"],axis=1,inplace=True)
he=dataset.head(3)

#seeing the linear seperation
#sns.pairplot(data=dataset)

#importing the library for dendograme
import scipy.cluster.hierarchy as sc

#making the dendograme
#plt.figure(figsize=(20,20))
#sc.dendrogram(sc.linkage(dataset,method='single',metric='euclidean'))
#plt.show()

#making the clusters
from sklearn.cluster import AgglomerativeClustering
ac=AgglomerativeClustering(n_clusters=2,linkage='single')
dataset["predict"]=ac.fit_predict(dataset)
he=dataset.head(3)

#making the graph of clusters
sns.pairplot(data=dataset,hue="predict")
#plt.show()"""

#dbscan cluestring
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_moons

#making x and y variables
x,y=make_moons(n_samples=250,noise=0.05)

#making a dataset 
import pandas as pd
df={"data1":x[:,0], "data2":x[:,1],"output":y}
dataset=pd.DataFrame(df)

#making the graph for linearity
#sns.scatterplot(x="data1",y="data2",data=dataset)
#plt.show()

#imporitng the dbscan library
from sklearn.cluster import DBSCAN

#making model and fitting it
db=DBSCAN(eps=0.2,min_samples=5)
print(db.fit_predict(dataset))

#making the graph to see clustering
#sns.scatterplot(x="data1",y="data2",data=dataset,hue="output")
#plt.show()"""

#silhout score
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the datasset
dataset=pd.read_csv("C:/Users/User/Desktop/Iris.csv")
he=dataset.head(3)

#droping the "species" column for clustering
dataset.drop(["Id","Species"],axis=1,inplace=True)
he=dataset.head(3)

#making the graph to see linear seperation
#sns.pairplot(data=dataset)

#importing the kmeans library
from sklearn.cluster import KMeans

#making clusters
wcss=[]
for i in range(2,21):
    km=KMeans(n_clusters=i,init='k-means++')
    km.fit(dataset)
    wcss.append(km.inertia_)

#making the graph for elbow diagrame
#plt.figure(figsize=(10,5))
#plt.plot([i for i in range(2,21)],wcss,marker="o")
#plt.xlabel("no.of.clusters")
#plt.ylabel("wcss")
#plt.xticks([i for i in range(2,21)])
#plt.grid(axis="x")
#plt.show()

#prediction of dataset
kmn=KMeans(n_clusters=3)
dataset["predict"]=kmn.fit_predict(dataset)
he=dataset.head(3)
#print(kmn.labels_)

#making graph for cluster
#sns.pairplot(data=dataset,hue="predict")
#plt.show()

#imporintg the silhoute score
from sklearn.metrics import silhouette_score

#making the best clusters
ss=[]
no_c=[j for j in range(2,21)]
for i in range(2,21):
    km1=KMeans(n_clusters=i)    
    km1.fit(dataset)
    ss.append(silhouette_score(dataset,km1.labels_))

#making the graph for clusters
plt.plot(no_c,ss)
plt.xlabel("no of cluesters")
plt.ylabel("silhouete score")
plt.xticks(no_c)
plt.grid(axis="x")
plt.show()"""