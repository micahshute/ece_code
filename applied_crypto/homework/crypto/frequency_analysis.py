import re
import math
from random import randint

class FrequencyAnalysis:

    english_ioc = 1.73

    # From Wikipedia 
    english_letter_frequencies = {
        "A": 0.08167,
        "B": 0.01492,
        "C": 0.02782,
        "D": 0.04253,
        "E": 0.12702,
        "F": 0.02228,
        "G": 0.02015,
        "H": 0.06094,
        "I": 0.06966,
        "J": 0.00153,
        "K": 0.00772,
        "L": 0.04025,
        "M": 0.02406,
        "N": 0.06749,
        "O": 0.07507,
        "P": 0.01929,
        "Q": 0.00095,
        "R": 0.05987,
        "S": 0.06327,
        "T": 0.09056,
        "U": 0.02758,
        "V": 0.00978,
        "W": 0.02360,
        "X": 0.00150,
        "Y": 0.01974,
        "Z": 0.00074
    }

    # From practicalcryptography.com
    bigram_frequencies = {
        "TH": 0.0271,
        "HE": 0.0233,
        "IN": 0.0203,
        "ER": 0.0178,
        "AN": 0.0161,
        "RE": 0.0141,
        "ES": 0.0132,
        "ON": 0.0132,
        "ST": 0.0125,
        "NT": 0.0117,
        "EN": 0.0113,
        "AT": 0.0112, 
        "ED": 0.0108,  
        "ND": 0.0107,
        "TO": 0.0107,
        "OR": 0.0106,
        "EA": 0.0100,
        "TI": 0.0099,
        "AR": 0.0098,
        "TE": 0.0098,
        "NG": 0.0089,
        "AL": 0.0088,
        "IT": 0.0088,
        "AS": 0.0087,
        "IS": 0.0086,
        "HA": 0.0083,
        "ET": 0.0076,
        "SE": 0.0073,
        "OU": 0.0072,
        "OF": 0.0071
    }

    trigram_frequencies = {
        "THE":  0.0181,              
        "AND":  0.0073,               
        "ING":  0.0072,              
        "ENT":  0.0042,               
        "ION":  0.0042,             
        "HER":  0.0036,               
        "FOR":  0.0034,              
        "THA":  0.0033,              
        "NTH":  0.0033,               
        "INT":  0.0032,               
        "ERE":  0.0031,  
        "TIO":  0.0031, 
        "TER":  0.0030,  
        "EST":  0.0028, 
        "ERS":  0.0028,   
        "ATI":  0.0026, 
        "HAT":  0.0026,  
        "ATE":  0.0025,  
        "ALL":  0.0025, 
        "ETH":  0.0024, 
        "HES":  0.0024,
        "VER":  0.0024,
        "HIS":  0.0024,
        "OFT":  0.0022,
        "ITH":  0.0021,
        "FTH":  0.0021,
        "STH":  0.0021,
        "OTH":  0.0021,
        "RES":  0.0021,
        "ONT":  0.0020
    }

    @classmethod
    def unigram_autocorrelation(cls):
        return sum([freq ** 2 for letter, freq in cls.english_letter_frequencies.items()])

    @classmethod
    def bigram_autocorrelation(cls):
        return sum([freq ** 2 for bigram, freq in cls.bigram_frequencies.items()])

    @classmethod
    def trigram_autocorrelation(cls):
        return sum([freq ** 2 for trigram, freq in cls.trigram_frequencies.items()])

    @classmethod
    def letters_ordered_by_frequency(cls):
        return [ char for (char, freq) in sorted(cls.english_letter_frequencies.items(), key=lambda item: item[1], reverse=True) ]

    def __init__(self, phrase, keylen=0):
        regex = re.compile('[^a-zA-Z]')
        self.ciphertext = regex.sub('', phrase).upper()
        self.keylen = keylen
        self.letter_histogram = self.create_character_histogram()
        self.total_chars = sum(self.letter_histogram.values())
        self._ciphertext_bigram_frequencies = {}
        self.total_bigrams = 0
        self._ciphertext_trigram_frequencies = {}
        self.total_trigrams = 0

    @property
    def ciphertext_bigram_frequencies(self):
        if len(self._ciphertext_bigram_frequencies.keys()) == 0:
            self.set_bigram_frequencies()
        return self._ciphertext_bigram_frequencies
    
    @ciphertext_bigram_frequencies.setter
    def ciphertext_bigram_frequencies(self, newval):
        self._ciphertext_bigram_frequencies = newval

    @property
    def ciphertext_trigram_frequencies(self):
        if len(self._ciphertext_trigram_frequencies.keys()) == 0:
            self.set_trigram_frequencies()
        return self._ciphertext_trigram_frequencies
    
    @ciphertext_trigram_frequencies.setter
    def ciphertext_trigram_frequencies(self, newval):
        self._ciphertext_trigram_frequencies = newval

    def english_correlation_distance(self):
        return abs(self.english_correlation() - FrequencyAnalysis.unigram_autocorrelation())

    def bigram_correlation_distance(self):
        return abs(self.english_bigram_correlation() - FrequencyAnalysis.bigram_autocorrelation())

    def trigram_correlation_distance(self):
        # code.interact(local=dict(globals(), **locals()))
        return abs(self.english_trigram_correlation() - FrequencyAnalysis.trigram_autocorrelation())

    def english_correlation(self):
        lf = self.letter_frequencies()
        corr = 0
        for letter, freq in lf.items():
            corr += (freq * FrequencyAnalysis.english_letter_frequencies[letter])
        # corr should be about 0.065
        # print(corr)
        return corr

    def unigram_log_score(self):
        minval = 0.0001
        sum = 0
        for char, count in self.letter_histogram.items():
            probability = FrequencyAnalysis.english_letter_frequencies[char]
            sum += count * math.log10(probability)
        return sum

    def bigram_log_score(self):
        minval = 0.0001
        sum = 0
        for char, freq in self.ciphertext_bigram_frequencies.items():
            probability = FrequencyAnalysis.bigram_frequencies.get(char, 0)
            # code.interact(local=dict(globals(), **locals()))
            if probability == 0:
                probability = minval
            sum += (freq * self.total_bigrams) * math.log10(probability)
        return sum

    def trigram_log_score(self):
        minval = 0.0001
        sum = 0
        for char, freq in self.ciphertext_trigram_frequencies.items():
            probability = FrequencyAnalysis.trigram_frequencies.get(char, 0)
            # code.interact(local=dict(globals(), **locals()))
            if probability == 0:
                probability = minval
            sum += (freq * self.total_trigrams) * math.log10(probability)
        return sum
        



    def english_bigram_correlation(self):
        if len(self.ciphertext_bigram_frequencies.keys()) == 0: self.set_bigram_frequencies()
        corr = 0
        for bigram, freq in self.ciphertext_bigram_frequencies.items():
            corr += (freq * FrequencyAnalysis.bigram_frequencies.get(bigram, 0))
        return corr

    def english_trigram_correlation(self):
        if len(self.ciphertext_trigram_frequencies.keys()) == 0: self.set_trigram_frequencies()
        corr = 0
        for trigram, freq in self.ciphertext_trigram_frequencies.items():
            corr += (freq * FrequencyAnalysis.trigram_frequencies.get(trigram, 0))
        return corr

    def frequency_autocorrelation(self):
        lf = self.letter_frequencies()
        corr = 0
        for _, freq in lf.items():
            corr += (freq ** 2)
        return corr

    def ioc_deviation(self):
        return abs(self.index_of_coincidence() - FrequencyAnalysis.english_ioc)


    def index_of_coincidence(self):
        # \mathbf{IC} = \frac{\displaystyle\sum_{i=1}^{c}n_i(n_i -1)}{N(N-1)/c}
        c = 26
        num = sum([(count * (count - 1)) for char, count in self.letter_histogram.items()])
        den = (self.total_chars * (self.total_chars - 1)) / c
        if den == 0: return 0
        return num / den

    def create_character_histogram(self):
        hist = {}
        for char in self.ciphertext:
            if(char in hist):
                hist[char] += 1
            else:
                hist[char] = 1
        return hist

    # Dictionaries preserve order in python >= 3.7, so we can order these and maintain it
    def letter_frequencies(self):
        return { char: (count / self.total_chars) for (char, count) in sorted(self.letter_histogram.items(), key=lambda item: item[1], reverse=True) }


    def set_bigram_frequencies(self):
        bigrams = {}
        chars = [char for char in self.ciphertext]
        bigrams[f"{chars[0]}{chars[1]}"] = 1
        for i in range(1, len(chars)):
            bigram = f"{chars[i-1]}{chars[i]}"
            if bigram in bigrams:
                bigrams[bigram] += 1
            else:
                bigrams[bigram] = 1
        total_bigrams = sum(bigrams.values())
        self.total_bigrams = total_bigrams
        self.ciphertext_bigram_frequencies = { bigram: (count / total_bigrams) for (bigram, count) in sorted(bigrams.items(), key=lambda item: item[1], reverse=True) }


    def set_trigram_frequencies(self):
        trigrams = {}
        chars = [char for char in self.ciphertext]
        trigrams[f"{chars[0]}{chars[1]}{chars[2]}"] = 1
        trigrams[f"{chars[1]}{chars[2]}{chars[3]}"] = 1
        for i in range(2, len(chars)):
            trigram = f"{chars[i-2]}{chars[i-1]}{chars[i]}"
            if trigram in trigrams:
                trigrams[trigram] += 1
            else:
                trigrams[trigram] = 1
        total_trigrams = sum(trigrams.values())
        self.total_trigrams = total_trigrams
        self.ciphertext_trigram_frequencies = { trigram: (count / total_trigrams) for (trigram, count) in sorted(trigrams.items(), key=lambda item: item[1], reverse=True) }

