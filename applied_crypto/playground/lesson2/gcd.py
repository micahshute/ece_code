from python_resources.functions import gcd

class GCDMetric:

    def __init__(self):
        self.count = 0

    def lgcd(self,a,b):
        self.count += 1
        if b == 0:
            return a
        else: 
            return self.lgcd(b, a % b)


m = GCDMetric()
print(m.lgcd(56, 42))
print(m.count)
print('----')
m.count = 0
print(m.lgcd(8, 13))
print(m.count)
print('----')
m.count = 0
print(m.lgcd(1071, 462))
print(m.count)
print('----')
m.count = 0
print(m.lgcd(4880197746793002076754294951020699004973287771475874, 3016128079338728432528443992613633888712980904400501))
print(m.count)
print('----')
m.count = 0
print(m.lgcd(761238467827682763587623876572628198230562381084701293847, 18927309587912873948712983578932651298347190283749382))
print(m.count)
print('----')
m.count = 0