#  for reading csv files

import pandas as pd

df = pd.read_csv('gdppercapita_us_inflation_adjusted.csv').head(2)
print(df)
