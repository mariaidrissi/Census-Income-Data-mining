import pandas as pd
from collections import namedtuple
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

import merge

def _chi2_metric(x, y, **kwargs):
    """
    Calcule la distance du chi2 entre deux individus x et y issus d'un tableau de contingence
    """
    nb_modalites = len(x)
    n = kwargs.get("n", None)
    nb_variables = kwargs.get("nb_variables", None)
    count_p_modalites = kwargs.get("count_p_modalites", None)
    d2 = 0
    for i in range(nb_modalites):
        if count_p_modalites["nombre"][i] != 0:
            d2 += (x[i] - y[i])**2 / count_p_modalites["nombre"][i]
    d2 = d2 * n / nb_variables
    return d2

#Lecture des données
adult = merge.read_adult()
n = adult.shape[0]
adult["US-born"] = (1 if adult.iloc[i, "native-country"] == "United-States" else 0 for i in range(n))
adult_qual = adult[['occupation', 'workclass', 'marital-status', 'relationship', 'race', 'sex', 'US-born']]
#adult_qual = adult_qual.dropna()
income = adult.loc[:, "income"]

#Calcul de la matrice de contingence
adult_contingency = pd.DataFrame(pd.get_dummies(adult_qual, dtype=int))
n, nb_modalites = adult_contingency.shape
nb_variables = adult_qual.shape[1]
adult_contingency.columns = range(nb_modalites)

#Comptage pour chaque modalité
count_p_modalites = pd.DataFrame(adult_contingency.sum(axis=0)).reset_index()
count_p_modalites.rename(columns={"index" : "modalite", 0 : "nombre"}, inplace=True)

#Séparation du jeu de données
X_train, X_val, y_train, y_val = train_test_split(adult_contingency, income)

#Initialisation du KNearestNeighbors
n_neighbors = 10
args = {"n" : n, "nb_variables" : nb_variables, "count_p_modalites" : count_p_modalites}
#cls = KNeighborsClassifier(n_neighbors=n_neighbors, metric=_chi2_metric, metric_params=args)
cls = KNeighborsClassifier(n_neighors=n_neighbors)

#Application du modèle
cls.fit(X_train, y_train)
y_predict = cls.predict(X_val)

#Calcul et sauvegarde de la précision
acc = accuracy_score(y_val, y_predict)
with open("data/accuracy.txt", "w+") as f:
    f.write("Accuracy : " + str(acc))
print(acc)

#Sauvegarde des étiquettes
y_predict = pd.Series(y_predict)
y_val = y_val.reset_index().drop(columns="index", axis=1)
result = pd.concat([y_val, y_predict], axis=1)
result.columns = ["y_val", "y_predict"]
result.to_csv("data/result.csv")