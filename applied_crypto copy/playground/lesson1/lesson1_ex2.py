import hashlib


dic = open('dictionary.txt', 'r')
secret_file = open('secret', 'r')
secret = secret_file.read().strip()
secret_file.close()

[print(word) for word in dic if hashlib.sha512(word.strip().encode('utf-8')).hexdigest() == secret]

dic.close()
