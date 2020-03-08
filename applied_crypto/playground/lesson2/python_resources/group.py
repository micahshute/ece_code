

class Group:

    def __init__(self, nset, binop):
        if type(nset) == list:
            nset = set(nset)
        self.values = nset
        self.binop = binop
        self.e = None
        self.check_validity()
            
    

    def check_validity(self):
        if not self.check_validity_1(): raise Exception(f"{self.values} does not have an identity element")
        if not self.check_validity_2(): raise Exception(f"{self.values} - not all elements have inverses")
        if not self.check_validity_3(): raise Exception(f"{self.values} - not all ops return another memeber of the group")
        if not self.check_validity_4(): raise Exception(f"{self.values} is not associative")
        return True

    def check_validity_1(self):
        for el_to_check in self.values:
            is_identity = True
            for el in self.values:
                if self.binop(el_to_check, el) != el:
                    is_identity = False
                    break
            if is_identity:
                self.e = el_to_check
                return True
        return False

    def check_validity_2(self):
        for el_to_check in self.values:
            inverse_found = False
            for el in self.values:
                if self.binop(el_to_check, el) == self.e:
                    inverse_found = True
                    break
            if not inverse_found:
                print(f"{el_to_check} has no inverse")
                return False
        return True

    def check_validity_3(self):
        for el_to_check in self.values:
            for el in self.values:
                if self.binop(el_to_check, el) not in self.values:
                    return False
        return True

    def check_validity_4(self):
        for el1 in self.values:
            for el2 in self.values:
                if el2 == el1: continue
                for el3 in self.values:
                    if el3 == el2 or el3 == el1: continue
                    if not (self.binop(self.binop(el1, el2), el3) == self.binop(el1, self.binop(el2, el3))):
                        return False
        return True