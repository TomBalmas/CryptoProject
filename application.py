from triple_des import triple_des, PAD_PKCS5
from ECElgamal import sign, verify, make_keypair
from utils import  scalar_mult

users = ("Alice", "Bob")
inboxes = [["", "", "", ""], ["", "", "", ""]]

def app():
    valid = False
    while not valid:
        user = input("Enter user: ")
        if user.lower() == "alice":
            valid = True
            user = "Alice"
            receiver = users[1]
            inbox = inboxes[0] # alice inbox
        elif user.lower() == "bob":
            valid = True
            user = "Bob"
            receiver = users[0]
            inbox = inboxes[1] # bob inbox
        elif user.lower() == "exit":
            exit(0)
        else:
            print("Error: User not found...")
    print("--------------------CryptoWhatsApp--------------------")
    if inbox != ["", "", "", ""]:
        print("decrypting cipher: ", inbox[0])
        if user.lower() == "alice":
            plain = tdAlice.decrypt(inbox[0]).decode("utf-8")
        else:
            plain = tdBob.decrypt(inbox[0]).decode("utf-8")
        print("verifying signature:", inbox[1])
        verify(plain, inbox[1], inbox[2], inbox[3])
        print(receiver, ": ", plain, sep="")

    print(user, end="")
    msg = input(": ")
    print(user, "signing the message...")
    if user.lower() == "alice":
        r, s = sign(msg, aliceSecretKey)
        cipher = tdAlice.encrypt(msg)
    else:
        r, s = sign(msg,bobSecretKey)
        cipher = tdBob.encrypt(msg)
    print(user, " sent to ", receiver, ": ", cipher, " with signature: ", r,sep="")
    if user.lower() == "bob":
        inboxes[0] = cipher, r, s, bobPublicKey
    else:
        inboxes[1] = cipher, r, s, alicePublicKey
    print("------------------------------------------------------")

    # input crypto project
    return user, cipher


print("Welcome to CryptoWhatsApp:\n"
      "Users are Alice and Bob")


aliceSecretKey, alicePublicKey = make_keypair()
bobSecretKey, bobPublicKey = make_keypair()
print("Alice\'s secret key:\t", aliceSecretKey)
print("Alice\'s public key:\t", alicePublicKey)
print("Bob\'s secret key:\t", bobSecretKey)
print("Bob\'s public key:\t", bobPublicKey)

sharedSecret1 = scalar_mult(bobSecretKey, alicePublicKey)
sharedSecret2 = scalar_mult(aliceSecretKey, bobPublicKey)
print("Alice\'s shared key:\t", sharedSecret1)
print("Bob\'s shared key:\t", sharedSecret2)
print("The shared value is the x-value:\t", (sharedSecret1[0]))
print("Encryption/Decryption Key is 38-53 index numbers from the secret shared key:", str(sharedSecret1[0])[38:54])

tdBob = triple_des(str(sharedSecret2[0])[38:54], padmode=PAD_PKCS5)
tdAlice = triple_des(str(sharedSecret1[0])[38:54], padmode=PAD_PKCS5)

while True:
    app()
