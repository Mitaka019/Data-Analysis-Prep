
# 4.5 Linear Algebra

import numpy as np

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])

print(x)
print(y)

print(x.dot(y))

# x.dot(y) is equivalent to np.dot(x, y):

print(np.dot(x, y))

# A matrix product between a two-dimensional array and a suitably sized onedimensional array results in a one-dimensional array:

print(np.dot(x, np.ones(3)))

# The @ symbol (as of Python 3.5) also works as an infix operator that performs matrix
# multiplication:

print(x @ np.ones(3))

from numpy.linalg import inv, qr

X = np.random.randn(5, 5)
mat = X.T.dot(X)

print(inv(mat))

print(mat.dot(inv(mat)))

q, r = qr(mat)
print(r)

# ===============================
# 🔹 Linear Algebra Functions (numpy.linalg)
# ===============================

# diag        -> Return diagonal (or off-diagonal) elements of a square matrix as 1D array,
#                or convert a 1D array into a square matrix with zeros on off-diagonal

# dot         -> Matrix multiplication

# trace       -> Sum of the diagonal elements

# det         -> Matrix determinant

# eig         -> Eigenvalues and eigenvectors of a square matrix

# inv         -> Inverse of a square matrix

# pinv        -> Moore-Penrose pseudo-inverse of a matrix

# qr          -> QR decomposition

# svd         -> Singular Value Decomposition (SVD)

# solve       -> Solve linear system Ax = b for x (A must be square)

# lstsq       -> Least-squares solution to Ax = b

