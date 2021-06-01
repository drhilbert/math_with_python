### Python Code for Use in Number Theory and Cryptography


You can run Python code in your browser, e.g. here: [www.programiz.com/python-programming/online-compiler](https://www.programiz.com/python-programming/online-compiler/)


[utilities.py](code/utilities.py): Basic number theory utilities

    prod(numbers): Returns the product of a list of numbers

    egcd(a,b): Returns a triple (g,x,y) with g = gcd(a,b) = xa+yb

    modinv(a,m): Returns the modular inverse of a (mod m) between 0 and m

    solve_cong(a,b,m): Returns the smallest nonnegative solution of the congruence
                       a*x congruent b (mod m)
    
    solve_diophantine(a,b,c): Returns a particular solution (x,y) of the diophantine equation
                              a*x + b*y = c
    
    chinese_remainder(a,m): Solves the system of congruences 
                            x congruent a_i (mod m_i)
                            where a = [ a_0, a_1, a_2, ... ]
                            and   m = [ m_0, m_1, m_2, ... ] 
                    

[primes.py](code/primes.py): Primality testing and prime generation

    is_prime(n): Returns True if n is prime (Miller-Rabin test)
    
    make_prime(d): Creates a prime with d digits

    safe_prime(d): Creates a safe prime with d digits


[factoring.py](code/factoring.py): Tools for finding the prime factorization

    find_factor(n): Uses Pollard's rho method to find a factor of n

    list_of_prime_factors(n): Returns the sorted list of all prime factors of n (with repetitions)

    list_of_prime_powers(n): Returns the prime factorization of n as a list (without repetitions)
                             of pairs (p,k), where p is a prime factor of multiplicity k

    print_prime_factorization(n): Prints the prime factorization of n


[primitive_roots.py](code/primitive_roots.py): Orders and primitive roots. Warning: Code not optimized for large n

    phi(n): Euler's totient function
    
    order(a,n): Returns the order of a (mod n)

    is_primitive_root(a,n): Returns True if a is a primitive root (mod n)

    make_primitive_root(n): Returns the smallest primitive root of n, or None

    has_primitive_root(n): Returns True if n has a primitive root

    primitive_root(safe_prime): Returns a primitive root of a safe prime p
    
    make_base_point(d): Returns a pair (p,r), where p is a safe prime
                        with d digits and r is a primitive roote of p


[hashes.py](code/hashes.py): SHA-256 hashes

    sha_256_hex(string): Returns the SHA-256 hash of a string as a hexadecimal string  

    sha_256(string): Returns the SHA-256 hash of a string as a base 10 integer


[rsa.py](code/rsa.py): RSA encryption and RSA signatures

    create_rsa_private_key(d): Creates a private RSA key (p,q,j) where p and q have d digits

    rsa_public_key(private_key): Returns the public key (n,k) corresponding to a private key (p,q,j)
    
    rsa_encrypt(plaintext, public_key): Encrypts an integer plaintext with a public key (n,k)
    
    rsa_decrypt(ciphertext, private_key): Decrypts an integer ciphertext with a private key (p,q,j)
    
    rsa_signature(string, private_key): Signs the SHA-256 hash of a string with a private key (p,q,j)
    
    rsa_verify(string, signature, public_key): Verifies if the SHA-256 hash of the string was
                                               correctly signed by the owner of the public key (n,k)


[elgamal.py](code/elgamal.py): ElGamal encryption and ElGamal signatures

    create_EG_private_key(): Creates an integer ElGamal private key
    
    EG_public_key(private_key): Returns the public key corresponding to a private key

    EG_encrypt(plaintext, public_key): ElGamal encryption of an integer plaintext with a public key
    
    EG_decrypt(ciphertext, private_key): ElGamal decryption of ciphertext (A,M) with a private key

    EG_sign(string, private_key): Signs the SHA-256 hash of a string with a private key
    
    EG_verify(string, signature, public_key): Verifies if the SHA-256 hash of the string was
                                              correctly signed by the owner of the public key


[pohlig_hellman.py](code/pohlig_hellman.py): Implementation of the Pohlig-Hellman algorithm to compute discrete logarithms

    dlog(A,r,p): Returns the discrete logarithm of A with base r (mod p)

    primitive_root(p, prime_powers): Finds the smallest primitive root of a prime p,
                                     given the list of prime powers in p-1.


[shamir_sharing.py](code/shamir_sharing.py): Implemetation of Shamir's Secret Sharing method

    create_shares(s,p,k,n): Split the secret number s into n shares so that
                            k out of n shares recover the secret.
                            Returns a list of shares of the form (i,u), where
                            i is the share index in {1,2,...,n} and u is in Z_p. 
    
    recover_secret(shares, p): Use a list of shares to recover the secret.
                               Each share has the form (i,u), where
                               i is the share index and u is in Z_p.


[ecc.py](code/ecc.py): Tools for elliptic curve computations. Warning: Not optimized for large p

    on_curve(P): Returns True if the point P = (x,y) lies on the elliptic curve
    
    reflect(P): Returns P' (i.e. the negative of P)
    
    add(P,Q): Returns the sum of P and Q
    
    mult(P,n): Returns nP

    order(P): Returns the order of a point P
    
    points_on_curve(): Returns the list of points on the elliptic curve
                    
    group_order(): Returns the order of the elliptic curve

    generators(): Returns the list of generators of the elliptic curve
