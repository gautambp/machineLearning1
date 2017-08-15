# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols, usecols=range(3))
m_cols = ['movie_id', 'title']
movies = pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

#print(ratings.head())

movie_ratings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')
#print(movie_ratings.head())

aMovieRating = movie_ratings['Star Wars (1977)']
#print(aMovieRating.head())

similarMovies = movie_ratings.corrwith(aMovieRating)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)
#print(similarMovies.head(10))
#similarMovies.sort_values()
#print(similarMovies)
# this results of similarMovies are not so good.. since it includes
# even most obscure movies with higher ratings.. we need to keep only popular movies

movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
#print(movieStats.head())

popularMovies = movieStats['rating']['size'] > 100
#print(popularMovies.head())

popMovieStats = movieStats[popularMovies];
#print(popMovieStats.head())
sortedPopMovieStats = popMovieStats.sort_values(by=[('rating','mean')], axis=0, ascending=False)
#print(sortedPopMovieStats.head())

df = sortedPopMovieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
#print(df.head())

df = df.sort_values(['similarity'], ascending=False)
print(df.head())
