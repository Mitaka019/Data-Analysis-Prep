
# 4.4 File Input and Output with Arrays

import numpy as np

# np.save and np.load are the two workhorse functions for efficiently saving and loading array data on disk.

arr = np.arange(10)
print(np.save('some_array', arr))

print(np.load('some_array.npy'))

print(np.savez('array_archive.npz', a=arr, b=arr))

arch = np.load('array_archive.npz')
print(arch['b'])

print(np.savez_compressed('arrays_compressed.npz', a=arr, b=arr))