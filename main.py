import random 
import string

def password_generator(key):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(key))

    return password

key_generator = password_generator(12)
print(f"Your password: {key_generator}")

    