import numpy as np
import random

# Define the longest common subsequence of two binary strings
def lcs(X, Y):
    m = len(X)
    n = len(Y)

    L = [[None]*(n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]

def generate_markov_chain(length, p):
    sequence = np.zeros(length, dtype=int)
    sequence[0] = np.random.choice([0, 1])
    for i in range(1, length):
        if np.random.rand() < p:
            sequence[i] = sequence[i - 1]
        else:
            sequence[i] = 1 - sequence[i - 1]
    return sequence

# Parameters
length = 10000
p = 0.1
q = 0.1
trials = 70

# Store normalized LCS values for variance calculation
lcs_values = []

for _ in range(trials):
    X = generate_markov_chain(length, p)
    Y = generate_markov_chain(length, q)
    lcs_length = lcs(X, Y)
    lcs_values.append(lcs_length)

average_lcs = np.mean(lcs_values)
variance_lcs = np.var(lcs_values, ddof=1)  # Population variance

print(f"Parameters: p = {p}, q = {q}")
print(f"Average LCS over {trials} trials: {average_lcs:.5f}")
print(f"Variance of LCS: {variance_lcs:.5f}")