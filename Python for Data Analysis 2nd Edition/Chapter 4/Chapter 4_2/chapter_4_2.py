
# 4.2 Universal Functions: Fast Element-Wise Array Functions

import numpy as np

# A universal function, or ufunc, is a function that performs element-wise operations
# on data in ndarrays. 

arr = np.arange(10)

print(arr)

print(np.sqrt(arr))

print(np.exp(arr))

x = np.random.randn(8)
y = np.random.randn(8)

print(x)
print(y)

print(np.maximum(x, y))

arr = np.random.randn(7) * 5
print(arr)

remainder, whole_part = np.modf(arr)

print(remainder)

print(whole_part)


print(arr)

print(np.sqrt(arr))

print(np.sqrt(arr, arr))
              
print(arr)

# ===============================
# 🔹 Unary Universal Functions (operate on one array)
# ===============================
# abs, fabs       -> Absolute value
# sqrt            -> Square root (arr ** 0.5)
# square          -> Square (arr ** 2)
# exp             -> Exponential (eˣ)
# log, log10,
# log2, log1p     -> Natural log, base 10, base 2, log(1+x)
# sign            -> Sign of element (1, 0, –1)
# ceil            -> Round up
# floor           -> Round down
# rint            -> Round to nearest integer
# modf            -> Fractional & integral parts
# isnan           -> Check for NaN
# isfinite, isinf -> Check finite / infinite
# cos, cosh,
# sin, sinh,
# tan, tanh       -> Trigonometric & hyperbolic
# arccos, arccosh,
# arcsin, arcsinh,
# arctan, arctanh -> Inverse trigonometric functions
# logical_not     -> Element-wise NOT (~arr)

# ===============================
# 🔹 Binary Universal Functions (operate on two arrays)
# ===============================
# add             -> Addition
# subtract        -> Subtraction
# multiply        -> Multiplication
# divide,
# floor_divide    -> Division / floor division
# power           -> Exponentiation
# maximum, fmax   -> Element-wise max (fmax ignores NaN)
# minimum, fmin   -> Element-wise min (fmin ignores NaN)
# mod             -> Modulus (remainder)
# copysign        -> Copy sign from one array to another
# greater,
# greater_equal,
# less,
# less_equal,
# equal,
# not_equal       -> Comparisons (>, >=, <, <=, ==, !=)
# logical_and,
# logical_or,
# logical_xor     -> Element-wise logical ops (&, |, ^)
