from Crypto.Util import Counter
from Crypto.Cipher import AES
import binascii
ctr = Counter.new(128, initial_value=1)

aes = AES.new(b'abcdefghijklmnop', AES.MODE_CTR, counter=ctr)

ct = aes.encrypt(b'hello world')

print(ct)