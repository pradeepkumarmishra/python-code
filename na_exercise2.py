import pandas as pd
df = pd.read_csv("/Users/pradeepmishra/Downloads/source-code 2/2_pandas_basics_code/4_handling_missing_data_fillna_dropna_interpolate/Exercises/fruits_data.csv")
#print(df.shape)
#print(df.columns)
#print(df)
#new_df = df.fillna(-1)
#print(new_df)
# new_df = df.fillna(
#     {
#         'apple(1kg)': df['apple(1kg)'].mean(),
#         'banana(1 dozen)': df['banana(1 dozen)'].mean(),
#         'grapes(1kg)': df['grapes(1kg)'].median(),
#         'mango(1kg)': df['mango(1kg)'].median(),
#         'Water Melons(1)': 'Not Available'
#     }
# )
#print(new_df)
#new_df = df.fillna('ffill', inplace=True)
#print(new_df)
new_df = df.dropna(thresh=4)
#new_df.set_index(False)
new_df.to_csv("final_data.csv", index=False)