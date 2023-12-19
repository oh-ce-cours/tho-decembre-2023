import pandas as pd

production_url = "https://data.open-power-system-data.org/time_series/2020-10-06/time_series_30min_singleindex.csv"
df_production = pd.read_csv(production_url)

print(df_production.head())

# création de la série temporelle
df_production.set_index(pd.to_datetime(df_production.utc_timestamp), inplace=True)

# affichage de la génération de 2
df_production[
    ["GB_GBN_solar_generation_actual", "GB_UKM_wind_offshore_generation_actual"]
].plot()

# on remplace les valeurs manquantes
df_production.interpolate(inplace=True, method="linear")

# on regarde la production et la génération, que l'on moyenne sur une année (plus ou moins)
df_production[
    ["GB_GBN_solar_generation_actual", "GB_UKM_wind_offshore_generation_actual"]
].rolling("365d").mean().plot()

