import pandas as pd

df = pd.read_csv("/Users/pradeepmishra/Downloads/source-code 2/2_pandas_basics_code/6_group_by/Exercise/movies_data.csv")
#print(df)
#print(df[df['city'] == 'mumbai'])
#g = df.groupby('industry')
#task2
print(df['imdb_rating'])
#task 3
#print(g.get_group("Bollywood"))
#task 4

def grouper(df, idx, col):
    if 1 <= df[col].loc[idx] <= 3.9:
        return "Poor"
    elif 4 <= df[col].loc[idx] <= 7.9:
        return "Average"
    elif 8 <= df[col].loc[idx] <= 10:
        return "Good"
    return "others"

g = df.groupby(lambda x : grouper(df, x, 'imdb_rating'))
for key, d in g:
    print(key)
    print("\n")
    print(d)
#print(df['imdb_rating'].loc['idx'])

