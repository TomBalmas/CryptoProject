import sys
from random import randint, randrange
from hashlib import sha256 as hash
from utils import curve, scalar_mult, point_add


def sign(msg, dA):
    s = 0
    r = 0
    if (len(sys.argv) > 1):
        msg = (sys.argv[1])
    # Alice's key pair (dA,QA)

    h = int(hash(msg.encode()).hexdigest(), 16)
    while s == 0:
        k = randint(0, curve.n - 1)
        rpoint = scalar_mult(k, curve.g)
        r = rpoint[0] % curve.n
        if r == 0:
            continue
        # Bob takes m and (r,s) and checks
        inv_k = pow(k, -1, curve.n)
        s = (inv_k * (h + r * dA)) % curve.n
    # print(f"Msg: {msg}\n\nAlice's private key={dA}\nAlice's public key={QA}\nk= {k}\n\nr={r}\ns={s}")
    return r, s


# To check signature

def verify(msg, r, s, QA):
    inv_s = pow(s, -1, curve.n)
    c = inv_s
    h = int(hash(msg.encode()).hexdigest(), 16)
    u1 = (h * c) % curve.n
    u2 = (r * c) % curve.n
    P = point_add(scalar_mult(u1, curve.g), scalar_mult(u2, QA))
    res = P[0] % curve.n
    # print (f"\nResult r={res}")
    if (res == r):
        print("Signature matches!")
    else:
        print("Not Valid signature!!")
        exit(0)


def make_keypair():
    """Generates a random private-public key pair."""
    private_key = randrange(1, curve.n)
    public_key = scalar_mult(private_key, curve.g)

    return private_key, public_key
