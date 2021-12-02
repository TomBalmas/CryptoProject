from triple_des import triple_des, PAD_PKCS5

users = ("Alice","Bob")
inboxes = ["",""] #always hidden messages
td = triple_des("asdf",padmode=PAD_PKCS5)

def app():
    user = input("Enter user: ")
    if user.lower() == "alice":
        user = "Alice"
        reciver = users[1]
        inbox = inboxes[0]
    else:
        user = "Bob"
        reciver = users[0]
        inbox = inboxes[1]
    print("--------------------CryptoWhatsApp--------------------")
    if inbox != "":
        print(reciver,": ",sep="",end="")
        print(inbox)
    print(user,end="")
    msg = input(": ")
    if user.lower() == "bob":
        inboxes[0] = msg
    else:
        inboxes[1] = msg
    #input crypto project
    return user,msg

while True:
    app()