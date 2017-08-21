# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols, usecols=range(3))
m_cols = ['movie_id', 'title']
movies = pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")
ratings = pd.merge(movies, ratings)

#print(ratings.head())

user_ratings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')
#print(user_ratings.head())

# the corr method produces columns and rows as movie names and intersection values
# as the correlation between column and row movie..
# Also remove/ignore movie similarities with <100 ratings
# this will ignore even movies that do not have >= 100 ratings
corrMatrix = user_ratings.corr(method='pearson', min_periods=100)
#print(corrMatrix.head())

# pick ratings for user_id = 0
myRatings = user_ratings.loc[0].dropna()
print("Movies that i rated - \n", myRatings)

simCandidates = pd.Series()
for i in range(len(myRatings.index)):
    #print("Adding sim for ", myRatings.index[i])
    sims = corrMatrix[myRatings.index[i]].dropna()
    #print("sims - ", sims)
    sims = sims.map(lambda x: x * myRatings[i])
    #print("Mapped sims - ", sims)
    simCandidates = simCandidates.append(sims)

simCandidates.sort_values(inplace=True, ascending=False)
#print(simCandidates.head(20))

simCandidates = simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace=True, ascending=False)
#print(simCandidates.head(20))

# remove the movies that were in my list..
filteredSimCand = simCandidates.drop(myRatings.index)
print("Recommended movies based on my ratings - \n", filteredSimCand.head(10))
