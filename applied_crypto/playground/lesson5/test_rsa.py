# ssh-keygen -t rsa -m PEM
# openssl rsa -text -noout -in rsa_key

import subprocess
import sage.all as sage
rsa = subprocess.run(['openssl', 'rsa', '-text', '-noout', '-in', 'rsa_key'], stdout=subprocess.PIPE).stdout

print(rsa.decode())

def format_hex(str):
    return str.replace(":", "")


pstr = "00:ed:07:04:18:de:94:36:d2:9d:93:5b:cf:c2:96:33:fe:8c:79:06:73:0b:a6:37:f7:02:84:c7:2f:e6:92:dc:f6:47:83:6e:58:b6:a4:2c:c7:80:80:52:02:7a:58:dc:3d:da:7d:0d:cb:bb:34:5f:2c:94:df:3a:ac:37:d8:07:c1:86:22:b2:d1:41:6a:bf:96:c2:5d:2f:7a:8c:6a:69:98:e9:45:ac:f4:1d:78:32:c5:ae:68:06:33:d8:e1:73:38:86:4b:3f:5e:d2:0e:68:e9:32:f2:d7:fd:3e:0b:6a:e9:b8:7a:0b:ac:7e:8a:73:e4:49:af:a8:52:71:5c:df:57"
phex = format_hex(pstr)
qstr = "00:d0:21:cd:14:39:2b:aa:51:76:78:6d:67:5d:46:4c:bf:c5:21:58:5e:65:6a:d2:80:f5:f8:0a:13:d9:00:81:ff:e6:4e:31:c8:8f:36:6f:7b:03:4d:7e:3f:81:8a:a5:b4:1f:8e:9e:ca:50:f8:ec:34:e0:06:47:eb:40:76:df:c8:91:c4:88:27:0c:aa:15:19:d1:d2:56:3a:11:ac:b7:2b:4f:1e:c2:20:7f:6e:cc:60:cd:2b:26:0b:f9:6b:ef:7d:c8:60:f9:de:25:8b:00:77:77:2e:68:a0:2c:d0:32:e8:9f:95:17:6a:c5:e4:ff:bf:6e:96:de:ae:06:66:57:e7"
qhex = format_hex(qstr)
nstr = "00:c0:b4:ff:1d:13:d0:57:9d:94:06:ea:7a:fa:dc:ae:1f:a2:19:6c:27:e8:86:95:8b:c3:eb:5d:ab:75:6d:9d:1f:fe:28:47:13:6e:4a:cb:49:23:f9:3f:7d:d6:3a:0b:51:d3:2a:de:2b:f1:0b:fe:05:c0:66:37:6d:0e:a5:d8:65:42:da:35:18:88:e4:43:6a:ed:2f:f7:ab:63:76:3a:0c:f6:9a:52:a1:c0:f5:42:67:eb:c2:b5:71:97:9d:e2:c1:41:bb:4e:ca:44:6a:5c:f4:e6:03:95:31:4d:44:53:17:8a:75:56:c6:49:04:77:c1:16:7f:c6:11:54:03:6b:ac:0c:96:8d:9b:2f:a2:19:12:57:b7:96:27:a2:29:3a:e5:33:0f:8b:08:94:9c:24:93:fa:8d:0e:6f:4b:a1:02:e3:6f:36:5d:cf:62:6f:b5:60:6c:6b:76:ac:6a:bf:cb:6f:9c:f8:28:87:75:57:bc:22:dc:bb:13:8c:52:07:cb:ba:80:0e:8f:84:eb:e3:c4:78:93:77:4f:c3:46:05:da:bf:39:ce:6b:c5:55:e0:3d:16:55:db:34:09:8b:98:dc:4b:c5:df:86:18:f4:38:13:bf:3a:95:bb:40:18:16:3e:05:50:5b:a3:e2:2c:9f:27:9b:04:fd:7e:49:e1:5e:18:81"
nhex = format_hex(nstr)
dstr = "05:66:0c:af:97:da:82:59:db:c7:c5:d1:e4:2d:42:83:88:5b:05:f8:a8:3e:fc:f9:89:67:92:9c:37:11:f7:10:ea:61:de:7b:e0:df:1f:8a:d1:03:2e:90:2b:ec:3c:5c:f2:79:84:f7:de:2c:e3:d4:ed:6a:ef:aa:92:7a:7a:f1:7b:49:f9:aa:d2:4a:f2:c8:90:14:83:ef:bd:3d:96:aa:be:4d:dc:7a:c3:99:1b:5f:25:ef:b2:7d:98:2d:c8:28:79:da:f1:7e:21:24:89:ae:22:b3:7e:fe:7e:97:a7:6c:45:68:bc:21:99:f2:12:18:ca:b4:91:ab:f2:9a:95:ed:93:84:13:7f:52:13:f8:55:28:78:2b:a9:a1:3c:dd:0a:31:ce:c2:8a:58:e8:90:b6:b0:28:1c:4e:98:01:d9:d1:cf:bf:2e:c1:2d:f3:cf:5c:53:23:f7:81:8b:d1:88:0d:88:fe:ef:09:f8:54:44:0c:67:08:48:a3:53:66:26:9e:64:8c:95:85:ca:f5:fd:29:b1:31:25:ab:fb:70:68:ad:6b:80:b8:9f:8a:cf:10:b9:23:78:59:1f:81:9d:67:ae:94:44:4f:a6:ea:10:d7:dd:06:56:fd:08:89:a9:d6:cb:16:c1:ad:ea:01:4f:34:cf:7c:ca:b3:6a:cf:16:93:b1"
dhex = format_hex(dstr)


e = 65537
p = int(phex, 16)
q = int(qhex, 16)
n = int(nhex, 16)
d = int(dhex, 16)


print(n == p * q)
print(e * d % ((p-1)*(q-1)))
print(sage.is_prime(p))
print(sage.is_prime(q))


