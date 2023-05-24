import pandas as pd

data = pd.read_csv("glass.csv")

print(data.dropna()["Na"].astype(int))