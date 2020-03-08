import numpy as np
from python_resources.functions import *


# def nextnum(a,c,m,num):
#     return (a * num + c) % m

# a = np.matrix([[40,1], [42,1]])
# b = np.matrix([[42],[49]])

# ainv = inv_mod_matrix(a, 101)

# ans = (ainv * b) % 101

# print(ans)

# def nextnum(a,c,m,num):
#     return (a * num + c) % m

# a = matrix2([[40,1], [42,1]])
# b = matrix2([[42],[49]])

# ainv = inv_mod_matrix2(a, 101)

# ans = (ainv * b) % 101

# print(ans)

o1 = 3904654068
o2 = 897137925
o3 = 4281244274
o4 = 3573336907
m = 2 ** 32
a = matrix([[o1, 1],[o2, 1]])
b = matrix([[o2], [o3]])

ainv = inv_mod_matrix(a, m) 
ans = ainv * b % m

print(ans)



