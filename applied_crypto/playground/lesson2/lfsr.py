import code
from python_resources.lfsr import *


# class LFSR:

#     def __init__(self, state, coefficients):
#         if len(state) != len(coefficients):
#             raise AttributeError
#         self.state = state
#         self.c = coefficients

#     def generator(self):
#         while True: 
#             sum = 0
#             for i in range(len(self.state) - 1, 0, -1):
#                 sum = sum ^ (self.c[i] * self.state[i])
#             self.state.insert(0, sum)
#             yield self.state.pop()


# lfsr = LFSR([1,0,0,1,1], [0,1,1,1,1])
# g = lfsr.generator()

# out = []
# for _ in range(20):
#     out.append(next(g))
#     print(lfsr.state)
# print(out)

lfsr = LFSR([1,1,0,1,0], [1,1,1,1,1])
out = []
for _ in range(15):
    out.append(next(lfsr.stream))
    print(lfsr.state)
print(out)

# code.interact(local=dict(globals(), **locals()))