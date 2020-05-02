import pandas as pd

def read_adult():
    #Lecture des fichiers csv d'entrainement et de test
    adult_data = pd.read_csv("data/adult.data", sep=" *, *", header=None, na_values='?')
    adult_test = pd.read_csv("data/adult.test", sep=" *, *", skiprows=1, header=None, na_values='?')

    #Ajout des entêtes
    adult_data.columns = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"]
    adult_test.columns = adult_data.columns

    population_data = adult_data.fnlwgt.sum()
    population_test = adult_test.fnlwgt.sum()
    #print(population_data)
    #print(population_test)

    #Supprimer le caractère "." de la colonne income du jeu de test
    adult_test.income = adult_test.income.str.split(".", expand=True)[0]

    #Fusion des deux jeux de données 
    adult = pd.concat((adult_data, adult_test), axis=0)

    #Conversion des variables qualitatives en category
    adult.workclass = pd.Categorical(adult.workclass)
    adult.education = pd.Categorical(adult.education)
    adult["marital-status"] = pd.Categorical(adult["marital-status"])
    adult.occupation = pd.Categorical(adult.occupation)
    adult.relationship = pd.Categorical(adult.relationship)
    adult.race = pd.Categorical(adult.race)
    adult.sex = pd.Categorical(adult.sex)
    adult["native-country"] = pd.Categorical(adult["native-country"])
    adult.income = pd.Categorical(adult.income)
    
    #Ajout variable capital qui fusionne les colonnes capital-gain et capital-loss
    def capital(row):
        if row["capital-gain"] > 0:
            capital = row["capital-gain"]
        else :
            capital = -row["capital-loss"]
        return capital
    #adult["capital"] = adult.apply(capital, axis=1)

    return adult