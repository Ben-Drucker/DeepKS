from venv import create
import numpy as np
import sklearn.metrics
import random

labels = np.array([0 for _ in range(70)] + [1 for _ in range(77)], dtype=float)

def create_random(labels):
    ast = np.argsort(labels)
    num_zeros = len(ast) - sum(labels)
    num_ones = sum(labels)
    if num_zeros % 2: # number of zeros is not even
        print("Info: Trimming a true decoy instance for even size of sets.")
        ast = ast[1:]
        labels = labels[ast]
    if num_ones % 2: # number of ones is not even
        print("Info: Trimming a true target instance for even size of sets.")
        ast = ast[:-1]
        labels = labels[ast]

    rand_outputs = np.zeros_like(labels)
    for i in range(len(ast) - 1, -1, -1):
        rand_outputs[ast[i]] = 1 if i % 2 else 0

    return labels, rand_outputs

labels, rand_outputs = create_random(labels)
score = sklearn.metrics.roc_auc_score(labels, rand_outputs)
print(score)