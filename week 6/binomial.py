from math import factorial

def binom(n, k):
    num = factorial(n) # this is O(n)
    denom = factorial(k) * factorial(n - k) 

    return num // denom 

print(binom(3, 2))
