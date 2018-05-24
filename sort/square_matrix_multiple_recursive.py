import numpy as np


def square_matrix_multiple(a, b):
    m = a.shape[0]
    if m == 1:
        c = a*b
    else:
        n = m // 2
        a11 = a[:n, :n]
        a12 = a[:n, n:]
        a21 = a[n:, :n]
        a22 = a[n:, n:]
        b11 = b[:n, :n]
        b12 = b[:n, n:]
        b21 = b[n:, :n]
        b22 = b[n:, n:]
        c11 = square_matrix_multiple(a11, b11) + square_matrix_multiple(a12, b21)
        c12 = square_matrix_multiple(a11, b12) + square_matrix_multiple(a12, b22)
        c21 = square_matrix_multiple(a21, b11) + square_matrix_multiple(a22, b11)
        c22 = square_matrix_multiple(a21, b12) + square_matrix_multiple(a22, b22)
        c = np.concatenate((np.concatenate((c11, c12), axis=1), np.concatenate((c21, c22), axis=1)), axis=0)
    return c


def square_matrix_multiple2(a, b):
    m = a.shape[0]
    if m == 1:
        c = a*b
    else:
        n = m // 2
        a11 = a[:n, :n]
        a12 = a[:n, n:]
        a21 = a[n:, :n]
        a22 = a[n:, n:]
        b11 = b[:n, :n]
        b12 = b[:n, n:]
        b21 = b[n:, :n]
        b22 = b[n:, n:]
        s1 = b12 - b22
        s2 = a11 + a12
        s3 = a21 + a22
        s4 = b21 - b11
        s5 = a11 + a22
        s6 = b11 + b22
        s7 = a12 - a22
        s8 = b21 + b22
        s9 = a11 - a21
        s10 = b11 - b12
        p1 = square_matrix_multiple2(a11, s1)
        p2 = square_matrix_multiple(s2, b22)
        p3 = square_matrix_multiple(s3, b11)
        p4 = square_matrix_multiple(a22, s4)
        p5 = square_matrix_multiple(s5, s6)
        p6 = square_matrix_multiple(s7, s8)
        p7 = square_matrix_multiple(s9, s10)
        c11 = p5 + p4 - p2 + p6
        c12 = p1 + p2
        c21 = p3 + p4
        c22 = p5 + p1 -p3 - p7
        c = np.concatenate((np.concatenate((c11, c12), axis=1), np.concatenate((c21, c22), axis=1)), axis=0)
    return c


a = np.array([[2, 2], [2, 3]])
b = np.array([[1, 1], [1, 2]])
# c = np.multiply(a, b)
# c = np.matmul(a, b)
c = square_matrix_multiple(a, b)
print(c)