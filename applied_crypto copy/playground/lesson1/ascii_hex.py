import binascii, hashlib

hexascii = hashlib.sha256("andy").hexdigest()
realhex = hashlib.sha256("andy").digest()

binary_for_hexascii = ""
binary_for_realhex = ""

for character in hexascii:
	binary_for_hexascii += bin(ord(character))[2:].zfill(8)
for character in realhex:
	binary_for_realhex += bin(ord(character))[2:].zfill(8)

print binary_for_hexascii
print binary_for_hexascii.count('0'), binary_for_hexascii.count('1')

print binary_for_realhex
print binary_for_realhex.count('0'), binary_for_realhex.count('1')