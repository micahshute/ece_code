import numpy as np

def solve(a, b):
    a = np.matrix(a)
    b = np.matrix(b)
    ainv = np.linalg.inv(a)
    return ainv * b



# a = [[3,-2], [2, -2]]
# b = [[4],[-4]]

a = [[4, -3, 1], [2, 1, 3], [-1, 2, -5]]
b = [[-10], [0], [17]]


print(solve(a,b))