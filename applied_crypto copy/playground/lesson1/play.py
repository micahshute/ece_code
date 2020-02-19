from python_resources.frequency_analysis import *

# text = 'wndzewrgxtszml'
# fa = FrequencyAnalysis(text)
# print(FrequencyAnalysis.bf_decrypt_cc(fa.ciphertext))

# print(FrequencyAnalysis.decrypt_cc(19, text))
# fa = FrequencyAnalysis(text)
# keylen = fa.find_keylen()
# print(keylen)
# fa.keylen = keylen
# key = fa.vc_freq_analysis_correlation()
# print(key)
# res = fa.decrypt_with_vc(key.values())
# print(res)


text = "this is my deepest darkest secret that I hope that nobody ever finds out, so I am going to encode it!"# But, I will put some more text here so that there is enough data for a really smart person to decrypt it."
fa = FrequencyAnalysis(text)
key = [2, 12, 21, 7, 17, 5]
ciphertext = FrequencyAnalysis.encrypt_vc(key, fa.ciphertext)
breaker = FrequencyAnalysis(ciphertext)
print(breaker.crack_vigenere())
breaker.keylen = 6
print(breaker.decrypt_with_vc(breaker.vc_freq_analysis_correlation().values()))