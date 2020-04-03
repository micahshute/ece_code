
def safe_prime(bits):
    found_safe_prime = False
    ohshit = 0
    while (not found_safe_prime and ohshit < 1000000):
        ohshit += 1
        q = 2*randint(2**(bits-1), 2**(bits))-1
        if power_mod(2,2*q, 2*q + 1) != 1:
            continue
        if not q.is_prime(False):
            continue
        found_safe_prime = True
    if ohshit >= 1000000:
        return -1
    return 2*q+1