import hashlib


phrase = 'andy rocks your face off'.encode('utf-8')
hash_phrase = hashlib.sha512(phrase)
hexdigest = hash_phrase.hexdigest()
print(hexdigest)