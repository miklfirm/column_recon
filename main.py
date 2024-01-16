import pandas as pd
from dask import dataframe as dd

filtered_df = pd.DataFrame()
df_original = pd.read_csv("original_list.txt", on_bad_lines='skip', header=None)
df_search = pd.read_csv("search_list.txt", on_bad_lines='skip', header=None)


for i in range(0, len(df_search)):
    """
    Function create new DataFrame with finded words in original_list from search_list
    """
    filtered_df_temp = df_original.loc[df_original[0].str.contains(df_search[0][i])]
    filtered_df = filtered_df._append(filtered_df_temp)

filtered_df.to_csv("output_list.txt", index=False)

# print(df_search)
# print(filtered_df)
# print(df_output)