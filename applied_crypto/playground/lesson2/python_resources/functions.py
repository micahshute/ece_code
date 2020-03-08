import numpy as np
from scipy import linalg
import sympy as sp
import sage.all as sage

def gcd(a,b):
    if b == 0:
        return a
    else: 
        return gcd(b, a % b)


def inv_mod(a,b):
    r, rm1 = b, a
    s, sm1 = 0, 1
    t, tm1 = 1, 0
    while r != 0:
        q = rm1 // r
        rm1, r = r, rm1 % r
        sm1, s = s, sm1 - q * s
        tm1, t = t, tm1 - q * t
    d = sm1 * a + tm1 * b
    return d, sm1, tm1

def smod_mat(vals, mod):
    r = sage.IntegerModRing(mod)
    return sage.matrix(r, vals)

def sinv_mat(mat):
    return mat.inverse()

def matrix(vals):
    return sp.Matrix(vals)

# def inv_mod_matrix(matrix, mod):
#         det = matrix.det()
#         _, modinv, _= inv_mod(det, mod)
#         modinv = int(modinv)
#         return modinv * (det  * matrix ** -1)

def inv_mod_matrix(matrix, mod):
    return matrix.inv_mod(mod)


def linsolve(a, b):
    a = np.matrix(a)
    b = np.matrix(b)
    ainv = np.linalg.inv(a)
    return ainv * b

def euler_totient(n):
    res = n
    p = 2
    while(p ** 2 <= n):
        if(n % p == 0):
            while( n % p == 0 ):
                n = n // p 
            res -= res // p
        p += 1

    if n > 1:
        res -= res // n
    return res









def matrix_mod(mat, m):
    matrix = mat.copy()
    for row in range(np.shape(matrix)[0]):
        for col in range(np.shape(matrix)[1]):
            matrix[row, col] = int(matrix[row, col]) % m
    return matrix

def matrix_round(mat):
    matrix = mat.copy()
    for row in range(np.shape(matrix)[0]):
        for col in range(np.shape(matrix)[1]):
            matrix[row, col] = int(round(matrix[row, col]))
    return matrix

def npinv_mod_matrix(matrix, mod):
        matrix = matrix_mod(matrix, mod)
        det = int(round(np.linalg.det(matrix))) 
        _, modinv, _= inv_mod(det, mod) 
        modinv = int(modinv)
        return matrix_round((modinv * det * np.linalg.inv(matrix)))


def npmatrix(nums):
    return np.matrix(nums, dtype=np.int64)

def to_bin_arr(num, length=None):
    bnum = bin(num)[2:]
    if length is not None:
        bnum = ('0' * (length - len(bnum))) + bnum
    return [int(i) for i in bnum]