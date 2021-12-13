from triple_des import triple_des, PAD_PKCS5
from ECElgamal import sign, verify
from DiffieHellman import DiffieHellman

users = ("Alice", "Bob")
inboxes = [["", "", "", ""], ["", "", "", ""]]

def app():
    user = input("Enter user: ")
    if user.lower() == "alice":
        user = "Alice"
        receiver = users[1]
        inbox = inboxes[0]
    else:
        user = "Bob"
        receiver = users[0]
        inbox = inboxes[1]
    print("--------------------CryptoWhatsApp--------------------")
    if inbox != ["", "", "", ""]:
        print(receiver, ": ", sep="", end="")
        print("decrypting cipher: ", inbox[0])
        if user.lower() == "alice":
            plain = tdAlice.decrypt(inbox[0]).decode("utf-8")
        else:
            plain = tdBob.decrypt(inbox[0]).decode("utf-8")
        print("verifying signature:", inbox[1])
        verify(plain, inbox[1], inbox[2], inbox[3])
        print(receiver,":",plain)

    print(user, end="")
    msg = input(": ")
    print(user, "signing the message...")
    r, s, QA = sign(msg)
    if user.lower() == "alice":
        cipher = tdAlice.encrypt(msg)
    else:
        cipher = tdBob.encrypt(msg)
    print(user, "sent to", receiver, ":", cipher, "with signature:", r)
    if user.lower() == "bob":
        inboxes[0] = cipher, r, s, QA
    else:
        inboxes[1] = cipher, r, s, QA

    # input crypto project
    return user, cipher


print("Welcome to CryptoWhatsApp:\n"
      "Users are Alice and Bob")
alice = DiffieHellman()
bob = DiffieHellman()
print("Alice's public key:", alice.publicKey)
print("Bob's public key:", bob.publicKey)
print("Alice generates her key for encrypt/decrypt:")
alice.genKey(bob.publicKey)
print(alice.getKey())
print("Bob generates his key for encrypt/decrypt:")
bob.genKey(alice.publicKey)
print(bob.getKey())
tdBob = triple_des(bob.getKey(), padmode=PAD_PKCS5)
tdAlice = triple_des(alice.getKey(), padmode=PAD_PKCS5)

while True:
    app()
