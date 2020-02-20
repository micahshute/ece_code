import ssl
from urllib.request import urlopen
from python_resources.frequency_analysis import *

response = urlopen("https://vip.udel.edu/crypto/mobydick.txt", context=ssl._create_unverified_context())
mobytext = response.read().decode()
onlyletters = "".join(filter(lambda x: x.isalpha(), mobytext))
loweronly = onlyletters.lower()

frequency = {}
for ascii in range(ord('a'), ord('a')+26):
    frequency[chr(ascii)] = float(loweronly.count(chr(ascii)))/len(loweronly)

sum_freqs_squared = 0.0
for ltr in frequency:
    sum_freqs_squared += frequency[ltr]*frequency[ltr]

print("Should be near .065 if plain: " + str(sum_freqs_squared))

fa = FrequencyAnalysis(mobytext)
print(f"English Correlation Plain Text:{fa.english_correlation()}")
print(f"Freq Autocorrelation Plain Text: {fa.frequency_autocorrelation()}")
cc_moby = FrequencyAnalysis(FrequencyAnalysis.encrypt_cc(5, fa.ciphertext))
print(f"English Correlation Caesar Cipher: {cc_moby.english_correlation()}")
print(f"Freq Autocorrelation Caesar Cipher: {cc_moby.frequency_autocorrelation()}")
