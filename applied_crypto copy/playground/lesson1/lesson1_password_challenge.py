import bcrypt
import hashlib
import time


# salt = bcrypt.gensalt()
salt = "$2a$12$5Bx/CBG3xoXor78zB8DSRe"
password = 'password'

def salted_password_hash(salt, password, r):
    hash = ''
    for i in range(r):
        hash = hashlib.sha256((hash + password + salt).encode('utf-8')).hexdigest()
    return hash

def password_timing_test(salt, password, r):
    start = time.process_time()
    salted_password_hash(salt, password, r)
    end = time.process_time()
    return end - start

def r_for_desired_time(salt, password, des_time_sec):
    rval = 605000
    while True:
        time_elapsed = password_timing_test(salt, password, rval)
        if(rval % 1000 == 0):
            print(f"For r = {rval}, seconds = {time_elapsed}")
        if(time_elapsed > des_time_sec):
            break
        rval += 1
    return rval


# print(r_for_desired_time(salt, password, 1)) #  1500000

rval = 1500000
# rval = 380000





## Part 2

def password_hasher(password):
    r = 1500000
    salt = bcrypt.gensalt().decode('utf-8')
    hash = ''
    for _ in range(r):
        hash = hashlib.sha256((hash + password + salt).encode('utf-8')).hexdigest()
    return [salt, r, hash]

password = "i<3wilmy"
hashed_password_and_info = password_hasher(password)
print(hashed_password_and_info)
print("check")
hashed_password_check = salted_password_hash(hashed_password_and_info[0], password, hashed_password_and_info[1])
print(hashed_password_check == hashed_password_and_info[2])