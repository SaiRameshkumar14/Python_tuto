
# import hashlib
 
# # Declaring Password
# password = 'GeeksPassword'
# # adding 5gz as password
# salt = "5gz"
 
# # Adding salt at the last of the password
# dataBase_password = password+salt
# # Encoding the password
# hashed = hashlib.md5(dataBase_password.encode())
 
# # Printing the Hash
# print(hashed.hexdigest())


# import bcrypt

# def hash_password(password: str) -> str:
#     salt = bcrypt.gensalt()
#     hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
#     return hashed.decode('utf-8')

# def verify_password(password: str, hashed: str) -> bool:
#     return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# # Example usage
# if __name__ == "__main__":
#     password = input("Password : ")
#     hashed_password = hash_password(password)
#     print(f"Hashed password: {hashed_password}")
    
#     is_valid = verify_password(password, hashed_password)
#     print(f"Password is valid: {is_valid}")


from passlib.context import CryptContext

# Create a CryptContext with the desired hashing algorithm
encrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return encrypt.hash(password)

def verify_password(password: str, hashed: str) -> str:
    return encrypt.verify(password, hashed)

# Example usage
password = "my_secure_password"
hashed_password = hash_password(password)
print(f"Hashed password: {hashed_password}")

is_valid = verify_password(password, hashed_password)
print(f"Password is valid: {is_valid}")


########################################################################################


from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
# In a real application, you should store this key securely
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_password(password: str) -> str:
    encrypted_text = cipher_suite.encrypt(password.encode())
    return encrypted_text.decode('utf-8')

def decrypt_password(encrypted_password: str) -> str:
    decrypted_text = cipher_suite.decrypt(encrypted_password.encode())
    return decrypted_text.decode('utf-8')

# Example usage
if __name__ == "__main__":
    password = "my_secure_password"
    encrypted_password = encrypt_password(password)
    print(f"Encrypted password: {encrypted_password}")

    decrypted_password = decrypt_password(encrypted_password)
    print(f"Decrypted password: {decrypted_password}")
