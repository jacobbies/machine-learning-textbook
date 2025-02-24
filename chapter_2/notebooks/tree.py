import matplotlib.pyplot as plt
import numpy as np 

def gini_impurity(labels):
    if len(labels) == 0:
        return 0
    counts = np.unique(labels, return_counts=True)[1]
    fractions = counts / len(labels)
    return 1 - np.sum(fractions**2)
