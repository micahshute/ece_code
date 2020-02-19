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
    def letters_ordered_by_frequency(cls):
        return [ char for (char, freq) in sorted(cls.english_letter_frequencies.items(), key=lambda item: item[1], reverse=True) ]

    @classmethod
    def encrypt_cc(cls, key, msg):
        return "".join([chr(65 + (ord(c) - 65 + key) % 26) for c in msg.upper() if ord(c) >= 65 and ord(c) <= 90])

    @classmethod
    def decrypt_cc(cls, key, msg):
        return cls.encrypt_cc(26 - key, msg)

    @classmethod
    def bf_decrypt_cc(cls, msg):
        return [ (key, cls.decrypt_cc(key, msg)) for key in range(26) ]

    @classmethod
    def encrypt_vc(cls, key, msg):
        return "".join([cls.encrypt_cc(key[i % len(key)], char) for i, char in enumerate(msg)])

    @classmethod
    def decrypt_vc(cls, key, msg):
        return cls.encrypt_vc([ 26 - k for k in key], msg)

    def __init__(self, phrase, keylen=0):
        regex = re.compile('[^a-zA-Z]')
        self.ciphertext = regex.sub('', phrase).upper()
        self.keylen = keylen
        self.letter_histogram = self.create_character_histogram()
        self.total_chars = sum(self.letter_histogram.values())
        self.ciphertext_bigram_frequencies = {}


    def cc_freq_analysis_naive(self):
        ordered_letter_frequencies = self.letter_frequencies()
        most_common_letter = list(ordered_letter_frequencies.keys())[0]
        likely_key = (ord(most_common_letter) - ord('E')) % 26
        # print('---------------------------------------------------------------------------------')
        # print(f"The most common letter is {most_common_letter} with a frequency of {ordered_letter_frequencies[most_common_letter]}")
        # print(f"This should correspond to E with a frequncy of {FrequencyAnalysis.english_letter_frequencies['E']}")
        confidence_level = 0
        for i, char in enumerate(FrequencyAnalysis.letters_ordered_by_frequency()):
            expected_char = chr(65 + (ord(char) - 65 + likely_key) % 26) 
            if i < len(ordered_letter_frequencies.keys()) and expected_char == list(ordered_letter_frequencies.keys())[i]:
                confidence_level += FrequencyAnalysis.english_letter_frequencies[char]
        # print(f"The confidence level of this key is {confidence_level}")
        return likely_key, confidence_level

    def vc_freq_analysis_naive(self):
        columns = self.columnize()
        return { col: FrequencyAnalysis("".join(chars)).cc_freq_analysis_naive() for col, chars in columns.items()}

    def english_correlation(self):
        lf = self.letter_frequencies()
        corr = 0
        for letter, freq in lf.items():
            corr += (freq * FrequencyAnalysis.english_letter_frequencies[letter])
        # corr should be about 0.065
        # print(corr)
        return corr

    def frequency_autocorrelation(self):
        lf = self.letter_frequencies()
        corr = 0
        for _, freq in lf.items():
            corr += (freq ** 2)
        return corr

    def max_correlation(self):
        max_corr = float('-inf')
        max_key = None
        for key in range(26):
            txt = self.decrypt_with_cc(key)
            corr = FrequencyAnalysis(txt).english_correlation()
            if(corr > max_corr):
                max_corr = corr
                max_key = key
        return max_key, max_corr

    def vc_freq_analysis_correlation(self):
        columns = self.columnize()
        return { col: FrequencyAnalysis("".join(chars)).max_correlation()[0] for col, chars in columns.items()}

    def find_keylen(self, maxlen=20):
        iocs = {}
        for keylen in range(1, maxlen + 1):
            columns = self.columnize(keylen)
            col_iocs = [ FrequencyAnalysis("".join(chars)).index_of_coincidence() for col_no, chars in columns.items() ]
            avg_col_ioc = sum(col_iocs) / len(col_iocs)
            iocs[keylen] = avg_col_ioc
        minval = float('inf')
        minkey = None
        for keylen, ioc in iocs.items(): 
            abs_diff = abs(ioc - FrequencyAnalysis.english_ioc)
            if abs_diff < minval: 
                # Account for the fact that multiples of the actual keylen also has a good ioc score
                if(minkey and abs(abs_diff - minval) < 0.1 and keylen % minkey == 0 and abs_diff < 0.1): break
                minval = abs_diff
                minkey = keylen
        # print(f"IOCs: {iocs}")
        # print(f"Min IOC is {iocs[minkey]} with a keylen {minkey}")
        return minkey


    def columnize(self, keylen=0):
        if not keylen: keylen = self.keylen 
        columns = {i: [] for i in range(keylen)}
        for i, char in enumerate(self.ciphertext):
            columns[i % keylen].append(char)
        return columns


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


    def decrypt_with_cc(self, key):
        return FrequencyAnalysis.decrypt_cc(key, self.ciphertext)

    def decrypt_with_vc(self, key):
        return FrequencyAnalysis.decrypt_vc(key, self.ciphertext)

    def bf_cc(self):
        key, _ = self.max_correlation()
        return key, self.decrypt_with_cc(key)

    def crack_vigenere(self):
        self.keylen = self.find_keylen()
        key = self.vc_freq_analysis_correlation()
        return key, self.decrypt_with_vc(key.values())


    def is_cc(self):
        corr = self.english_correlation() 
        return corr >= 0.063 and corr <= 0.068

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

        # letter_set = set(elf)
        # for cipher_char, cipher_freq in lf.items():
        #     closest_char = None
        #     closest_distance = float('inf')
        #     for english_char, english_freq in FrequencyAnalysis.english_letter_frequencies.items():
        #         distance = abs(cipher_freq - english_freq)
        #         if( distance < closest_distance and english_char in letter_set):
        #             closest_char = english_char
        #             closest_distance = distance
        #     mapping[cipher_char] = closest_char
        #     letter_set.remove(closest_char)

        # cracked =  "".join([mapping.get(char, '*') for char in self.ciphertext])
        # curr_soln_fa = FrequencyAnalysis(cracked)
        # self.set_bigram_frequencies()

        

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
                print("CHANGED!!!!!")
                curr_soln_fa = new_soln_fa
                mapping = new_mapping
           



        # mapping = {char: char for char in self.ciphertext}
        # cracked =  "".join([mapping.get(char, '*') for char in self.ciphertext])
        # curr_soln_fa = FrequencyAnalysis(cracked)
        while(abs(curr_soln_fa.english_correlation() - 0.065) > 0.0002 ):
            new_mapping = dict(mapping)
            random_index_to_change = randint(0, len(new_mapping.keys()) - 1)
            random_cipherval_to_change = list(new_mapping.keys())[random_index_to_change]


            prev_val = new_mapping[random_cipherval_to_change]
            new_val = elf[randint(0, len(elf) - 1)]


            for cipherchar, plainchar in new_mapping.items():
                if plainchar == new_val:
                    new_mapping[cipherchar] = prev_val
                    continue
            new_mapping[random_cipherval_to_change] = new_val
            new_cracked = "".join([new_mapping.get(char, '*') for char in self.ciphertext])
            new_soln_fa = FrequencyAnalysis(new_cracked)
            if(new_soln_fa.english_correlation() > curr_soln_fa.english_correlation()):
                curr_soln_fa = new_soln_fa
                mapping = new_mapping


        # print({char: FrequencyAnalysis.english_letter_frequencies[char] for char in FrequencyAnalysis.letters_ordered_by_frequency()})
        # print(lf)
        # print(mapping)
        # print(self.ciphertext_bigram_frequencies)
        # print(curr_soln_fa.english_correlation())
        # print(self.letter_frequencies())
        return mapping, curr_soln_fa.ciphertext





    