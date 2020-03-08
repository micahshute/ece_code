from python_resources.functions import *


msg = "tryin a do wilmy"
seed = 7136531
gen1 = crand(seed)
gen2 = crand(seed)

chex = stream_cipher(gen1, msg, decode=False)
phex = stream_cipher(gen2, chex, decode=True)
pmsg = hex2str(phex)
print(pmsg)
