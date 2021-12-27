from utils import  scalar_mult
from utils import curve
from random import randrange


# Keypair generation and ECDSA ################################################

def make_keypair():
    """Generates a random private-public key pair."""
    private_key = randrange(1, curve.n)
    public_key = scalar_mult(private_key, curve.g)

    return private_key, public_key



print("Name:\t",curve.name)
print("a:\t",curve.a)
print("b:\t",curve.b)
print("G:\t",curve.g)
print("P:\t",curve.p)

print("==========================")

aliceSecretKey, alicePublicKey = make_keypair()
bobSecretKey, bobPublicKey = make_keypair()

print("Alice\'s secret key:\t", aliceSecretKey)
print("Alice\'s public key:\t", alicePublicKey)
print("Bob\'s secret key:\t", bobSecretKey)
print("Bob\'s public key:\t", bobPublicKey)


sharedSecret1 = scalar_mult(bobSecretKey,alicePublicKey)
sharedSecret2 = scalar_mult(aliceSecretKey,bobPublicKey)


print("==========================")
print("Alice\'s shared key:\t",sharedSecret1)
print("Bob\'s shared key:\t",sharedSecret2)


print("==========================")
print("The shared value is the x-value:\t", (sharedSecret1[0]))