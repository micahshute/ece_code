from crypto.analysis_decorator import *
import random
import math
import code


class PlayfairCipherCracker(AnalysisDecorator):

    def random_key(self):
        alph = [char for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ"]
        random.shuffle(alph)
        return self.construct_key("".join(alph))

    def construct_key(self, keyphrase):
        alph = [char for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ"]
        seen_letters = set()
        klst = [char for char in self.new_analyzer(keyphrase).ciphertext]
        fbf = [[[],[],[],[],[]] for _ in range(5) ]
        adds = 0
        ltrsource = klst
        while adds < 25:
            col = adds % 5
            row = math.floor(adds / 5)
            ltr = ltrsource.pop(0)
            if ltr not in seen_letters:
                fbf[row][col] = ltr
                seen_letters.add(ltr)
                adds += 1
            if ltrsource == klst and len(klst) <= 0:
                ltrsource = alph
        return fbf


    def key2hash(self, key):
        keyhash = {}
        for row in range(len(key)):
            for col in range(len(key[row])):
                keyhash[key[row][col]] = (row, col)
        return keyhash

    def recover_doubles(self, l1, l2):
        if l2 == "X":
            l2 = l1
        return l1, l2

    def cipher_line(self, rc1, rc2, rc, deciphering=False):
        l1 = rc[(rc1 + 1) % 5]
        l2 = rc[(rc2 + 1) % 5]
        if deciphering:
            l1, l2 = self.recover_doubles(l1, l2)
        return f"{l1}{l2}"


    def cipher_box(self, r1, c1, r2, c2, k, deciphering=False):
        l1 = k[r1][c2]
        l2 = k[r2][c1]
        if deciphering: 
            l1, l2 = self.recover_doubles(l1, l2)
        return f"{l1}{l2}"

    def cipher_pair(self, key, kh, wordpair):
        if wordpair[0] == wordpair[1]:
            wordpair = f"{wordpair[0]}X"
        row1, col1 = kh[wordpair[0]]
        row2, col2 = kh[wordpair[1]]
        if row1 == row2:
            return self.cipher_line(col1, col2, key[row1])
        elif col1 == col2:
            return self.cipher_line(row1, row2, [row[col1] for row in key])
        else:
            return self.cipher_box(row1, col1, row2, col2, key)

    def cipher(self, key, phrase):
        kh = self.key2hash(key)
        res = ""
        for i in range(1, len(phrase), 2):
            res += self.cipher_pair(key, kh, f"{phrase[i-1]}{phrase[i]}")
        return res

    def decipher_pair(self, key, kh, wordpair):
        row1, col1 = kh[wordpair[0]]
        row2, col2 = kh[wordpair[1]]
        if row1 == row2:
            return self.cipher_line(col1 - 2, col2 - 2, key[row1], True)
        elif col1 == col2:
            return self.cipher_line(row1 - 2, row2 - 2, [row[col1] for row in key], True)
        else:
            return self.cipher_box(row1, col1, row2, col2, key, True)

    def decipher(self, key, phrase):
        kh = self.key2hash(key)
        res = ""
        for i in range(1, len(phrase), 2):
            res += self.decipher_pair(key, kh, f"{phrase[i-1]}{phrase[i]}")
        return res

    def random_swap(self, k):
        decision = random.randint(0,9)
        if decision == 7:
            return self.random_row_swap(k)
        else:
            return self.random_key_swap(k)

    def random_key_swap_for_row_col(self, r1, c1, key):
        k = self.copy_key(key)
        r2,c2 = [random.randint(0,4) for _ in range(2)]
        k[r1][c1], k[r2][c2] = k[r2][c2], k[r1][c1]
        print(f"{k[r1][c1]}, {k[r2][c2]}")
        return k

    def random_key_swap(self, key):
        k = self.copy_key(key)
        r1,c1,r2,c2 = [random.randint(0,4) for _ in range(4)]
        k[r1][c1], k[r2][c2] = k[r2][c2], k[r1][c1]
        return k

    def transpose_key(self, key):
        copykey = self.copy_key(key)
        k = []
        for col in range(5):
            k.append([row[col] for row in copykey])
        return k

    def copy_key(self, key):
        return [list(row) for row in key]

    def random_row_swap(self, key):
        k = self.copy_key(key)
        r1 = random.randint(0,4)
        r2 = random.randint(0,4)
        while r1 == r2:
            r2 = random.randint(0,4)
        k[r1], k[r2] = k[r2], k[r1]
        return k

    def fitness_score(self, txtfa):
        uls = txtfa.unigram_log_score()
        dls = txtfa.bigram_log_score()
        tls = txtfa.trigram_log_score()
        return abs(uls + dls + tls)

    def good_key_swap(self, k):
        decision = random.randint(0,100)
        if decision < 5:
            return self.random_key_swap(k)
        return self.swap_within_row(k)

    def swap_within_row(self, key):
        k = self.copy_key(key)
        r,c1,c2 = [random.randint(0,4) for _ in range(3)]
        while c1 == c2:
            c2 = random.randint(0,4)
        k[r][c1], k[r][c2] = k[r][c2], k[r][c1]
        return k

    def crack_close_key(self, key):
        ckey = self.copy_key(key)
        cmsg = self.new_analyzer(self.decipher(ckey, self.ciphertext))

        bkey = ckey
        bmsg = self.new_analyzer(cmsg.ciphertext)
        count = 0
        no_change_count = 0
        maxiters = 100000
        reset_iters = 1000
        while True:
            if no_change_count >= reset_iters:
                tkey = self.copy_key(ckey)
                for _ in range(random.randint(5,10)):
                    tkey = self.random_row_swap(tkey)
                for _ in range(random.randint(100,200)):
                    tkey = self.swap_within_row(tkey)
                tmsg = self.new_analyzer(self.decipher(tkey, self.ciphertext))
            else:
                tkey = self.good_key_swap(ckey)
                tmsg = self.new_analyzer(self.decipher(tkey, self.ciphertext))

            if self.fitness_score(tmsg) < self.fitness_score(cmsg) or no_change_count >= reset_iters:
                ckey = tkey
                cmsg = tmsg
                no_change_count = 0

                if self.fitness_score(cmsg) < self.fitness_score(bmsg):
                    bkey = ckey
                    bmsg = cmsg
                # print('--------- KEY REFINEMENT PROCESS ---------')
                # print(f"Best Key: {bkey}")
                # print(f"Best Key Score: {self.fitness_score(bmsg)}")
                # print(f"Local Key: {ckey}")
                # print(f"Local Key Score: {self.fitness_score(cmsg)}")
                # print('----------')
            else:
                no_change_count += 1

            print(f"X {count}/{maxiters} iterations", end="\r")
            if count >= maxiters:
                break
            
            count += 1
        return bkey, bmsg



    def crack(self):
        ckey = self.random_key()   
        bkey = self.copy_key(ckey)

        cmsg = self.new_analyzer(self.decipher(self.copy_key(ckey), self.analyzer.ciphertext))
        ctrilog = cmsg.trigram_log_score()
        best_msg = cmsg

        max_iters = 200000
        reset_iters = 1000
        consecutive_no_change = 0
        count = 1

        while abs(ctrilog) > 2325:

            if(consecutive_no_change >= reset_iters):
                test_key = self.random_key()
                test_key = self.random_row_swap(self.transpose_key(ckey))
            else:
                test_key = self.random_key_swap(ckey)

            test_msg = self.new_analyzer(self.decipher(self.copy_key(test_key), self.analyzer.ciphertext))
            print(f"X {count}/{max_iters} iterations", end="\r")
 
            if self.fitness_score(test_msg) < self.fitness_score(cmsg) or consecutive_no_change >= reset_iters:
                ckey = self.copy_key(test_key)
                cmsg = self.new_analyzer(test_msg.ciphertext)
                ctrilog = cmsg.trigram_log_score()
                consecutive_no_change = 0

                if self.fitness_score(cmsg) < self.fitness_score(best_msg):
                    bkey = list(ckey)
                    best_msg = self.new_analyzer(cmsg.ciphertext)

                # print('-------Key Aquisition Process-------')
                # print(f"Looking for a key with a score < 5165")
                # print(f"Best overall key:{bkey}")
                # print(f"Best key score: {self.fitness_score(best_msg)}")
                # print(f"Best local key {ckey}")
                # print(f"Local Key score: {self.fitness_score(cmsg)}")
                # print('-------')
                # print('-------')
            else:
                consecutive_no_change += 1

            count += 1
            if count >= max_iters:
                break

        return self.crack_close_key(bkey)
