from math import gcd

def prod(numbers):
    # Returns the product of a list of numbers
    product = 1
    for number in numbers:
        product = product * number
    return product


def egcd(a, b): 
    # Returns a triple (g,x,y) with g = gcd(a,b) = xa+yb
    # Adapted from www.techiedelight.com/extended-euclidean-algorithm-implementation
    if a == 0:
        if b == 0:
            raise Exception('gcd does not exist')
        if b > 0:
            return (b, 0, 1)
        if b < 0:
            return (-b, 0, -1)
    else: # What follows is just the Euclidean Algorithm
        (g, y, x) = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    

def modinv(a, m):
    # Returns the modular inverse of a (mod m) between 0 and m
    (g, x, y) = egcd(a, m) 
    if g == 1: # Note that 1 = xa+ym in this case
        return x % m
    else: 
        return None
    

def solve_cong(a, b, m):
    # Returns the smallest nonnegative solution of the congruence
    # a*x congruent b (mod m)
    d = gcd(a,m)
    if d == 1:
        return (modinv(a,m) * b) % m
    if b % d == 0: # i.e. if d divides b
        return solve_cong(a//d, b//d, m//d)
    else:
        raise Exception('Congruence has no solution')
    

def solve_diophantine(a, b, c):
    # Returns a particular solution (x,y) of the diophantine equation
    # a*x + b*y = c
    assert not (a == 0 and b == 0) # to avoid trivialities
    d = gcd(a,b)
    if c % d == 0: # i.e. if d divdides c
        (g, x, y) = egcd(a//d, b//d) # Note that g must be 1
        return ((c*x)//d, (c*y)//d)
    else:
        raise Exception('Diophantine equation has no solution')
    
        
def chinese_remainder(a, m):
    #
    # Solves the system of congruences
    # x congruent a_i (mod m_i)
    # where a = [ a_0, a_1, a_2, ... ]
    # and   m = [ m_0, m_1, m_2, ... ]    
    #
    r = len(m) # number of congruences
    M = prod(m) # product of the moduli m_i
    b = [ M//m[i] for i in range(r) ] # list of b_i = M/m_i
    b_inv  = [ modinv(b[i], m[i]) for i in range(r) ]
    x = sum([ a[i]*b[i]*b_inv[i] for i in range(r) ])
    return x % M
