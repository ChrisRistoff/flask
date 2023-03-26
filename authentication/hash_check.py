import random
import string
import hashlib

def hash_password(password):
    salt = ''.join(random.choice(string.ascii_letters
                    + string.digits) for _ in range(16))
    salted = password + salt
    hashed = hashlib.sha256(salted.encode('utf-8')).hexdigest()
    return hashed, salt

def check_password(password, hashed, salt):
    salted = password + salt
    return hashed == hashlib.sha256(salted.encode('utf-8')).hexdigest()

def main():
    password = input('password: ')
    hashed, salt = hash_password(password)
    print('hashed :', hashed)
    input_password = input('again to check: ')
    if check_password(input_password, hashed, salt):
        print('match.')
    else:
        print('no match.')

if __name__ == '__main__':
    main()
