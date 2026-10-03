import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
dataset=pd.read_csv("C:/Users/User/Desktop/supermarket_transactions.csv")
he=dataset.head(3)

#seeing the shape 
sh=dataset.shape

#removing the null vlaues and seperating them
market=[]
for i in range(0,dataset.shape[0]):
    cus=[]
    for j in dataset.columns:
        if type(dataset[j][i])==str:
            cus.append(dataset[j][i])
        market.append(cus)
print(market)

#making a single list and collection
l=[]
for i in market:
    for j in i:
        l.append(j)

#importing doing collections
import collections