import pandas as pd

df = pd.read_csv("/Users/pradeepmishra/Downloads/source-code 2/2_pandas_basics_code/4_handling_missing_data_fillna_dropna_interpolate/weather_data.csv", parse_dates=['day'])
df.set_index('day', inplace=True)
#print(df)
# df.fillna({
#     'temperature': 0,
#     'windspeed': 0,
#     'event':  'Sunny'
# }, inplace=True)

df.fillna(method='bfill', limit=1, inplace=True)
print(df)
df.dropna(inplace=True)
print(df)
