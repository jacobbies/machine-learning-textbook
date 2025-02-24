import matplotlib.pyplot as plt
import numpy as np 


#measures class mixture rate
def gini_impurity(labels):
    #empty set = pure
    if len(labels) == 0:
        return 0
    #count occurences of each label
    counts = np.unique(labels, return_counts=True)[1]
    fractions = counts / len(labels)
    return 1 - np.sum(fractions**2)

#measures the reduction of uncertainty due to a split
def entropy(labels):
    if len(labels) == 0:
        return 0
    counts = np.unique(labels, return_counts=True)[1]
    fractions = counts / len(labels)
    return -np.sum(fractions * np.log2(fractions))
    