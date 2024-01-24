import sys
import pandas as pd

path_original_list = "original_list.txt"
path_search_list = "search_list.txt"
path_output_list = "output_list.txt"

print ('<br /><br />Test python script <br />')
print ('<b>Output list: </b>', path_output_list, '<br />')
print ('<b>Original list: </b>', path_original_list, '<br />')
print ('<b>Search list: </b>', path_search_list, '<br />')


filtered_df = pd.DataFrame()
df_original = pd.read_csv(path_original_list, on_bad_lines='skip', header=None)
df_search = pd.read_csv(path_search_list, on_bad_lines='skip', header=None)


for i in range(0, len(df_search)):
    filtered_df_temp = df_original.loc[df_original[0].str.contains(df_search[0][i])]
    filtered_df = filtered_df._append(filtered_df_temp)

filtered_df.to_csv(path_output_list, index=False)

