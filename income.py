from merge import *
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

adult = read_adult()
adult_qual = adult[["marital-status", "sex", "income"]]
print(adult.info())

adult["US-born"] = (adult["native-country"] == "United-States")

#income
sns.catplot(
    x="income",
    kind="count",
    data=adult
)
plt.title("Distribution de la variable income")
plt.show()

#education vs education-num
ax = sns.barplot(
    x="education",
    y="education-num",
    data=adult
)
ax.set_title("education vs education-num")
ax.set_xticklabels(labels=ax.get_xticklabels(), rotation=45)
#plt.show()

#Analyse des variables quantitatives
#table_qual = pd.pivot_table(adult_qual, index=["sex", "marital-status"], columns=["income"], aggfunc=np.sum)
#print(table_qual)

#age vs income
plt.clf()
sns.violinplot(
    x="income",
    y="age",
    data=adult
)
plt.title("age vs income")
#plt.show()

#fnlwgt
plt.clf()
ax = sns.violinplot(
    x="income",
    y="fnlwgt",
    data=adult
)
plt.title("fnlwgt vs income")
#plt.show()

#education-num
plt.clf()
sns.violinplot(
    x="income",
    y="education-num",
    data=adult
)
plt.title("education-num vs income")
#plt.show()

#capital-gain
plt.clf()
sns.violinplot(
    x="income",
    y="capital-gain",
    data=adult
)
plt.title("capital-gain vs income")
#plt.show()


#capital-loss
plt.clf()
sns.violinplot(
    x="income",
    y="capital-loss",
    data=adult
)
plt.title("capital-loss vs income")
#plt.show()

#capital-gain vs capital-loss
plt.clf()
sns.scatterplot(
    x="capital-gain",
    y="capital-loss",
    data=adult,
    alpha=0.1
)
plt.title("capital-loss vs capital-gain")
#plt.show()

#capital vs income
# plt.clf()
# sns.violinplot(
#     x="income",
#     y="capital",
#     data=adult
# )
# plt.title("capital vs income")
#plt.show()

#hours-per-week
plt.clf()
sns.boxplot(
    x="income",
    y="hours-per-week",
    data=adult
)
plt.title("hours-per-week vs income")
#plt.show()

plt.clf()
sns.violinplot(
    x="income",
    y="hours-per-week",
    data=adult
)
plt.title("hours-per-week vs income")
#plt.show()

#hours-per-week-cat
def hoursPerWeekCat(row):
    if row["hours-per-week"] < 35 :
        hoursPerWeekCat = "<35"
    elif row["hours-per-week"] < 40 :
        hoursPerWeekCat = "35-40"
    elif row["hours-per-week"] <= 50 :
        hoursPerWeekCat = "40-50"
    else :
        hoursPerWeekCat = ">50"
    return hoursPerWeekCat
adult["hours-per-week-cat"] = adult.apply(hoursPerWeekCat, axis=1)
adult["hours-per-week-cat"] = pd.Categorical(
    adult["hours-per-week-cat"],
    categories=["<35", "35-40", "40-50", ">50"],
    ordered=True
)
plt.clf()
sns.catplot(
    x="hours-per-week-cat",
    kind="count",
    hue="income",
    data=adult
)
plt.title("hours-per-week-cat vs income")
#plt.show()

#Analyse des variables qualitatives
#workclass
plt.clf()
sns.catplot(
    x="workclass",
    kind="count",
    hue="income",
    data=adult
)
plt.title("workclass vs income")
plt.xticks(rotation=45)
#plt.show()

#education
plt.clf()
sns.catplot(
    x="education",
    kind="count",
    hue="income",
    data=adult
)
plt.title("education vs income")
plt.xticks(rotation=45)
#plt.show()

#marital-status
plt.clf()
sns.catplot(
    x="marital-status",
    kind="count",
    hue="income",
    data=adult
)
plt.title("marital-status vs income")
plt.xticks(rotation=45)
#plt.show()

#occupation
plt.clf()
sns.catplot(
    x="occupation",
    kind="count",
    hue="income",
    data=adult
)
plt.title("occupation vs income")
plt.xticks(rotation=90)
#plt.show()

#relationship
plt.clf()
sns.catplot(
    x="relationship",
    kind="count",
    hue="income",
    data=adult
)
plt.title("relationship vs income")
plt.xticks(rotation=45)
#plt.show()

#race
plt.clf()
sns.catplot(
    x="race",
    kind="count",
    hue="income",
    data=adult
)
plt.title("race vs income")
plt.xticks(rotation=45)
#plt.show()

#sex
plt.clf()
sns.catplot(
    x="sex",
    kind="count",
    hue="income",
    data=adult
)
plt.title("sex vs income")
plt.xticks(rotation=45)
#plt.show()

#native-country
plt.clf()
sns.catplot(
    y="US-born",
    x="income",
    data=adult,
    kind="bar"
)
plt.title("US-born vs income")
#plt.xticks(rotation=45)
#plt.show()