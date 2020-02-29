

def gen_mult_group(num):
    return set(range(1,num))

def gen_subsets(s, mod=None):
    if mod is None: mod = len(s) + 1
    subsets = []
    for num in s:
        cset = {num}
        cnum = (num * num) % mod
        while cnum != num:
            cset.add(cnum)
            cnum = (cnum * num) % mod
        subsets.append(cset)
        print(f"---\nNum: {num}\nSet: {cset}\n-----")
    return subsets 

s = gen_mult_group(31)
ss = gen_subsets(s)
print(ss)
print([len(ms) for ms in ss])