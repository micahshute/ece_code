import hashlib

f = open("dictionary.txt", 'r')
lines = f.readlines()
f.close()
md5s = []
for l in lines:
    md5s.append(hashlib.md5(l.encode()).hexdigest())

last4bytes = [h[-8:] for h in md5s]

last4bytes_len = len(last4bytes)
last4bytes_set = set(last4bytes)
unique_last_4_bytes = len(last4bytes_set)
print(f"{last4bytes_len} total words")
print(2 ** 32)
print(f"There are {last4bytes_len - unique_last_4_bytes} collisions")
l4bset = {}
collision_indices = []
for i in range(len(last4bytes)):
    if last4bytes[i] in l4bset:
        collision_indices.append(i)
        collision_indices.append(l4bset[last4bytes[i]])
    else: 
        l4bset[last4bytes[i]] = i

print(collision_indices)

collision_words = [lines[i] for i in collision_indices]
print(collision_words)