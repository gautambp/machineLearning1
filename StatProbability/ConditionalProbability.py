# -*- coding: utf-8 -*-

import numpy as np

np.random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0
peopleCount = 100000

for _ in range(peopleCount):
    ageDecade = np.random.choice([20, 30, 40, 50, 60, 70])
    # probability of purchase has been made dependent on age.. if this were to change to 
    # hard coded value, you would see change in all values below
    purchaseProbability = float(ageDecade) / 100.0
    #purchaseProbability = 0.4
    totals[ageDecade] += 1
    if (np.random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1

print("People count in each age decade: ", totals)
print("Purchases in each age decade: ", purchases)
print("Total purchases - ", totalPurchases)

# Probability of being in age decade 30
probIn30 = float(totals[30]) / float(peopleCount)
print("Probability of being in age decade 30 (P[30s]): ", probIn30)

# Probability of purchase regardless of age decade
probPurchase = float(totalPurchases) / float(peopleCount)
print("Probaility of purchase (P[purchase]): ", probPurchase)

print("P[purchase] * P[30s] : ", probIn30 * probPurchase)

probPurchaseAndIn30 = float(purchases[30])/float(peopleCount)
print("Probability of being in 30s with a purchase (P[30s, purchase]): ", probPurchaseAndIn30)

# P[purchase | 30s] = P[purchase, 30s] / P[30s]
print("Probability of a purchase given age decade 30 (P[purchase | 30s]): ", probPurchaseAndIn30/probIn30)

# Probability of a purchase for age decade 30
probPurchaseIn30 = float(purchases[30]) / float(totals[30])
print("Probability of a purchase in age decade 30 (P[purchase | 30s]): ", probPurchaseIn30)
