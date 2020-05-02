from merge import *
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import prince

#Lecture des données et stockage des variables qualitatives dans adult_qual
adult = read_adult()
adult["US-born"] = (adult["native-country"] == "United-States")
adult_qual = adult[['workclass', 'marital-status', 'occupation', 'relationship', 'race', 'sex']]

#Tableau Disjonctif Complet (tdc) de dimension n (nombre d'individus) * m (nombre total de modalités)
tdc = pd.DataFrame(pd.get_dummies(adult_qual, dtype=int))
n, p = adult_qual.shape
m = tdc.shape[1]
#print(tdc.head())

#Calcul pour chaque modalité du nombre d'individus la possédant
ns = pd.DataFrame(tdc.sum(axis=0)).reset_index()
ns.rename(columns={"index" : "modalite", 0 : "nombre"}, inplace=True)
#print(ns)

#Calcul de la distance du chi2 entre chaque individu
distances = list()
for i in range(n):
    for j in range(i, n):         
        temp = 0
        for s in range(m):
            temp += (tdc.iloc[i, s] - tdc.iloc[j, s])**2 / ns["nombre"][s] 
        distances.append(n/p * temp)      

print(distances)
#mca = prince.MCA()
#mca = mca.fit(adult_qual)
#mca = mca.transform(adult_qual)
#print(mca)