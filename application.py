from triple_des import triple_des, PAD_PKCS5

chat = []

# td = triple_des("key", padmode=PAD_PKCS5)

def app():
    valid = False
    while not valid:
        user = input("Enter user: ")
        if user.lower() == "alice":
            valid = True
            user = "Alice"
        elif user.lower() == "bob":
            valid = True
            user = "Bob"
        else:
            print("Error: User not found...")
    print("--------------------CryptoWhatsApp--------------------")
    chatFile = open("chat.txt", "r")
    for line in chatFile:
        chat.append(line.split(": ", 1))
    for u, m in chat:
        # for each line decrypt here
        print(u, ": ", m, end="")
    chatFile.close()
    chatFile = open("chat.txt", "a")
    print(user, end="")
    msg = input(": ")
    # encrypt the message here
    message = user + ": " + msg + "\n"
    chatFile.write(message)
    chatFile.close()
    if user.lower() == "bob":
        chat.append((msg, "Bob"))
    else:
        chat.append((msg,"Alice"))


while True:
    app()