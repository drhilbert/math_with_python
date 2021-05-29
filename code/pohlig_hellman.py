from random import randint # just for testing
from time import perf_counter
from utilities import prod, modinv, chinese_remainder
from primes import is_prime, make_prime
from factoring import list_of_prime_powers

# Implementation of the Pohlig-Hellman algorithm to compute discrete logarithms
# Still to do: compute dlog(A, r, p) with the baby-step giant-step algorithm

def dlog_by_trial_mult(A, r, p):
    # Returns the discrete logarithm of A with base r (mod p)
    # We return 0 if A = 1, so dlog_by_trial_mult(1,r,p) = 1
    A = A % p
    r = r % p
    assert ( A != 0 )
    if A == 1:
        return 0
    power = 1 
    for k in range(1,p):
        power = (power * r) % p
        if power == A:
            return k
    return None # That happens if no exponent works.

def dlog(A, r, p):
    # Returns the discrete logarithm of A with base r (mod p)
    # We return 0 if A = 1, so dlog(1,r,p) = 1
    A = A % p
    r = r % p
    assert ( A != 0 )
    if A == 1:
        return 0
    # Reduction 1 of Pohlig_Hellman:
    prime_powers = list_of_prime_powers(p-1) # list of pairs (p_i,k_i)
    s = len(prime_powers)
    moduli = [ p_i**k_i for (p_i,k_i) in prime_powers ]
    R_ = [ pow(r, (p-1)//p_i**k_i, p) for (p_i,k_i) in prime_powers ] # list of r_i's
    A_ = [ pow(A, (p-1)//p_i**k_i, p) for (p_i,k_i) in prime_powers ] # list of A_i's
    solutions = [ dlog_2(A_[i], R_[i], p, prime_powers[i]) for i in range(s) ]
    if None in solutions:
        return None
    x = chinese_remainder(solutions, moduli)
    return x

def dlog_2(A, r, p, prime_power):
    # Uses Reduction 2 of Pohlig-Hellman to compute the discrete logarithm
    # of A with base r (mod p) if the order of r (mod p) is q^k,
    # where prime_power = (q,k)
    (q,k) = prime_power
    a = [] # list of digits a_i in Reduction 2
    left_base = pow(r, q**(k-1), p)
    for j in range(0,k):
        sigma = sum([ a[i]*q**i for i in range(0,j) ])
        neg_power = pow(modinv(r,p), sigma, p)
        right_base = (A*neg_power) % p
        right_side = pow(right_base, q**(k-1-j), p)
        next_digit = dlog_by_trial_mult(right_side, left_base, p)
        a.append(next_digit)
    x = sum([ a[i]*pow(q,i,p) for i in range(0,k) ])
    return x

def primitive_root(p, prime_powers):
    # Finds the smallest primitive root of a prime p, given the prime powers in p-1
    # See https://cp-algorithms.com/algebra/primitive-root.html
    # First we check that p is prime and that the prime factorization works:
    assert( is_prime(p) ) 
    assert( prod([p_i**k_i for (p_i,k_i) in prime_powers]) == p-1 )
    for a in range(1,p):
        powers = [ pow(a, (p-1)//p_i, p) for (p_i,k_i) in prime_powers ]
        if 1 in powers:
            continue
        else:
            return a
        
def print_prime_factorization():
    output = "Prime factorization of p-1: "
    for (p_i,k_i) in prime_powers:
        if k_i > 1:
            output += f"({p_i}^{k_i})"
        else:
            output += f"({p_i})"
    print(output)

# Testing dlog:

digits = 10
p = make_prime(digits)
print(f"Random prime p with {digits} digits: {p}")

start = perf_counter()
prime_powers = list_of_prime_powers(p-1) # Find the prime powers in p-1
end = perf_counter()
factoring_time = end-start

print_prime_factorization()
r = primitive_root(p, prime_powers)

# Computing dlog(A,r,p) for a random A:
A = randint(1,p-1)
start = perf_counter()
k = dlog(A,r,p) # Replace dlog with dlog_by_trial_mult for comparison
end = perf_counter()
dlog_time = end-start # This indcludes the time to factor p-1
assert( pow(r,k,p) == A ) # Just checking that dlog works as is should

print(f"Factoring time:      {factoring_time} seconds")
print(f"Pohlig-Hellman time: {dlog_time} seconds")
