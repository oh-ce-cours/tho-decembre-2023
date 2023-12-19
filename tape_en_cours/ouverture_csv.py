import pandas as pd

df = pd.read_csv('demo_excel.csv', delimiter=";", decimal=",", parse_dates={'Timestamp': ['Date', 'Heure']}, dayfirst=True)
#print(df.Valeur1.describe())

# chat gpt
#df = pd.read_csv('demo_excel.csv', delimiter=';', decimal='.', parse_dates={'Timestamp': ['Date', 'Heure']}, dayfirst=True)
df.dropna(axis=1, how='all', inplace=True)  # Supprimer les colonnes vides résultant du double point-virgule

infos_train_1 = df[df["Numero de train"] == 1]

for num_train, grouped in df.groupby("Numero de train"):
    print(num_train, grouped.Valeur1.mean())
    