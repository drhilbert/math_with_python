from math import ceil, sqrt
from primitive_roots import make_base_point
from random import randint # just for testing
from time import perf_counter

def dlog_by_trial_mult(A, r, p):
    # Returns the discrete logarithm of A with base r (mod p)
    # We return 0 if A = 1, so dlog_by_trial_mult(1,r,p) = 1
    A = A % p
    r = r % p
    assert A != 0
    if A == 1:
        return 0
    power = 1 
    for k in range(1,p):
        power = (power * r) % p
        if power == A:
            return k
    return None # That happens if no exponent works.

def dlog_by_shanks(A, r, p, N = None):
    # Returns the discrete logarithm of A with base r (mod p)
    # N is the order of r (mod p)
    # The last argument is optional: We use N = p-1 if left out
    A = A % p
    r = r % p
    assert A != 0
    if N == None:
        N = p-1 # happens when r is a primitive root of p
    n = ceil(sqrt(N))
    giantstep = pow(r, -n, p)
    # Create the giantstep "list":
    giant_dict = {} # using a dictionary for efficient lookup
    entry = A
    for j in range(n+1):
        giant_dict[entry] = j
        entry = (entry * giantstep) % p
    # Find a power of r that's in the giantstep dictionary:
    power = 1
    for i in range(n+1):
        if power in giant_dict:
            j = giant_dict[power]
            x = (i + j * n)
            return x % N
        power = (power * r) % p
    return None # That happens only if the DLP has no solution.
        
(p, r) = make_base_point(8)
A = randint(1, p-1)

start = perf_counter()
dlog_by_shanks(A,r,p)
end = perf_counter()
print("Babystep-giantstep time:  ", end-start)

start = perf_counter()
dlog_by_trial_mult(A,r,p)
end = perf_counter()
print("Trial multiplication time:", end-start)
    


    
    