from hashlib import sha256

def sha_256_hex(string):
    # Returns the SHA-256 hash of a string as a hexadecimal string  
    return sha256(string.encode()).hexdigest()

def sha_256(string):
    # Returns the SHA-256 hash of a string as a base 10 integer
    return int(sha_256_hex(string), 16)
