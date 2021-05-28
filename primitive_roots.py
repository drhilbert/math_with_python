# This code is not efficient for large values of n.
# To find a primitive root of a large prime p using the prime
# factorization of p-1, look in the file pohlig-hellman.py.

from math import gcd

def phi(n):
    # Euler's totient function
    assert(n > 0)
    counter = 0
    for k in range(0,n):
        if gcd(k,n) == 1:
            counter += 1
    return counter

def order(a,n):
    # Returns the order of a (mod n)
    assert(n > 1)
    if gcd(a,n) != 1:
        raise Exception('Order is undefined')
    k = 1
    power = 1
    while True:
        power = (power * a) % n
        if power == 1:
            return k
        k += 1
        
def is_primitive_root(a,n):
    # Returns True if a is a primitive root (mod n)
    assert(n > 1)
    return (order(a,n) == phi(n))
            
def make_primitive_root(n):
    # Returns the smallest primitive root of n, or None
    assert(n > 1)
    for a in range(1,n):
        if is_primitive_root(a,n):
            return a
    return None

def has_primitive_root(n):
    # Returns True if n has a primitive root
    assert(n > 1)
    if make_primitive_root(n):
        return True
    return False
