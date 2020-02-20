import re
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

    @classmethod
    def unigram_autocorrelation(cls):
        return sum([freq ** 2 for letter, freq in cls.english_letter_frequencies.items()])

    @classmethod
    def bigram_autocorrelation(cls):
        return sum([freq ** 2 for bigram, freq in cls.bigram_frequencies.items()])

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

    @property
    def ciphertext_bigram_frequencies(self):
        if len(self._ciphertext_bigram_frequencies.keys()) == 0:
            self.set_bigram_frequencies()
        return self._ciphertext_bigram_frequencies
    
    @ciphertext_bigram_frequencies.setter
    def ciphertext_bigram_frequencies(self, newval):
        self._ciphertext_bigram_frequencies = newval

    def english_correlation_distance(self):
        return abs(self.english_correlation() - FrequencyAnalysis.unigram_autocorrelation())

    def bigram_correlation_distance(self):
        return abs(self.english_bigram_correlation() - FrequencyAnalysis.bigram_autocorrelation())

    def english_correlation(self):
        lf = self.letter_frequencies()
        corr = 0
        for letter, freq in lf.items():
            corr += (freq * FrequencyAnalysis.english_letter_frequencies[letter])
        # corr should be about 0.065
        # print(corr)
        return corr

    def english_bigram_correlation(self):
        if len(self.ciphertext_bigram_frequencies.keys()) == 0: self.set_bigram_frequencies()
        corr = 0
        for bigram, freq in self.ciphertext_bigram_frequencies.items():
            corr += (freq * FrequencyAnalysis.bigram_frequencies.get(bigram, 0))
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
        self.ciphertext_bigram_frequencies = { bigram: (count / total_bigrams) for (bigram, count) in sorted(bigrams.items(), key=lambda item: item[1], reverse=True) }


    def crack_substitution(self):
        mapping = {}
        lf = self.letter_frequencies()
        elf = FrequencyAnalysis.letters_ordered_by_frequency()

        letter_set = set(elf)
        for cipher_char, cipher_freq in lf.items():
            closest_char = None
            closest_distance = float('inf')
            for english_char, english_freq in FrequencyAnalysis.english_letter_frequencies.items():
                distance = abs(cipher_freq - english_freq)
                if( distance < closest_distance and english_char in letter_set):
                    closest_char = english_char
                    closest_distance = distance
            mapping[cipher_char] = closest_char
            letter_set.remove(closest_char)

        cracked =  "".join([mapping.get(char, '*') for char in self.ciphertext])
        curr_soln_fa = FrequencyAnalysis(cracked)
        self.set_bigram_frequencies()

        

        mapping = {char: char for char in self.ciphertext}
        cracked =  "".join([mapping.get(char, '*') for char in self.ciphertext])
        curr_soln_fa = FrequencyAnalysis(cracked)

        bigrams = {bigram: self.ciphertext_bigram_frequencies[bigram] for bigram in  list(self.ciphertext_bigram_frequencies.keys())[:1]}
        bigram_keys = list(bigrams.keys())
        english_bigram_keys = list(FrequencyAnalysis.bigram_frequencies.keys())
        for i in range(len(bigrams)):
            new_mapping = dict(mapping)
            cipher_bigram = bigram_keys[i]
            english_bigram = english_bigram_keys[i]
            #Swap values with values bigrams indicate
            prev_val_0 = new_mapping[cipher_bigram[0]]
            new_val_0 = english_bigram[0]
            prev_val_1 = new_mapping[cipher_bigram[1]]
            new_val_1 = english_bigram[1]

            for cipherchar, plainchar in new_mapping.items():
                if plainchar == new_val_0:
                    new_mapping[cipherchar] = prev_val_0
                    continue
                if plainchar == new_val_1:
                    new_mapping[cipherchar] = prev_val_1
                    continue
            new_mapping[cipher_bigram[0]] = new_val_0
            new_mapping[cipher_bigram[1]] = new_val_1
            new_cracked = "".join([new_mapping.get(char, '*') for char in self.ciphertext])
            new_soln_fa = FrequencyAnalysis(new_cracked)
            if(new_soln_fa.english_correlation() > curr_soln_fa.english_correlation()):
                # print("CHANGED!!!!!")
                curr_soln_fa = new_soln_fa
                mapping = new_mapping
           



        # mapping = {char: char for char in self.ciphertext}
        # cracked =  "".join([mapping.get(char, '*') for char in self.ciphertext])
        # curr_soln_fa = FrequencyAnalysis(cracked)
        unigram_corr_range = 0.0007
        bigram_corr_range = 0.0007
        while(curr_soln_fa.english_correlation_distance() > unigram_corr_range or curr_soln_fa.bigram_correlation_distance() > bigram_corr_range):
            
            new_mapping = dict(mapping)
            random_index_to_change = randint(0, len(new_mapping.keys()) - 1)
            random_cipherval_to_change = list(new_mapping.keys())[random_index_to_change]


            prev_val = new_mapping[random_cipherval_to_change]
            new_val = elf[randint(0, len(elf) - 1)]
            
            #can delete vvv
            subs = ''

            for cipherchar, plainchar in new_mapping.items():
                if plainchar == new_val:
                    new_mapping[cipherchar] = prev_val
                    subs = cipherchar
                    continue
            new_mapping[random_cipherval_to_change] = new_val
            new_cracked = "".join([new_mapping.get(char, '*') for char in self.ciphertext])
            new_soln_fa = FrequencyAnalysis(new_cracked)
            better_unigram_corr = new_soln_fa.english_correlation_distance() < curr_soln_fa.english_correlation_distance()
            better_bigram_corr = new_soln_fa.bigram_correlation_distance() < curr_soln_fa.bigram_correlation_distance()

            if ( (better_unigram_corr or (new_soln_fa.english_correlation_distance() < unigram_corr_range )) and (better_bigram_corr or (new_soln_fa.bigram_correlation_distance() < bigram_corr_range))):
                print(f"---\nswp\nOLD: {subs}: {new_val} and {random_cipherval_to_change}: {prev_val}\nNEW: {subs}: {prev_val} and {random_cipherval_to_change}: {new_val}\n---")
                print(f"Unigram Correlation: {new_soln_fa.english_correlation()}")
                print(f"Unigram Correlation Distance: {new_soln_fa.english_correlation_distance()}")
                print(f"Bigram Correlation: {new_soln_fa.english_bigram_correlation()}")
                print(f"Bigram Correlation Distance: {new_soln_fa.bigram_correlation_distance()}")
                # print(f"Current Mapping: {new_mapping}")
                curr_soln_fa = new_soln_fa
                mapping = new_mapping
            


        # print({char: FrequencyAnalysis.english_letter_frequencies[char] for char in FrequencyAnalysis.letters_ordered_by_frequency()})
        # print(lf)
        # print(mapping)
        # print(self.ciphertext_bigram_frequencies)
        # print(curr_soln_fa.english_correlation())
        # print(self.letter_frequencies())
        return mapping, curr_soln_fa.ciphertext





    