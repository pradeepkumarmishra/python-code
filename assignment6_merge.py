import pandas as pd

df_movies = pd.read_csv("/Users/pradeepmishra/Downloads/source-code 2/2_pandas_basics_code/7_concat_merge/Exercise/movies.csv")

#print(df_movies)
df_financials = pd.read_csv("/Users/pradeepmishra/Downloads/source-code 2/2_pandas_basics_code/7_concat_merge/Exercise/financials.csv")

df_languages = pd.read_csv("/Users/pradeepmishra/Downloads/source-code 2/2_pandas_basics_code/7_concat_merge/Exercise/languages.csv")

#task 1
#print(df_movies.head(3))
#task 2
df_new_movies = pd.read_csv("/Users/pradeepmishra/Downloads/source-code 2/2_pandas_basics_code/7_concat_merge/Exercise/new_movies.csv")
#
# df_movies = pd.concat([df_movies, df_new_movies], ignore_index=True)
# print(df_movies.tail(5))
#task 3
df_movies = pd.merge(df_movies, df_languages, on = "language_id")
#print(df_movies.head(1))
#task 4
df_movies = pd.merge(df_movies, df_financials, on = "movie_id", how = "left")
df_movies.to_csv('final_complete_movies.csv', index = False, columns= ['movie_id', 'title', 'lang_name', 'budget', 'revenue', 'currency'])
