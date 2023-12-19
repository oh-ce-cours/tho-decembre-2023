import pandas as pd

df = pd.read_csv('demo_excel.csv', delimiter=";", decimal=",")
print(df.Valeur1.describe())