import numpy as np
import scipy

A = np.array([[1, -1, 0, 0, 0], [-1, 2, -1, 0, 0], [0, -1, 2, -1, 0], [0, 0, -1, 2, -1], [0, 0, 0, -1, 2]])
print(A)
print(np.linalg.eigh(A))
