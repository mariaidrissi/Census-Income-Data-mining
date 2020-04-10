import pandas as pd

#Lecture des fichiers csv d'entrainement et de test
adult_data = pd.read_csv("data/adult.data", sep=",", header=None)
adult_test = pd.read_csv("data/adult.test", sep=",", skiprows=1, header=None)

#Ajout des entêtes
adult_data.columns = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capitol-loss", "hours-per-week", "native-country", "income"]
adult_test.columns = adult_data.columns

#Supprimer le caractère "." de la colonne income du jeu de test
adult_test.income = adult_test.income.str.split(".", expand=True)[0]

#Fusion des deux jeux de données 
adult = pd.concat((adult_data, adult_test), axis=0)