import pandas as pd

df=pd.read_csv("Advertising.csv")


print(df.head())



print(df.TV.value_counts())
