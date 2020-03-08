from python_resources.functions import *


cipherhex = 'e5d8443c6ac32d3ee5c7398ecf7f9e03f619'
seed = 54321

gen = crand(54321)

plainhex = stream_cipher(gen, cipherhex, decode=True)
print(plainhex)
msg = hex2str(plainhex)
print(msg)