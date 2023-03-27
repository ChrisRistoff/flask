import random
import string
import hashlib

def hash_password(password):
    salt = ''.join(random.choice(string.ascii_letters
                    + string.digits) for _ in range(16))
    salted = password + salt
    hashed = hashlib.sha256(salted.encode('utf-8')).hexdigest()
    return hashed

def check_password(password, hashed):
    salt = hashed[:16]
    return hashed == hash_password(password + salt)

def main():
    current_password = 'password'
    password = input('Password: ')
    hashed = hash_password(password)
    print('Hashed:', hashed)
    print('Check:', check_password(current_password, hashed))

if __name__ == '__main__':
    main()
