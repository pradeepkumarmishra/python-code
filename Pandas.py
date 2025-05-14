import pandas as pd

df = pd.read_csv("/Users/pradeepmishra/Downloads/source-code/2_pandas_basics_code/movies.csv")
#print(df['language'])
#print(dir(df))
#print(df.industry.value_counts())
#print (df.language.value_counts())]
#print(df[df.language == "English"])
#print(df[(df.imdb_rating == df.imdb_rating.max()) | (df.imdb_rating == df.imdb_rating.min())])
df['age'] = df['release_year'].apply(lambda x : 2013 - x)
#print(df.head(4))
#df['profit'] = df.apply(lambda x : x['revenue'] - x['budget'], axis=1)
#print(df.head(4))
#print(df[['title', 'revenue', 'age']])
df['year_classify'] = df['release_year'].apply(lambda x : 'before 2000' if x < 2000  else 'after 2000')
#print(df[['title', 'release_year', 'year_classify']])
#print(df.head(2))
df.to_csv("/Users/pradeepmishra/Downloads/source-code/2_pandas_basics_code/final_movie_data.csv", columns=['title', 'budget', 'revenue', 'year_classify'], index=False)