import os
from python_resources.functions import *
from python_resources.one_time_pad import *

msg = "iLiKeTuRtLeS"
rand_num = os.urandom(12)
print(rand_num)
msg_hex = msg.encode().hex()
msg_int = int(msg_hex, 16)
xor_int = int(rand_num.hex(), 16)

encrypted_int = msg_int ^ xor_int
encrypted_hex = hex(encrypted_int)
print(encrypted_hex)
hexdigest = ('0' * (len(encrypted_hex) % 2)) + encrypted_hex[2:]

print(hexdigest)

intdigest = int(hexdigest, 16)

retreived_msg_int = intdigest ^ xor_int

retreived_msg_hex = hex(retreived_msg_int)
retreived_msg = bytearray.fromhex(retreived_msg_hex[2:]).decode()
print(retreived_msg)


# NOW TRY AGAIN WITH HELPER FUNCTIONS
print('---------------------------------')
msg2 = "iLiKeTuRtLeS"
rand_num2 = os.urandom(12)
print(rand_num2)
rand_int2 = to_int(rand_num2)
msg_int2 = str2int(msg2)

xor_int2 = rand_int2 ^ msg_int2
hexdigest = to_hex(xor_int2)
print(hexdigest)

hexdigest_int = to_int(hexdigest)
decoded_int = hexdigest_int ^ rand_int2

decoded_str = int2str(decoded_int)

print(decoded_str)

print('--------------------------')

msg3 = "iLiKeTuRtLeS"
otp = OneTimePad()
hexdigest, key = otp.encode(msg3)
print(key)
print(hexdigest)
originalmsg = otp.decode(hexdigest)

print(originalmsg)


print('-------------------------')
print('should be the same hexdigest as the second example:')

otp2 = OneTimePad(rand_num2)
hexdigest, key = otp2.encode(msg3)
print(hexdigest)
print(key)

msg = otp2.decode(hexdigest)
print(msg)
