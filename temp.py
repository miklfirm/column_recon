import dask.dataframe as dd
import pandas as pd

df = dd.read_csv("original_list.txt")
print(df.head())
# dff = pd.read_csv("original_list.txt")

# n_rows = df.shape[0].compute()
# print(df.head())
