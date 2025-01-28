import pandas as pd


# Выбранный континент - Asia
def countries_in_continent(csv_name, continent):
    data = pd.read_csv(csv_name)
    data_continent = data[data["continent"] == continent]
    data_non_null = data_continent.fillna(data_continent.min())
    data_non_null.to_csv("CountryOutput.csv")
    return data_non_null
