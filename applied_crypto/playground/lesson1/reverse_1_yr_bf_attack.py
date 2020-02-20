import bcrypt
import math
import time
import hashlib
# Intellectual Challenge : Compute an r such that a single 
# common word from the dictionary is enough that it takes 1 
# core-year to brute-force reverse this hash scheme. How long 
# would it take for your user to compute a single hash?

words_in_dict = 187632
# words_per_sec = words_in_dict / 0.1
sec_per_year = 60 * 60 * 24 * 365.25
hash_iterations_per_second = 1500000

seconds_needed_for_one_hash = sec_per_year / words_in_dict
iterations_needed = math.ceil(seconds_needed_for_one_hash * hash_iterations_per_second)

print(f"Iterations required: {iterations_needed}") # 252,283,193 iterations required

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


salt = bcrypt.gensalt().decode()
time_for_a_single_hash = password_timing_test(salt, "i<3wilmy", iterations_needed)
print(f"Time needed for a single hash: {time_for_a_single_hash} seconds") #421.104124 seconds