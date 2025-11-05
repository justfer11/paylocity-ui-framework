from cryptography.fernet import Fernet

key = b'Yh9KYkdf8epBRbwZy4w1nB-un-lfTEdbg5ITQO6pnLw='  # paste your key here
fernet = Fernet(key)

password = "U&fTVxE$a?l0"
encrypted = fernet.encrypt(password.encode())
print("Encrypted password:", encrypted.decode())