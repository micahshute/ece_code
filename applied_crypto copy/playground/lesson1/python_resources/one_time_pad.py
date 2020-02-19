from python_resources.functions import *
import os


class OneTimePad:

    def __init__(self, key=0):
        self.key = key
    
    def set_key(self, size):
        self.key = os.urandom(size)

    def encode(self, msg):
        if not self.key: self.set_key(len(msg))
        key_int = to_int(self.key)
        msg_int = str2int(msg)
        msg_int = key_int ^ msg_int
        hexdigest = to_hex(msg_int)
        return hexdigest, self.key

    def decode(self, hexdigest, key=0):
        if not key: key = self.key
        int_digest = to_int(hexdigest)
        decoded_int = int_digest ^ to_int(key)
        return int2str(decoded_int)
