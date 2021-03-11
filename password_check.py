MIN_PASSWORD_LENGTH = 10

password = input("Password (min. length: {}): ".format(MIN_PASSWORD_LENGTH))
while len(password) < MIN_PASSWORD_LENGTH:
    print("Password must be {} characters long.".format(MIN_PASSWORD_LENGTH))
    password = input("Password (min. length: {}): ".format(MIN_PASSWORD_LENGTH))
print("*" * len(password))
