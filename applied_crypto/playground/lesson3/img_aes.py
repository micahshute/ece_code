from PIL import Image 
from Crypto import Random
from Crypto.Cipher import AES
import hashlib
import os


im = Image.open('heckert_gnu.png')

imgbytes = im.tobytes()
mode = im.mode #https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
size = im.size

iv = os.urandom(AES.block_size // 2)
key = hashlib.sha256(b'secret').digest()
aes = AES.new(key, AES.MODE_ECB)

eimgbytes = aes.encrypt(imgbytes)
Image.frombytes(mode, size, eimgbytes).save('output_ecb.png')


aes_ctr = AES.new(key, AES.MODE_CTR, nonce=iv)
ctr_bytes = aes_ctr.encrypt(imgbytes)
Image.frombytes(mode, size, ctr_bytes).save('output_ctr.png')