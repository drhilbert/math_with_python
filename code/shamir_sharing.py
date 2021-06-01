import random
# For cryptographically secure random number generation:
randint = random.SystemRandom().randint

from utilities import modinv
from primes import is_prime, make_prime
from itertools import combinations

def dot_product(a,b,p):
    # Returns the dot product of the lists a and b (mod p)
    assert len(a) == len(b)
    return sum([ (a[i]*b[i]) for i in range(len(a)) ]) % p

def create_shares(s,p,k,n):
    # Split the secret number s into n shares so that
    # k out of n shares recover the secret.
    # Returns a list of shares of the form (i,u), where
    # i is the share index in {1,2,...,n} and u is in Z_p. 
    assert ( is_prime(p) and s in range(p) )
    assert ( n in range(1,p) and k in range(1,n+1) )
    a = [randint(0,p-1) for j in range(k)]
    a[0] = s
    shares = [0] * n # list of shares to be created
    for i in range(1,n+1):
        powers = [pow(i,j,p) for j in range(k)]
        shares[i-1] = (i, dot_product(a,powers,p))
    test_shares(s,p,k,n,shares) # see below
    return shares

def recover_secret(shares, p):
    # Use a list of shares to recover the secret.
    # Each share has the form (i,u), where
    # i is the share index and u is in Z_p.
    l = len(shares)
    sum = 0
    for j in range(l):
        product = 1
        for r in range(l):
            if r != j:
                factor = shares[r][0] * modinv(shares[r][0]-shares[j][0], p)
                product = (product * factor) % p
        sum = (sum + shares[j][1] * product) % p
    return sum

def test_shares(s,p,k,n,shares):
    # Making sure that every combination of k or more
    # shares sucessfully restores the secret.
    test_tuples = []
    for l in range(k,n+1):
        test_tuples += list(combinations(range(n),l))
    test_list = [ [shares[i] for i in tuple] for tuple in test_tuples ]
    for shares in test_list:
        assert recover_secret(shares,p) == s


p = 10**8+7
s = 64983083 

shares = create_shares(s,p,2,4)
print(shares)
subset_of_shares = [ shares[i-1] for i in [1,3] ]
print(subset_of_shares)
secret = recover_secret(subset_of_shares,p)
print(secret)
