import pandas as pd

df = pd.read_csv('demo_excel.csv', delimiter=";", decimal=",")
print(df.Valeur1.describe())

infos_train_1 = df[df["Numero de train"] == 1]

