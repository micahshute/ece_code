import bcrypt
import hashlib


# salt = bcrypt.gensalt()
salt = "$2a$12$5Bx/CBG3xoXor78zB8DSRe"
password = 'password'

def hash(password, salt, r=1):
    to_hash = password + salt
    current_hash = ''
    for _ in range(r):
        current_hash = hashlib.sha256((current_hash + to_hash).encode('utf-8')).hexdigest()
    return current_hash

my_hash = hash(password, salt, 3)
print(my_hash)

print('test')
x1 = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
x2 = hashlib.sha256((x1 + password + salt).encode('utf-8')).hexdigest()
x3 = hashlib.sha256((x2 + password + salt).encode('utf-8')).hexdigest()
print('passed') if(x3 == my_hash) else print('failed')
