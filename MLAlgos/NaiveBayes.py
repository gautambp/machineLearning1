# -*- coding: utf-8 -*-

import os
import io
import numpy as np
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)
            
            inBody = False
            lines = []
            f = io.open(path, "r", encoding="latin1")
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == "\n":
                    inBody = True
            f.close()
            message = "\n".join(lines)
            yield path, message

def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({"message" : message, "class": classification})
        index.append(filename)
    
    return DataFrame(rows, index = index)

localFolderPath = "C:/development/training/MachineLearningSundog/DataScience-Python3/emails"
spamFolderPath = localFolderPath + "/spam"
hamFolderPath = localFolderPath + "/ham"
data = DataFrame({"message": [], "class": []})
data = data.append(dataFrameFromDirectory(spamFolderPath, "spam"))
data = data.append(dataFrameFromDirectory(hamFolderPath, "ham"))

#print("A few entries from the data files : ", data.head())

# count each word occurrences along with words in the messages
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

# do the actual classification.. utilize tokenized words alongwith counts 
# against target data for both classifications
classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)
print(classifier)

# now the classifier has been trained.. let's test it out
example = ["Free Viagra now!!!", "Hi Bob, how are you? Are you free tomorrow?"]
example_count = vectorizer.transform(example)
print(example_count)
print("Predictions for the example - ", classifier.predict(example_count))
