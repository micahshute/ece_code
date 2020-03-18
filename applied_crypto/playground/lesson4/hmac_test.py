import hmac, hashlib

print(hmac.new(b'secretkey', b'forge this punks', hashlib.sha256).hexdigest())
print("b815f8be415bc163b4e563c21a1ebd26d862f22a047c0aafd3dd0f919e653a0f")