from random import randint

def evenpad(hex):
    return ('0' * (len(hex) % 2)) + hex[2:]

 
message = "my deepest darkest secret"

message_hex = message.encode().hex()
message_int = int(message_hex, 16)

xornum = randint(message_int * 2, message_int * 10)
# xornum = 12
print(f"Message: {message}\nMsg Hex: {message_hex}\nMsg Int: {message_int}")

xord_message = message_int ^ xornum
print(f"{message_int} XOR {xornum} = {xord_message}")

print(f"binary orginal message: {bin(message_int)}")
print(f"binary xord message: {bin(xord_message)}")

message_int2 = xord_message ^ xornum

message_hex2 = evenpad(hex(message_int2))

decoded_message = bytearray.fromhex(message_hex2).decode()

print(f"Message: {decoded_message}")

# print(f"Decoded xored number: {bytearray.fromhex(evenpad(hex(xord_message))).decode()}")