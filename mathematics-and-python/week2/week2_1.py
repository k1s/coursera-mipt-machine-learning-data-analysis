import numpy as np
import scipy.spatial
import re

with open("sentences.txt") as file:
    lines = file.readlines()

linesLower = [line.lower() for line in lines]

sentences = [filter(None, re.split('[^a-z]', s)) for s in linesLower]

sentences_count = len(sentences)

words_flatten = reduce(list.__add__, sentences)

words = list(set(words_flatten))

words_count = len(words)

matrix = np.zeros((sentences_count, words_count))
for i, sentence in enumerate(sentences):
    for j, word in enumerate(words):
        matrix[i, j] = sentence.count(word)

distancies = [(i, scipy.spatial.distance.cosine(matrix[0], matrix[i])) for i in range(1, sentences_count)]

distancies_sorted = sorted(distancies, key=lambda x: x[1])

print distancies_sorted[0][0], distancies_sorted[1][0]