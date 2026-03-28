from cryptography.fernet import Fernet

# Generate a symmetric key

key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt a message

message = "This is a secret message."
token = cipher.encrypt(message.encode())

print("Encrypted message:", token)

# Decrypt the message

decrypted = cipher.decrypt(token).decode()
print("Decrypted message:", decrypted)