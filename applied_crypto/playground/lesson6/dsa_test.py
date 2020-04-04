import sage.all as sage
import hashlib
# run with: sage -python3 dsa_test.py

priv ="00:93:51:cb:3a:65:70:a1:64:06:05:ce:52:80:b2:b7:12:c0:87:0a:f1"
pub = "71:4d:6b:51:fe:8d:a2:d2:1f:54:db:b2:c7:09:08:be:7e:94:da:a6:20:90:f8:f9:9b:2e:6e:2e:c5:b9:a8:f9:50:6a:f3:5d:eb:a5:6c:2a:cb:10:b7:db:39:95:63:15:c5:75:08:5f:34:1e:00:e1:90:d0:dd:ad:25:f1:db:f1:d6:7b:00:3b:3f:71:b8:d0:6d:08:0a:8a:11:30:e2:4d:5a:00:6b:45:5a:8d:9f:72:38:5e:a7:65:35:54:62:d4:0b:fa:cb:55:d0:10:dc:7a:71:5c:f4:0b:25:ec:fc:62:8c:dd:49:c1:a7:a5:96:cc:c0:9e:bb:50:88:72:9b:68"
p = "00:b7:61:89:03:4d:1c:0f:e7:eb:bb:d8:08:7e:d2:2c:ce:23:87:12:e0:9e:9d:40:fa:c1:3f:dd:77:f3:e5:5e:5a:8d:b9:9f:6b:b6:a9:32:20:63:97:c6:a5:2d:fc:81:8c:62:36:e1:5f:68:84:9b:bc:44:03:c8:07:b4:52:56:27:3f:f0:fe:6d:5c:24:db:52:8b:62:e3:a2:1f:df:a3:25:6f:0d:45:8a:af:83:8f:be:e3:c4:9c:97:3e:2b:45:95:da:fd:81:b9:ea:14:5b:9f:0f:0a:47:7c:ca:e3:2f:63:cc:64:0c:38:26:fd:e0:d1:aa:57:3f:8b:8e:86:51:4f"
q = "00:95:95:38:e8:29:ae:41:81:65:6b:60:11:f1:47:f5:9b:98:22:7d:39"
g = "00:b2:fe:52:65:71:4e:58:19:37:3e:8b:11:11:7e:9f:0f:f0:85:c6:6d:8d:a7:f4:6d:52:73:fc:f2:10:78:59:bf:a6:e7:7a:6d:25:5b:95:90:d9:e4:39:60:bf:e5:41:fe:20:36:24:df:f3:d0:3b:21:ea:a5:15:6b:24:1f:68:c4:d5:fe:f6:e8:08:67:22:4d:1e:5b:b3:b6:4c:60:97:ed:ef:54:f7:60:de:41:14:66:1c:48:98:64:c6:ea:7a:c6:28:87:b9:70:b6:53:33:43:8f:63:57:cb:91:31:2d:65:dd:e8:9c:e2:b9:8d:86:02:85:62:08:4b:ae:fe:28:89"
r = "57A3FA59846F6430CBFC0C6314A0678F23801401"
s = "6BC7308E77994DCE9D8451630BAFE39AB1B0AB8F"

msg = "micah is great\n"

def format_hex(h):
    return h.replace(":", "")

def inv_mod(a,b):
    r, rm1 = b, a
    s, sm1 = 0, 1
    t, tm1 = 1, 0
    while r != 0:
        q = rm1 // r
        rm1, r = r, rm1 % r
        sm1, s = s, sm1 - q * s
        tm1, t = t, tm1 - q * t
    d = sm1 * a + tm1 * b
    # return d, sm1, tm1
    return sm1

pint = int(format_hex(p), 16)
qint = int(format_hex(q), 16)
gint = int(format_hex(g), 16)
pubint = int(format_hex(pub), 16)
privint = int(format_hex(priv), 16)
rint = int(r, 16)
sint = int(s, 16)

print ((pint - 1) % qint)
print(pow(gint, qint, pint))
print(sage.is_prime(pint))
print(sage.is_prime(qint))

print(pubint == pow(gint, privint, pint))

z = int(hashlib.sha256(msg.encode()).hexdigest()[:40], 16)

ke = inv_mod(sint * inv_mod(z + privint * rint, qint), qint) % qint

g_kemod = pow(gint, ke, pint) % qint

print(g_kemod)
print(rint)
print(sint)