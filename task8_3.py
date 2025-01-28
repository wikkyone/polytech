import pandas as pd


def make_dataframe(data, indexes):
    df = pd.DataFrame(data=data, index=indexes)
    return df


print(make_dataframe({"Олег": 17, "Миша": 19, "Витя": 21}, indexes=["возраст"]))
