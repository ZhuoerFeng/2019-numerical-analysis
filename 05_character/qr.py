import numpy as np  
a = np.array([ [1, 1, 1], [2, -1, -1], [2, -4, 5]])
q, r = np.linalg.qr(a)
print(a)
print(q)
print(r)

b = np.array([[-1, -2, -2], [-2, 2, -1], [-2, -1, 2]])
print(b)
test = np.dot(b, a)
print(test)