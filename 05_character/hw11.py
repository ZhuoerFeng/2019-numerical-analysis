import numpy as np 
a = np.array([[4, 0, 0], [4, 5, 5], [2, 5, 5]])
q, r = np.linalg.qr(a)
print(q)
print(r)