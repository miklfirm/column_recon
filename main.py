import pandas as pd

filtered_df = pd.DataFrame()
df_original = pd.read_csv("original_list.txt", header=None)
df_search = pd.read_csv("search_list.txt", header=None)


# print(df_original[0])
for i in range(0,len(df_search)):
    """
    Function create new DataFrame with finded words in original_list from search_list 
    """
    filtered_df_temp = df_original.loc[df_original[0].str.contains(df_search[0][i])]
    filtered_df = filtered_df._append(filtered_df_temp)

# print(filtered_df)

filtered_df.to_csv("output_list.txt", index=False)

# print(df_search)
# print(filtered_df)
# print(df_output)