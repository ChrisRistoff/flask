from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecret'
hashed_password = bcrypt.generate_password_hash(password)

print(hashed_password)

check = bcrypt.check_password_hash(hashed_password, 'asdasdasd')
print(check)
