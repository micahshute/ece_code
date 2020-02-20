from random import random, randint
import binascii


m="Hi there! Probability says no."

print(m)
hexstr = m.encode().hex()
print(hexstr)
integer_m = int(hexstr, 16)
print(integer_m)
# back2hex = format(integer_m, 'x')
back2hex = hex(integer_m)
print(back2hex)
evenpad = ('0' * (len(back2hex) % 2)) + back2hex[2:]
print(evenpad)
plaintext = bytearray.fromhex(evenpad).decode()
print(plaintext)



# random.randint(a, b)
# Return a random integer N such that 
# a <= N <= b. Alias for randrange(a, b+1).


# x = 240
# for _ in range(10):
#     r = randint(0,255)
#     y = x ^ r
#     print(f"{x} XOR {r} = {y}")
#     print(f"{bin(x)} XOR {bin(r)} = {bin(y)}")


# m="Hi there"

# print m

# hexstr = m.encode('hex')

# print hexstr

# integer_m = int(hexstr, 16)

# print integer_m

# back2hex = format(integer_m, 'x')

# print back2hex

# evenpad = ('0' * (len(back2hex) % 2)) + back2hex

# plaintext = evenpad.decode('hex')

# print plaintext




