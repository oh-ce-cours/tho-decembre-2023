# https://realpython.com/python-data-cleaning-numpy-pandas/

import pandas as pd

olympics_url = "https://raw.githubusercontent.com/realpython/python-data-cleaning/master/Datasets/olympics.csv"
olympics_df = pd.read_csv(
    olympics_url, header=1
)  # la première ligne ne nous intéresse pas, le header est dans la 2eme

# on renomme les colonnes
columns_rename = {
    "Unnamed: 0": "Country",
    "? Summer": "Summer Olympics",
    "01 !": "Gold",
    "02 !": "Silver",
    "03 !": "Bronze",
    "? Winter": "Winter Olympics",
    "01 !.1": "Gold.1",
    "02 !.1": "Silver.1",
    "03 !.1": "Bronze.1",
    "? Games": "# Games",
    "01 !.2": "Gold.2",
    "02 !.2": "Silver.2",
    "03 !.2": "Bronze.2",
}
olympics_df.rename(columns=columns_rename, inplace=True)


# on affiche les groupes par nombre de participation
for k, v in olympics_df.groupby("# Games"):
    print("Number of participations: {}".format(k))
    print(
        "  * " + "\n  * ".join(v.Country.values)
    )  # un peu de manipulation de strings pour formater les résultats


# on cherche si les pays suivants sont dans le dataset
for country in ["Germany", "France", "Monaco"]:
    print(
        olympics_df[olympics_df.Country.str.contains(country, regex=False)]
    )  # il faut utiliser le `.str.contains` pour faire l'équivalent du `in`


# on affiche le bar plot des 10 pays qui ont gagné le plus de médailles
top_10 = (
    olympics_df.drop(146)
    .sort_values("Gold", ascending=False)
    .head(10)[["Country", "Gold"]]
)

## on ne garde que les noms jusqu'à la paranthèse ouvrante s'il y en a une
top_10["Country"] = top_10.Country.str.extract(
    r"(.*) \("
)  # tester ici : https://regex101.com/

top_10.plot.bar(x="Country", y="Gold")


# on affiche les 10 pays qui ont gagnés le plus de médailles en moyenne
all_without_summary = olympics_df.drop(146)
all_without_summary["Mean"] = all_without_summary.Gold / all_without_summary["# Games"]

top10 = all_without_summary.sort_values("Mean", ascending=False).head(15)[
    ["Country", "Gold", "Mean"]
]

top10["Country"] = top10.Country.str.extract(
    r"(.*) \("
)  # tester ici : https://regex101.com/

top10.plot.bar(x="Country", y="Gold")

