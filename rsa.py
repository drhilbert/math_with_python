import random
# The following creates a cryptographically secure version of randint:
system_random = random.SystemRandom()
randint = system_random.randint

from math import gcd
from utilities import modinv
from primes import make_prime
from hashes import sha_256

def create_rsa_private_key(d):
    # Creates a private RSA key (p,q,j) where p and q have d digits
    p = make_prime(d)
    while True:
        q = make_prime(d)
        if q != p:
            break
    n = p*q
    phi = (p-1)*(q-1)
    while True:
        j = randint(2, phi-1)
        if gcd(j, phi) == 1:
            break
    return (p,q,j)

def rsa_public_key(private_key):
    # Returns the public key (n,k) corresponding to a private key (p,q,j)
    (p,q,j) = private_key
    n = p*q
    phi = (p-1)*(q-1)
    k = modinv(j, phi)
    return (n,k)

def rsa_encrypt(plaintext, public_key):
    # Encrypts an integer plaintext with a public key (n,k)
    (n,k) = public_key
    assert plaintext < n
    ciphertext = pow(plaintext, k, n)
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    # Decrypts an integer ciphertext with a private key (p,q,j)
    (p,q,j) = private_key
    n = p*q
    plaintext = pow(ciphertext, j, n)
    return plaintext

def rsa_signature(string, private_key):
    # Signs the SHA-256 hash of a string with a private key (p,q,j)
    (p,q,j) = private_key
    n = p*q
    assert n > 2**256 # making sure every SHA-256 hash can be signed
    signature = pow(sha_256(string), j, n)
    return signature

def rsa_verify(string, signature, public_key):
    # Verifies if the SHA-256 hash of the string was
    # correctly signed by the owner of the public key (n,k)
    (n,k) = public_key
    return ( pow(signature, k, n) == sha_256(string) )
    