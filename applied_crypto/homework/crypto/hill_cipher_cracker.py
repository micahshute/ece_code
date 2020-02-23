from crypto.analysis_decorator import *
import numpy as np
import random


class Hill2x2CipherCracker(AnalysisDecorator):

    def __init__(self, fa):
        super().__init__(fa)
        self.bigram_frequencies = self.calc_bigram_frequencies()


    def calc_bigram_frequencies(self):
        bigrams = {}
        chars = [char for char in self.analyzer.ciphertext]
        bigrams[f"{chars[0]}{chars[1]}"] = 1
        for i in range(1, len(chars), 2):
            bigram = f"{chars[i-1]}{chars[i]}"
            if bigram in bigrams:
                bigrams[bigram] += 1
            else:
                bigrams[bigram] = 1
        total_bigrams = sum(bigrams.values())
        return { bigram: (count / total_bigrams) for (bigram, count) in sorted(bigrams.items(), key=lambda item: item[1], reverse=True) }

    def ciphertext2numlist(self, txt=None):
        if txt is None: 
            txt = self.analyzer.ciphertext
        return [(ord(char) - 65) for char in txt]

    def numlist2ciphertext(self, lst=None):
        if lst is None:
            lst = self.ciphertext2numlist()
        return "".join([chr(num + 65) for num in lst])

    def group_list(self, lst, group_size):
        for i in range(0, len(lst), group_size):
            yield lst[i: i + group_size]

    def decrypt(self, key):
        invkey = self.calculate_inv_matrix(key)
        ciphertext_letter_pairs = list(self.group_list([char for char in self.analyzer.ciphertext], 2))
        ciphertext_num_pairs = [self.ciphertext2numlist("".join(pair)) for pair in ciphertext_letter_pairs]
        for cpair in ciphertext_num_pairs:
            pair_matrix = np.matrix([[cpair[0]], [cpair[1]]])
            nested_list = ((invkey * pair_matrix) % 26).tolist()
            yield [nested_list[0][0], nested_list[1][0]]

    def decrypt2txt(self, k):
        numlist = [int(el) for pair in list(self.decrypt(k)) for el in pair]
        plaintext = self.numlist2ciphertext(numlist)
        return plaintext

    # NOTE: modInverse function from GeeksForGeeks website
    def modInverse(self, a, m): 
        a = a % m
        for x in range(1, m): 
            if ((a * x) % m == 1): 
                return x 
        return 1

    def calculate_inv_matrix(self, matrix):
        det = round(np.linalg.det(matrix))
        return (self.modInverse(det, 26) * (det  * np.linalg.inv(matrix)).round()) % 26

    def new_index_list(self):
        cipher_bigram_opts = 3
        eng_bigam_opts = 17
        cipher_opt1 = random.randint(0,cipher_bigram_opts)
        cipher_opt2 = random.randint(0,cipher_bigram_opts)
        while cipher_opt1 == cipher_opt2:
            cipher_opt2 = random.randint(0,cipher_bigram_opts)
        eng_opt1 = random.randint(0,eng_bigam_opts)
        eng_opt2 = random.randint(0,eng_bigam_opts)
        while eng_opt1 == eng_opt2:
            eng_opt2 = random.randint(0,eng_bigam_opts)
        return [cipher_opt1, cipher_opt2, eng_opt1, eng_opt2]

    def crack(self):
        bfs = self.bigram_frequencies
        bf_chars = list(bfs.keys())
        
        ebfs = type(self.analyzer).bigram_frequencies
        ebf_chars = list(ebfs.keys())
        # index_list = [1,2,0,3]
        index_list = [0,1,0,1]
        
        best_english_correlation = float('inf')
        best_key = None
        best_txt = ''
        maxiters = 5000
        count = 0
        while best_english_correlation > 0.0007:
            print(f"X{count}, breaks at {maxiters}", end="\r")
            cpair1, cpair2, epair1, epair2 = index_list
            bfs_to_analyze = { bf_chars[cpair1]: bfs[bf_chars[cpair1]], bf_chars[cpair2]: bfs[bf_chars[cpair2]] }
            
            
            ebfs_to_analyze = { ebf_chars[epair1]: ebfs[ebf_chars[epair1]], ebf_chars[epair2]: ebfs[ebf_chars[epair2]] }
            bf_nums = [self.ciphertext2numlist(chars) for chars in bfs_to_analyze.keys()]
            ebf_nums = [self.ciphertext2numlist(chars) for chars in ebfs_to_analyze.keys()]

            cipher_matrix = np.transpose(np.matrix(bf_nums))
            english_matrix = np.transpose(np.matrix(ebf_nums))

            # K * english_matrix = cipher_matrix
            # K = cipher_matrix * (english_matrix) ^ -1
            try:
                inv_english_matrix = self.calculate_inv_matrix(english_matrix)
            except np.linalg.LinAlgError:
                index_list = self.new_index_list()
                continue
            k = (cipher_matrix * inv_english_matrix) % 26
        
            try:
                txt = self.decrypt2txt(k)
            except np.linalg.LinAlgError:
                index_list = self.new_index_list()
                continue
            fatxt = self.new_analyzer(txt)
            eng_corr_dist = fatxt.english_correlation_distance()
            if eng_corr_dist < best_english_correlation:
                best_english_correlation = eng_corr_dist
                best_key = k
                best_txt = txt
            count += 1
            index_list = self.new_index_list()
            # print(f"Index List: {index_list}")
            # print(f"Best Corr Dist: {best_english_correlation}")
            if count >= maxiters: break
        return best_key, best_txt


