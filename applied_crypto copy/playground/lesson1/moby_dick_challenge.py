import ssl
from urllib.request import urlopen
from python_resources.frequency_analysis import *


res = urlopen("https://vip.udel.edu/crypto/mobydick.txt", context=ssl._create_unverified_context())
txt = res.read().decode()

fa = FrequencyAnalysis(txt)

print(f"Autocorelation of freqs: {fa.frequency_autocorrelation()}")
print(f"English correlation: {fa.english_correlation()}")
# print(f"Freq chart: {fa.letter_frequencies()}")


enres = urlopen("https://vip.udel.edu/crypto/encrypted_mobydick.txt",  context=ssl._create_unverified_context())
entxt = enres.read().decode()

enfa = FrequencyAnalysis(entxt)

print(f"Autocorelation of freqs: {enfa.frequency_autocorrelation()}")
print(f"English correlation: {enfa.english_correlation()}")
# print(f"Freq chart: {enfa.letter_frequencies()}")

keylen = enfa.find_keylen(20)
enfa.keylen = keylen
keys = enfa.vc_freq_analysis_correlation()
print(keys.values())
out = enfa.decrypt_with_vc(keys.values())
# print(out)