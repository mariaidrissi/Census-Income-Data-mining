import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

#Analyse exploratoire des données pour occupation
pd.options.display.max_rows = 10
print(type(adult))
print(adult.shape) #(48842, 15)
print(adult.head())
print(adult.columns) #Index(['age', 'workclass', 'fnlwgt', 'education', 'education-num','marital-status', 'occupation', 'relationship', 'race', 'sex','capital-gain', 'capitol-loss', 'hours-per-week', 'native-country', 'income'], dtype='object')

#Nombre d'occurences pour chaque variables
print(adult['age'].value_counts())
print(adult['workclass'].value_counts())
print(adult['education'].value_counts())
print(adult['marital-status'].value_counts())
print(adult['occupation'].value_counts())
print(adult['relationship'].value_counts())
print(adult['race'].value_counts())
print(adult['sex'].value_counts())
print(adult['hours-per-week'].value_counts())
print(adult['native-country'].value_counts())
print(adult['income'].value_counts())

#Barplot occupation en fonction du pourcentage sex
x, y, hue = "occupation", "proportion", "sex"
hue_order = ["Male", "Female"]

(adult[x]
 .groupby(adult[hue])
 .value_counts(normalize=True)
 .rename(y)
 .reset_index()
 .pipe((sns.barplot, "data"), x=x, y=y, hue=hue))

plt.xticks(rotation=90)
plt.show()

#Barplot occupation en fonction du pourcentage income
x, y, hue = "occupation", "proportion", "income"
hue_order = ["<=50K", ">50K"]

(adult[x]
 .groupby(adult[hue])
 .value_counts(normalize=True)
 .rename(y)
 .reset_index()
 .pipe((sns.barplot, "data"), x=x, y=y, hue=hue))

plt.xticks(rotation=90)
plt.show()

#Barplot occupation en fonction du pourcentage race
x, y, hue = "occupation", "proportion", "race"
hue_order = ["White", "Black", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other"]

(adult[x]
 .groupby(adult[hue])
 .value_counts(normalize=True)
 .rename(y)
 .reset_index()
 .pipe((sns.barplot, "data"), x=x, y=y, hue=hue))

plt.xticks(rotation=90)
plt.show()

#Barplot occupation en fonction du pourcentage US-born
adult["US-born"]=(adult["native-country"]==" United-States")
x, y, hue = "occupation", "proportion", "US-born"
hue_order = ["True", "False"]

(adult[x]
 .groupby(adult[hue])
 .value_counts(normalize=True)
 .rename(y)
 .reset_index()
 .pipe((sns.barplot, "data"), x=x, y=y, hue=hue))

plt.xticks(rotation=90)
plt.show()

#Counplot de race
sns.countplot(x='race', data=adult)
plt.show()

#Counplot de sex
sns.countplot(x='sex', data=adult)
plt.show()

#Counplot de income
sns.countplot(x='income', data=adult)
plt.show()

#Counplot de relationship
sns.countplot(x='relationship', data=adult)
plt.show()

#Counplot de occupation
sns.countplot(x='occupation', data =adult)
plt.xticks(rotation=90)
plt.show()

#Countplot avec les valeurs absolues
#Qualitatif vs qualitatif
sns.countplot(x="workclass", hue="occupation", data=adult)
plt.xticks(rotation=90)
plt.show()

sns.countplot(x="occupation", hue="workclass", data=adult)
plt.xticks(rotation=90)
plt.show()

sns.percentageplot(x="occupation", hue="sex", data=adult)
plt.xticks(rotation=90)
plt.show()

sns.countplot(x="occupation", hue="income", data=adult)
plt.xticks(rotation=90)
plt.show()

adult["US-born"]=(adult["native-country"]==" United-States")
sns.countplot(x="occupation", hue="US-born", data=adult)
plt.xticks(rotation=90)
plt.show()

sns.countplot(x="occupation", hue="marital-status", data=adult)
plt.xticks(rotation=90)
plt.show()

sns.countplot(x="occupation", hue="relationship", data=adult)
plt.xticks(rotation=90)
plt.show()

sns.countplot(x="occupation", hue="race", data=adult)
plt.xticks(rotation=90)
plt.show()

adult["High-education"]=(adult["education-num"]>= 9)
sns.countplot(x="occupation", hue="High-education", data=adult)
plt.xticks(rotation=90)
plt.show()


#Qualitatif vs quantitatif

sns.barplot(x="occupation", y="age", data=adult)
plt.xticks(rotation=90)
plt.show()

sns.barplot(x="occupation", y="hours-per-week", data=adult)
plt.xticks(rotation=90)
plt.show()

sns.barplot(x="occupation", y="capital-gain", data=adult)
plt.xticks(rotation=90)
plt.show()

sns.baroplot(x="occupation", y="capital-loss", data=adult)
plt.xticks(rotation=90)
plt.show()
