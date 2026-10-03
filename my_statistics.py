#for mean calculation#
"""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:/Users/User/Desktop/Titanic-Dataset.csv")
dh=df.head(3)
mean=df["Age"].mean()
print("Mean of Age:", mean)
mean1=np.mean(df["Age"])
print("Mean of Age using numpy:", mean1)
sns.histplot(x="Age",data=df)
plt.plot([mean1 for i in range(0,300)],  [i for i in range(0,300)],label="mean")
plt.legend()
plt.show()"""

#for median calculation#
"""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:/Users/User/Desktop/Titanic-Dataset.csv")
dh=df.head(3)
df["Age"]=df["Age"].fillna(df["Age"].mean())
median=np.median(df["Age"])
print(median)"""

#calculating the fare column median and mean with graph# 
"""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:/Users/User/Desktop/Titanic-Dataset.csv")
nl=df.isnull().sum()
median=np.median(df["Fare"])
mean=df["Fare"].mean()
mod=df["Fare"].mode()
sns.histplot(x="Fare",data=df,bins=[i for i in range(0,81,10)])
plt.plot([mean for i in range(0,300)],[i for i in range(0,300)] , c="red" , label="mean")
plt.plot([median for i in range(0,300)],[i for i in range(0,300)] , c="green" , label="median")
plt.plot([mod for i in range(0,300)],[i for i in range(0,300)] , c="black" , label="mod")
plt.legend()
plt.show()"""

#range calculation(range=maximum-minimum)#
"""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:/Users/User/Desktop/Titanic-Dataset.csv")
min_r=df["Age"].min()
max_r=df["Age"].max()
rg=max_r-min_r
print(max_r,min_r)
print(rg)"""

#Mean Absolute Deviation#
"""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:/Users/User/Desktop/Titanic-Dataset.csv")
sec_a = np.array([75,65,73,68,72,67])
sec_b = np.array([90,47,43,96,93,51])
no=np.array([1,2,3,4,5,6])
na=np.mean(sec_a)
nb=np.mean(sec_b)
plt.scatter(sec_a,no,label="sec a")
plt.scatter(sec_b,no,label="sec b")
plt.plot([70,70,70,70,70,70],no,c="green",label="Mean")
plt.legend()
plt.show()"""

#caculate the Mean Absolute Deviation using formula
"""import numpy as np
import pandas as pd
sec_a = np.array([75,65,73,68,72,67])
sec_b = np.array([90,47,43,96,93,51])
na=np.mean(sec_a)
nb=np.mean(sec_b)
mad_a=np.sum(np.abs(sec_a-na))/len(sec_a)
mad_b=np.sum(np.abs(sec_b-nb))/len(sec_b)
print(mad_a,mad_b)"""

#where sd is low we considered that dataset for further manupulation#
#caculation of standard deviation
"""import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/User/Desktop/Titanic-Dataset.csv")
sec_a = np.array([75,65,73,68,72,67])
sec_b = np.array([90,47,43,96,93,51])
sd = np.std(sec_a),np.std(sec_b)
sr=np.var(sec_a),np.var(sec_b)
dc=df.describe()
print(dc)"""

#calculartion of iqr(inter quartile range)
"""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:/Users/User/Desktop/Titanic-Dataset.csv")
dh=df.head(3)
nl=df.isnull().sum()
df["Age"]=df["Age"].fillna(df["Age"].mean())
nl=df.isnull().sum()
pr=np.percentile(df['Age'],25),np.percentile(df['Age'],75),np.percentile(df['Age'],50)
me=np.median(df["Age"])
plt.figure(figsize=(10,10))
sns.boxplot(x="Age",data=df)
plt.show()"""

#caculating the skewness
#not sure about this programe#
"""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:/Users/User/Desktop/Titanic-Dataset.csv")
se=df['Age'].skew()
sns.histplot(x="Age",data=df)
plt.show()
data=np.random.normal(0,100,100)
dt=pd.DataFrame({"x":data})
dt1=dt["x"].skew()
me=np.mean(dt)
md=np.median(dt)
print(me,md)"""

"""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
Data=[2,3,3,4,4,4,5,5,5,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,11,11,12]
df=pd.DataFrame({"x":Data})
de=df["x"].skew()
me=df["x"].mean()
md=df["x"].median()
mo=df["x"].mode()
print(me)
print(md)
print(mo)"""

#calculating the corelation and covariance#
"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:/Users/User/Desktop/tip.csv")
dh=df.head(3)
di=df.info()
dc=df.select_dtypes(["float64","Int64"]).corr()
dc1=df.select_dtypes(["float64","Int64"]).cov()
plt.figure(figsize=(4,3))
sns.heatmap(dc1,annot=True)
plt.show()"""

#calculating the center limit theorem#
# a samll error in programe#
"""import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pop_data=[np.random.randint(10,100)for i in range(10000)]
pop_table=pd.DataFrame({"pop_data":pop_data})
#taking a sample data#
sample_mean=[]
for no_sample in range(60):
    sample_data=[]
    for data in range(500):
        sample_data.append(np.random.choice(pop_data))
        sample_mean.append(np.mean(sample_data))
        sample_M=pd.DataFrame({"Sample_mean":sample_mean})
        sns.kdeplot(x="Sample_mean",data=sample_M)
plt.show()"""

#cacluting and performing hypothesis testing 
#z-test(example 1)
#calculated value is alwayes greater than table value
#when h1 is less (left tail)
#when h1 is greater than(right tail)
#when h1 is not equal(two-tail)
"""import scipy.stats as st
import numpy as np
s_x=90
p_u=82
p_std=20
n=81
ap=0.05
z_cal=(s_x-p_u)/(p_std/np.sqrt(n))
z_table=st.norm.ppf(1-ap)
if z_table < z_cal:
    print("h1 is right")
else:
    print("h0 is right")
print(z_cal)
print(z_table)"""

#T-test(Example 1)
"""import scipy.stats as st
import numpy as np
p_u=150
s_x=148
s_std=5
n=25
t_table=st.t.ppf(0.05,24)
t_cal=(s_x-p_u)/(s_std/np.sqrt(n))
if abs(t_table) < abs(t_cal):
    print("h1 is right")
else:
    print("h0 is right")"""

#Example 2
"""import pandas as pd
import scipy.stats as st
import numpy as np
t_table=st.t.ppf(1-0.025,38)
t_cal=(80-75)/(np.sqrt((25/20)+(36/20)))
if t_table<t_cal:
    print("h1 is right")
else:
    print("h0 is right")"""

#Example 3
#not sure about answer
"""import scipy.stats as st
import numpy as np
t_table=st.t.ppf(1-0.025,19)
before=np.array([50,60,45,65,55,70,40,75,80,65,70,60,50,55,45,75,60,50,65])
After=np.array([60,70,55,75,65,80,50,85,90,70,75,65,55,60,50,80,65,55,70,75])
std_a=np.std(After)
std_b=np.std(before)
mean_a=np.mean(After)
mean_b=np.mean(before)
t_col=(mean_a-mean_b)/np.sqrt((np.square(std_a)/len(After)+(np.square(std_b)/len(before))))
print(t_col)
print(t_table)"""

#chisquare
"""#example 1
import numpy as np
ob=np.array([22,17,20,26,22,13])
ex=np.array([20,20,20,20,20,20])
chi=np.sum(np.square(ob-ex)/ex)
print(chi)"""

#example 2
# expected value not given
# calculating the expected value
#ex_value= sum of column * sum of row / no of sample
"""import numpy as np 
row1=np.array([40,45,25,10])
row2=np.array([35,30,20,30])
sum_r1=np.sum(row1)
sum_r2=np.sum(row2)
sum_col=row1+row2
sum_row=np.array([sum_r1,sum_r2])
exp=[]
for i in sum_row:
    for j in sum_col:
        value=(i*j)/235
        exp.append(value)
        obj=np.array([40,45,25,10,35,30,20,30])
        np.sum(np.square(obj - exp) /exp)
        
"""
#Z-test(1)
"""import pandas as pd
import numpy as np
import scipy.stats as st
u=150
x=148
std=6
n=36
z_table = st.norm.ppf(1-0.025)
z_cal=(x-u)/(std/np.sqrt(n))
if abs(z_cal)>abs(z_table):
    print("h1 is right")
else:
    print("h0 is right")"""

#z-test(2)
"""import numpy as np
import scipy.stats as st
u=75
x=78
std=8
n=40
z_table=st.norm.ppf(1-0.05)
z_cal=(x-u)/(std/np.sqrt(n))
if z_cal>z_table:
    print("h1 is right")
else:
    print("h0 is right")"""

#z_test(3)
"""import numpy as np
import scipy.stats as st
u=1200
x=1180
std=40
z_value= -1.645
n=50
z_cal=(x-u)/(std/np.sqrt(n))
if z_cal<z_value:
    print("h1 is right")
else:
    print("h0 is right")"""

#ztest(4)
"""import numpy as np
import scipy .stats as st
z_table=st.norm.ppf(1-0.025)
u=20
x=19.8
std=1.2
n=36
z_cal=(x-u)/(std/np.sqrt(n))
if z_cal>z_table:
    print("h1 is right")
else:
    print("h0 is right")"""

#ztest(5 and 6)
"""import numpy as np
import scipy.stats as st
z_table=-1.644
u=5000
x=4800
std=600
n=100
z_cal=(x-u)/(std/np.sqrt(n))
if z_cal<z_table:
    print("h1 is right")
else:
    print("h0 is right")"""