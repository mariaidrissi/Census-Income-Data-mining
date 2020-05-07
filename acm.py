from merge import *
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import prince

#Lecture des données et stockage des variables qualitatives qu'on souhaite utiliser pour l'analyse dans adult_qual
adult = read_adult()
adult["US-born"] = (adult["native-country"] == "United-States")
adult_qual = adult[['marital-status', 'relationship']]

#Tableau Disjonctif Complet (tdc) de dimension n (nombre d'individus) * m (nombre total de modalités)
#tdc = pd.DataFrame(pd.get_dummies(adult_qual, dtype=int))
#n, p = adult_qual.shape
#m = tdc.shape[1]
#print(tdc.head())

#Calcul pour chaque modalité du nombre d'individus la possédant
#ns = pd.DataFrame(tdc.sum(axis=0)).reset_index()
#ns.rename(columns={"index" : "modalite", 0 : "nombre"}, inplace=True)
#print(ns)

#Calcul de la distance du chi2 entre chaque individu
# distances = list()
# for i in range(n):
#     for j in range(i, n):         
#         temp = 0
#         for s in range(m):
#             temp += (tdc.iloc[i, s] - tdc.iloc[j, s])**2 / ns["nombre"][s] 
#         distances.append(n/p * temp)

#Initialisation de l'ACM
mca = prince.MCA(
    n_components=12, #Nombre d'axes
    n_iter=10
)
mca = mca.fit(adult_qual)

#On stocke les coordonnées des données transformées
adult_qual_mca = mca.transform(adult_qual)

#Représentation graphique de l'ACM
ax = mca.plot_coordinates(
    X=adult_qual,
    ax=None,
    x_component=0, #1er axe à utiliser pour l'abscisse
    y_component=1, #2ème axe à utiliser pour l'ordonnée
    show_column_labels=True
)
plt.show()
print(mca.explained_inertia_)

#Représentation graphique de l'inertie expliquée par chaque axe de l'ACM
plt.clf()
def plot_bar_x():
    # this is for plotting purpose
    label = range(len(mca.explained_inertia_))
    index = np.arange(len(label))
    plt.bar(index, mca.explained_inertia_)
    plt.xlabel('Axe')
    plt.ylabel("Part d'inertie expliquée")
    plt.xticks(index, label)
    plt.title("Part d'inertie expliquée par axe")
    plt.show()
plot_bar_x()