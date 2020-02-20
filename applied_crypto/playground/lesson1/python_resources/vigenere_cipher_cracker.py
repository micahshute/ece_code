from python_resources.decorator import * 



class VigenereCipherCracker(AnalysisDecorator):


    @classmethod
    def encrypt_cc(cls, key, msg):
        return "".join([chr(65 + (ord(c) - 65 + key) % 26) for c in msg.upper() if ord(c) >= 65 and ord(c) <= 90])


    @classmethod
    def bf_decrypt_cc(cls, msg):
        return [ (key, cls.decrypt_cc(key, msg)) for key in range(26) ]

    @classmethod
    def encrypt_vc(cls, key, msg):
        return "".join([cls.encrypt_cc(key[i % len(key)], char) for i, char in enumerate(msg)])

    @classmethod
    def decrypt_cc(cls, key, msg):
        return cls.encrypt_cc(26 - key, msg)

    @classmethod
    def decrypt_vc(cls, key, msg):
        return cls.encrypt_vc([ 26 - k for k in key], msg)


    def decrypt_with_cc(self, key):
        return VigenereCipherCracker.decrypt_cc(key, self.ciphertext)

    def max_correlation(self):
        max_corr = float('-inf')
        max_key = None
        for key in range(26):
            txt = self.decrypt_with_cc(key)
            corr = self.new_analyzer(txt).english_correlation()
            if(corr > max_corr):
                max_corr = corr
                max_key = key
        return max_key, max_corr

    def columnize(self, keylen=0):
        if not keylen: keylen = self.keylen 
        columns = {i: [] for i in range(keylen)}
        for i, char in enumerate(self.ciphertext):
            columns[i % keylen].append(char)
        return columns

    def freq_analysis_correlation(self):
        columns = self.columnize()
        return { col: VigenereCipherCracker(self.new_analyzer("".join(chars))).max_correlation()[0] for col, chars in columns.items()}


    def find_keylen(self, maxlen=20):
        iocs = {}
        for keylen in range(1, maxlen + 1):
            columns = self.columnize(keylen)
            col_iocs = [ self.new_analyzer("".join(chars)).index_of_coincidence() for col_no, chars in columns.items() ]
            avg_col_ioc = sum(col_iocs) / len(col_iocs)
            iocs[keylen] = avg_col_ioc
        minval = float('inf')
        minkey = None
        for keylen, ioc in iocs.items(): 
            abs_diff = abs(ioc - type(self.analyzer).english_ioc)
            if abs_diff < minval: 
                # Account for the fact that multiples of the actual keylen also has a good ioc score
                if(minkey and abs(abs_diff - minval) < 0.1 and keylen % minkey == 0 and minkey != 0 and abs_diff < 0.1): break
                minval = abs_diff
                minkey = keylen
        # print(f"IOCs: {iocs}")
        print(f"Min IOC is {iocs[minkey]} with a keylen {minkey}")
        return minkey

    def decrypt(self, key):
        return VigenereCipherCracker.decrypt_vc(key, self.ciphertext)

    def crack(self):
        self.keylen = self.find_keylen()
        key = self.freq_analysis_correlation()
        return key, self.decrypt(key.values())

    def bf_cc(self):
        key, _ = self.max_correlation()
        return key, self.decrypt_with_cc(key)

    def is_cc(self):
        corr = self.analyzer.english_correlation() 
        return corr >= 0.063 and corr <= 0.068