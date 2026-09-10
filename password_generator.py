import random
import string

length = int(input("Password length: "))
if length < 6:
    print("Password length must be at least 6.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

        print("Your password:", password)

