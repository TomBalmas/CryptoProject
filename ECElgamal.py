
import sys
from random import randint
from hashlib import sha256 as hash
import libnum

from utils import curve,scalar_mult,point_add


def sign(msg):

    if (len(sys.argv)>1):
        msg=(sys.argv[1])

    # Alice's key pair (dA,QA)
    dA = randint(0, curve.n-1)
    QA = scalar_mult(dA,curve.g)

    h=int(hash(msg.encode()).hexdigest(),16)

    k = randint(0, curve.n-1)

    rpoint = scalar_mult(k,curve.g)

    r = rpoint[0] % curve.n

    # Bob takes m and (r,s) and checks
    inv_k = libnum.invmod(k,curve.n)

    s = (inv_k*(h+r*dA)) % curve.n
    #print(f"Msg: {msg}\n\nAlice's private key={dA}\nAlice's public key={QA}\nk= {k}\n\nr={r}\ns={s}")
    return r,s,QA


# To check signature

def verify(msg,r,s,QA):
    inv_s = libnum.invmod(s,curve.n)
    c = inv_s
    h = int(hash(msg.encode()).hexdigest(), 16)
    u1=(h*c) % curve.n
    u2=(r*c) % curve.n
    P = point_add(scalar_mult(u1,curve.g), scalar_mult(u2,QA))
    res = P[0] % curve.n
    #print (f"\nResult r={res}")
    if (res==r):
	    print("Signature matches!")

r,s,QA = sign("blabla")

verify("blabla",r,s,QA)