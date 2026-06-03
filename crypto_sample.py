from cryptography.hazmat.primitives.asymmetric import rsa
def k():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)
