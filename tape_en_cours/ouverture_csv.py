import pandas as pd

df = pd.read_csv('demo_excel.csv', delimiter=";", decimal=",", parse_dates={'Timestamp': ['Date', 'Heure']}, dayfirst=True)
#print(df.Valeur1.describe())
df.dropna(axis=1, how='all', inplace=True)  # Supprimer les colonnes vides résultant du double point-virgule

infos_train_1 = df[df["Numero de train"] == 1]

# regrouper et faire des stats par train
for num_train, grouped in df.groupby("Numero de train"):
    print(num_train, grouped.Valeur1.mean())
    

# n'affiher que les données après un certain temps
df[df.Timestamp > "2023-12-21 14:13:00"]