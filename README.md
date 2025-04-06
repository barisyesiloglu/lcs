# lcs
The length of the longest common subsequence (LCS) of random binary strings and its variance is investigated using Monte Carlo simulations. Two different cases were examined:

LCSrand: Each digit of sequence X is independently 1 with probability p. Each digit of sequence Y is independently 1 with probability q.
LCSmarkov: The first digits of these sequences are randomized; they are independently 0 or 1 with equal probability. Then, X has a persistence probability p: If the nth digit of X is 1 (similarly 0), (n+1)th digit is also 1 (similarly 0) with probability p. In an identical fashion, Y has persistence probability q.

For the calculation of the length of the LCS, we used strings of length 10000 and we had 70 trials for each (p,q) case. Since each simulation took approximately 1 hour to complete, we ran the code for each (p,q) pair separately for both LCSrand and LCSmarkov. The uploaded codes are for p=0.1, q=0.1 case only, but they can be altered accordingly for each (p,q) pair.
