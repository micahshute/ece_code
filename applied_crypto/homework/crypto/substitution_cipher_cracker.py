from crypto.analysis_decorator import *
import random

class SubstitutionCipherCracker(AnalysisDecorator):

    @classmethod
    def cipher(cls, key, msg):
        return "".join([key[char] for char in msg])

    @classmethod
    def decipher(cls, key, msg):
        revkey = { v: k for k,v in key.items() }
        return cls.cipher(revkey, msg)


    def make_init_key(self):
        orderd_eng_letters = self.analyzer.letters_ordered_by_frequency()
        clf = self.analyzer.letter_frequencies()
        elf = type(self.analyzer).english_letter_frequencies
        oelf = { char: elf[char] for char in orderd_eng_letters }
        init_mapping = {}
        clfk = list(clf.keys())
        elfk = list(oelf.keys())
        for i in range(len(clf.keys())):
            init_mapping[clfk[i]] = elfk[i]
        return init_mapping

    def swap_key_char(self, key, known_set=None):
        keycpy = dict(key)
        keykeys = list(keycpy.keys())
        swap1 = random.randint(0, len(keykeys) - 1)
        swap2 = random.randint(0, len(keykeys) - 1)
        while swap1 == swap2:
            swap2 = random.randint(0, len(keykeys) - 1)

        if known_set is not None:
            while keykeys[swap1] in known_set or keykeys[swap2] in known_set:
                if keykeys[swap1] in known_set:
                    swap1 = random.randint(0, len(keykeys) - 1)
                if keykeys[swap2] in known_set:
                    swap2 = random.randint(0, len(keykeys) - 1)
                while swap1 == swap2:
                    swap2 = random.randint(0, len(keykeys) - 1)

        temp = keycpy[keykeys[swap1]]
        keycpy[keykeys[swap1]] = keycpy[keykeys[swap2]]
        keycpy[keykeys[swap2]] = temp
        return keycpy

    def swap_keys_at(self, key, keyval, val):
        keycpy = dict(key)
        oldkey = None
        for k,v in keycpy.items():
            if v == val:
                oldkey = k
                break
        tmp = keycpy[keyval]
        keycpy[keyval] = val
        keycpy[oldkey] = tmp
        return keycpy


    def crack(self, known_key=None):
        
        ikey = self.make_init_key()
        known_keys_set = None
        if known_key is not None:
            for k,v in known_key.items():
                ikey = self.swap_keys_at(ikey, k, v)
            known_keys_set = { k for k in known_key.keys() }
        ckey = dict(ikey)
        csoln = self.new_analyzer(SubstitutionCipherCracker.cipher(ckey, self.ciphertext))
        cbigram_dev = csoln.bigram_correlation_distance()
        bkey = dict(ckey)
        bsoln = csoln
        bbigram_dev = cbigram_dev
        bigram_stpt = 0.000382
        maxiters = 50000
        no_change_count = 0
        no_change_max = 1000
        count = 0
        while cbigram_dev > bigram_stpt:
            if(no_change_count > no_change_max):
                ckey = self.make_init_key()
                if known_key is not None:
                    for k,v in known_key.items():
                        ckey = self.swap_keys_at(ckey, k, v)
                 
                
            tkey = self.swap_key_char(ckey, known_keys_set)
            tsoln = self.new_analyzer(SubstitutionCipherCracker.cipher(tkey, self.ciphertext))
            tbigram_dev = tsoln.bigram_correlation_distance()
           
            if tbigram_dev < cbigram_dev or no_change_count > no_change_max:
                ckey = tkey
                csoln = tsoln
                cbigram_dev = tbigram_dev
                no_change_count = 0
                if cbigram_dev < bbigram_dev:
                    bkey = dict(ckey)
                    bsoln = csoln
                    bbigram_dev = cbigram_dev
            else:
                no_change_count += 1
            if count >= maxiters:
                break
            count += 1
        return bkey, bsoln.ciphertext
