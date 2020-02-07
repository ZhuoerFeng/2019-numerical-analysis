import numpy as np 
a = np.array([[-1, 2, 1], [2, -4, 1], [1, 1, -6]])
ainv = np.linalg.inv(a)
print("a : ", a)
print("a inverse: ", ainv)
v = [1, 2, 3]
print(v)
for i in range(1, 20):
    print("round ", i)
    b = np.dot(ainv, v)
    print(b)
    lam = 1 / max(b)
    print(lam)
    v = lam * b
    print(v)
    
norm = np.array([[6, 2, 1], [2, 3, 1], [1, 1, 1]])
test = np.dot(norm, v) / v
print("--------")
print(test)
print("--------")
eigen = np.linalg.eigvals(norm)
print(eigen)
vec = np.linalg.eigh(a)
print(vec)