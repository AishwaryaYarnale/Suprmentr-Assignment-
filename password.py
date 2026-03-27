import hashlib
import getpass

# Predefined user details
USERNAME = "aishwarya"
PASSWORD_HASH = hashlib.sha256("Aish@123".encode()).hexdigest()

# Login function
def login():
    print("=== Login System ===")
    attempts = 3

    while attempts > 0:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        if username == USERNAME and hashlib.sha256(password.encode()).hexdigest() == PASSWORD_HASH:
            print("Login successful! Access granted.")
            return
        else:
            attempts -= 1
            print(f"Wrong credentials! Attempts left: {attempts}")

    print("Account locked!")

# Run program
login()