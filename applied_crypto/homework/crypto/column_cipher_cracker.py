from crypto.analysis_decorator import *
from crypto.functions import permutations
import math
import random

class ColumnCipherCracker(AnalysisDecorator):


    def get_possible_text_list_bf(self, numcols):
        
        perms = permutations(list(range(numcols)))
        possibilities = []
        for perm in perms:
            possibility = self.decode_for_key(perm)
            possibilities.append((possibility, perm))
        return possibilities

    def shuffle_list_except_for_indices(self, arr, indices):
        arrcopy = list(arr)
        indices.sort()
        saved_portion = []
        for index in indices:
            saved_portion.append(arr[index])
            arrcopy[index] = None
        arrcopy = [el for el in arrcopy if el is not None]
        random.shuffle(arrcopy)
        ret_arr = []
        for i in range(len(arr)):
            if i in indices:
                ret_arr.append(saved_portion.pop(0))
            else:
                ret_arr.append(arrcopy.pop(0))
        return ret_arr


    # KEYLOCS = key index: value (aka cipherlocation: plaintextlocation)
    def get_best_text(self, numcols, keylocs = None, maxiters = 10000 ):
        key = list(range(numcols))
        indices_to_keep = set()
        if keylocs is not None:
            for index, value in keylocs.items():
                indices_to_keep.add(index)
                value_loc = key.index(value)
                key[index], key[value_loc] = key[value_loc], key[index]
            key = self.shuffle_list_except_for_indices(key, list(keylocs.keys()))
        else:
            random.shuffle(key)
        plain = self.decode_for_key(key)
        metric = self.analyze_possibility(plain)
        randomize_tripwire = numcols ** 3
        unchanged_count = 0
        tot_count = 0
        while metric > 0.00002:
            print(f"XX{tot_count}, breaks at {maxiters}, probably overkill", end="\r")
            if unchanged_count >= numcols ** 3:
                if keylocs is None:
                    random.shuffle(key)
                else:
                    key = self.shuffle_list_except_for_indices(key, list(keylocs.keys()))
            swap1 = random.randint(0, len(key) - 1)
            swap2 = random.randint(0, len(key) - 1)
            if keylocs is not None:
                while swap1 in indices_to_keep or swap2 in indices_to_keep or swap1 == swap2:
                    if swap1 == swap2:
                        swap2 = random.randint(0, len(key) - 1)
                    if swap1 in indices_to_keep:
                        swap1 = random.randint(0, len(key) - 1)
                    if swap2 in indices_to_keep:
                        swap2 = random.randint(0, len(key) - 1)
            else: 
                while swap1 == swap2:
                    swap2 = random.randint(0, len(key) - 1)
            keytest = list(key)
            keytest[swap1], keytest[swap2] = keytest[swap2], keytest[swap1]
            plaintest = self.decode_for_key(keytest)
            metrictest = self.analyze_possibility(plaintest)
            if metrictest < metric:
                metric = metrictest
                key = keytest
                plain = plaintest
            else:
                unchanged_count += 1
            tot_count += 1
            if(tot_count > maxiters and unchanged_count >= min(randomize_tripwire - 1, (9 * randomize_tripwire / 10))):
                break
        return {"key": key, "msg": plain, "bigram_divergence": metric}
        
    def numrows(self, numcols):
        return math.ceil(len(self.ciphertext) / numcols)

    def num_cols_filled(self, numcols):
        return len(self.ciphertext) % numcols  

    def decode_for_key(self, key):
        numcols = len(key)
        numrows = self.numrows(numcols)
        num_cols_filled = self.num_cols_filled(numcols)
        if num_cols_filled == 0: 
            num_cols_filled = numcols
        cols = [[] for _ in range(numcols)]
        starting_loc_offset = 0
        for final_order, orig_colnum in enumerate(key):
            starting_loc = final_order * numrows
            colcount = numrows
            start = starting_loc - starting_loc_offset
            if orig_colnum >= num_cols_filled:
                starting_loc_offset += 1
                colcount -= 1
            cols[orig_colnum] = self.ciphertext[start:start + colcount]
        possibility = ""
        for rownum in range(len(cols[0])):
            for col in cols:
                if rownum < len(col):
                    possibility += col[rownum]
        return possibility

    

    def analyze_possibilities(self, numcols):
        textlist = self.get_possible_text_list_bf(numcols)
        fas_perms = [(self.new_analyzer(txt_perm[0]), txt_perm[1]) for txt_perm in textlist]
        correlations = [[fa_perm[0], fa_perm[0].bigram_correlation_distance(), fa_perm[1]] for fa_perm in fas_perms]
        min_corr = float('inf')
        data = None
        for correlation in correlations:
            if correlation[1] < min_corr:
                min_corr = correlation[1]
                data = correlation
        return data

    def analyze_possibility(self, possibility):
        return self.new_analyzer(possibility).bigram_correlation_distance()

    def find_column_count_bf(self, colrange):
        correlations = []
        for numcols in colrange:
            correlations.append(self.analyze_possibilities(numcols))
        data = self.find_min_correlation(correlations)
        return data

           

    def crack(self, colrange=range(2,15)):
        data = []
        for numcols in colrange:
            data.append(self.get_best_text(numcols))
        best = {"key": None, "msg": '', "bigram_divergence": float('inf')}
        for point in data:
            if point["bigram_divergence"] < best["bigram_divergence"]:
                best = dict(point)
        return best

    def find_min_correlation(self, correlations):
        min_corr = float('inf')
        data = None
        for correlation in correlations:
            if correlation[1] < min_corr:
                min_corr = correlation[1]
                data = correlation
        return data