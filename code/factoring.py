from math import gcd
from primes import is_prime

def find_factor(n):
    # Uses Pollard's rho method to find a factor of n
    if n == 1 or is_prime(n):
        return None
    for seed in range(0,n): # Try all seeds. Warning: may run a long time!
        x = [seed] # Initialize the list x with the seed
        k = 0
        factor = 1
        while factor == 1:
            k += 1
            next_term = (x[k-1]**2+1) % n # using f(x)=x^2+1
            x.append(next_term) # Add the next term to the list x
            for j in range(0,k):
                factor = gcd(x[k]-x[j], n)
                if factor == n:
                    break # We must try a different seed
                if factor > 1:
                    return factor
    return None # No seed has worked!

                
def list_of_prime_factors(n):
    # Returns the sorted list of all prime factors of n (with repetitions)  
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    d = find_factor(n)
    prime_factors = list_of_prime_factors(d) + list_of_prime_factors(n//d)
    return sorted(prime_factors)


def list_of_prime_powers(n):
    # Returns the prime factorization of n as a list (without repetitions)
    # of pairs (p,k), where p is a prime factor of multiplicity k
    prime_factors = list_of_prime_factors(n)
    prime_powers = []
    included_primes = []
    for p in prime_factors:
        if p not in included_primes:
            k = prime_factors.count(p) # multiplicity of p
            prime_powers.append((p,k)) # add the pair (p,k) to the list
            included_primes.append(p) # to make sure we don't include p again
    return prime_powers


def print_prime_factorization(n):
    # Prints the prime factorization of n
    output = f"Prime factorization of {n}: "
    prime_powers = list_of_prime_powers(n)
    for (p,k) in prime_powers:
        if k > 1:
            output += f"({p}^{k})"
        else:
            output += f"({p})"
    print(output)
    