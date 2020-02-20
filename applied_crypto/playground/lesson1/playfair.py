from python_resources.frequency_analysis import *
import math

def construct_key(keyphrase):
    seen_letters = set()
    ktxt = FrequencyAnalysis(keyphrase).ciphertext
    [seen_letters.add(char) for char in ktxt]
    fbf = [[[],[],[],[],[]] for _ in range(5) ]
    for i in range(25):
        col = i % 5
        row = math.floor(i / 5)





phrase = "It's all about the money"
phrase2 = "playfair example"
print(construct_key(phrase))