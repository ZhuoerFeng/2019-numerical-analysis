import numpy as np 
a = np.array([ [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]])
q, r = np.linalg.qr(a, mode='complete')
print(a)
print(q)
print(r)

G = np.array( [ [5, 15], [15, 55]])
L = np.linalg.cholesky(G)
print(G)
print(L)