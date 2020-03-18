from PIL import Image
from Crypto import Random
from Crypto.Cipher import AES
import hashlib
import os

class ImageEncrypter:

    def __init__(self, path, *, key, writepath="output_pic.png", iv=None, aes_mode=AES.MODE_CTR, key_hashed=True, counter=None, rand_iv=True):
        self.path = path
        if key_hashed:
            self.key = hashlib.sha256(key.encode()).digest()
        else: 
            self.key = bytes.fromhex(key)
            self.key_is_hex = False
        self.writepath = writepath
        self.iv = iv
        self.rand_iv = rand_iv
        
        self.aes_mode = aes_mode
        self.counter = None

    def encrypt(self):
        self.__encrypt_decrypt__()

    def decrypt(self):
        self.__encrypt_decrypt__(False)

    def __encrypt_decrypt__(self, encrypt=True):
        aes = None

        if self.aes_mode == AES.MODE_ECB:
            aes = AES.new(self.key, self.aes_mode)
        elif self.aes_mode == AES.MODE_CBC:
            if self.iv is None and self.rand_iv:
                self.iv = os.urandom(16)
            aes = AES.new(self.key, self.aes_mode, iv=self.iv)
        elif self.aes_mode == AES.MODE_CFB:
            if self.iv is None and self.rand_iv:
                self.iv = os.urandom(16)
            aes = AES.new(self.key, self.aes_mode, iv=self.iv)
        elif self.aes_mode == AES.MODE_CTR:
            if self.iv is None and self.rand_iv:
                self.iv = os.urandom(8)
            aes = AES.new(self.key, self.aes_mode, nonce=self.iv, counter=self.counter)
        elif self.aes_mode == AES.MODE_OFB:
            if self.iv is None and self.rand_iv:
                self.iv = os.urandom(16)
            aes = AES.new(self.key, self.aes_mode, iv=self.iv)
        else:
            raise Exception("AES MODE not supported")
        img = Image.open(self.path)
        imgbytes = img.tobytes()
        mode = img.mode
        size = img.size
        e_img_bytes = None
        if encrypt:
            e_img_bytes = aes.encrypt(imgbytes)
        else:
            e_img_bytes = aes.decrypt(imgbytes)
        Image.frombytes(mode, size, e_img_bytes).save(self.writepath)


imgpath = "mill_falc.png"

ie = ImageEncrypter(imgpath, key='secret', aes_mode=AES.MODE_CBC)

ie.encrypt()
decrypt_iv = ie.iv
ie.path = ie.writepath
ie.writepath = "orig_pic.png"
ie.decrypt()

# CODE BELOW decrypts a pic if you know the IV (not stored in the object)
ie = ImageEncrypter('output_pic.png', key='secret', writepath="test.png", aes_mode=AES.MODE_CBC, iv=decrypt_iv)
ie.decrypt()