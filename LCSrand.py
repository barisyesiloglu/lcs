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

def rand_key(p):
    key1 = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key1 += temp
    return(key1)

def rand_key_bernoulli_numpy(length, p):
    # Generate binary values (0 and 1) using Bernoulli distribution
    binary_array = np.random.choice(['1', '0'], size=length, p=[p, 1-p])
    return ''.join(binary_array)

# Parameters
length = 10000
p = 0.1
q = 0.1
trials = 70

# Store normalized LCS values for variance calculation
lcs_values = []

for _ in range(trials):
    X = rand_key_bernoulli_numpy(length, p)
    Y = rand_key_bernoulli_numpy(length, q)
    lcs_length = lcs(X, Y)
    lcs_values.append(lcs_length)

average_lcs = np.mean(lcs_values)
variance_lcs = np.var(lcs_values, ddof=1)  # Population variance

print(f"Parameters: p = {p}, q = {q}")
print(f"Average LCS over {trials} trials: {average_lcs:.5f}")
print(f"Variance of LCS: {variance_lcs:.5f}")