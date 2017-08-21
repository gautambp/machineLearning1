# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy import spatial

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols, usecols=range(len(r_cols)))
#print(ratings.head())

movieStats = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})
#print(movieStats.head())

# normalize movie rating size; make it between 0 & 1
movieNumRatings = pd.DataFrame(movieStats['rating']['size'])
normalizedMovieRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
#print(normalizedMovieRatings.head())

movieDict = {}
with open(r'u.item') as f:
    temp = ''
    for line in f:
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = list(map(int, genres))
        sizeInfo = normalizedMovieRatings.loc[movieID].get('size')
        meanInfo = movieStats.loc[movieID].rating.get('mean')
        movieDict[movieID] = (name, genres, sizeInfo, meanInfo)
        
#print(movieDict[1])

def computeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genresDist= spatial.distance.cosine(genresA, genresB)
    popA = a[2]
    popB = b[2]
    popDist = abs(popA - popB)
    return genresDist + popDist

#print(computeDistance(movieDict[2], movieDict[4]))

import operator

# get K nearest neighbor of the movie (movieID)
def getNeighbors(movieID, k):
    distances = []
    # compute distance from movieID to all other movies
    for movie in movieDict:
        if (movie != movieID):
            dist = computeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
    # sort movies by their distance to movieID
    distances.sort(key=operator.itemgetter(1))
    # pick first k items from sorted list as nearest neighbors
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

K = 10
avgRating = 0.0
neighbors = getNeighbors(1, K)
print("Nearest neighbors of movie : ", movieDict[1][0])
for n in neighbors:
    avgRating += movieDict[n][3]
    print(movieDict[n][0], " - rating : ", movieDict[n][3])

avgRating /= float(K)
print("Average rating from all neighbors - ", avgRating)
