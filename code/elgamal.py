import random
# The following creates a cryptographically secure version of randint:
system_random = random.SystemRandom()
randint = system_random.randint

from math import gcd
from utilities import modinv
from hashes import sha_256

# The prime p and primitive root r are fixed.
# Using a safe prime p made it easy to find a primitive root r.
# The private key b and public key B are INTEGERS in range(1,p).

p = 16984472341397032004402043741822530993165685074287947293498910324162260474638136465220384359373467279932524412385551981663179922037374365889854220536608602827699169313542959865713637467407107927274927

r = 4044076521778304012505810609850465754803535044061622571506121581123971288799277703543022672824806997172071310862561744792648138420086935617241967561720567395887007631338752556043029444641422170322966

def create_EG_private_key():
    # Creates an integer ElGamal private key
    private_key = randint(1,p-1)
    return private_key

def EG_public_key(private_key):
    # Returns the public key corresponding to a private key
    b = private_key
    assert b in range(1,p)
    public_key = pow(r,b,p)
    return public_key

def EG_encrypt(plaintext, public_key):
    # ElGamal encryption of an integer plaintext with a public key
    assert plaintext in range(1,p)
    B = public_key
    a = randint(1,p-1) # random ephemeral key
    A = pow(r,a,p)
    M = ( plaintext * pow(B,a,p) ) % p
    ciphertext = (A,M)
    return ciphertext

def EG_decrypt(ciphertext, private_key):
    # ElGamal decryption of ciphertext (A,M) with a private key
    (A,M) = ciphertext
    b = private_key
    plaintext = ( M * pow(A,p-1-b,p) ) % p
    return plaintext

def EG_sign(string, private_key):
    # Signs the SHA-256 hash of a string with a private key
    m = sha_256(string)
    b = private_key
    while True:
        a = randint(1,p-1)
        if gcd(a,p-1) == 1:
            break
    A1 = pow(r,a,p)
    A2 = ( modinv(a,p-1) * (m - b*A1) ) % (p-1)
    signature = (A1,A2)
    return signature

def EG_verify(string, signature, public_key):
    # Verifies if the SHA-256 hash of the string was
    # correctly signed by the owner of the public key
    m = sha_256(string)
    (A1,A2) = signature
    B = public_key
    return (pow(B,A1,p)*pow(A1,A2,p)) % p == pow(r,m,p)
