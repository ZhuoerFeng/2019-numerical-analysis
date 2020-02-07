import numpy as np 
a=np.array([[5 / 0.9 ,0,0],[-1, 4 / 0.9 ,0],[2, -3, 10 / 0.9]])
print(a)
w = 0.9
M = np.linalg.inv(a) 
N = np.array([[5 / 9.0 ,-2, -1],[0, 4 / 9.0 ,-2],[0 , 0, 10 / 9.0]])
print(M)
print(N)
# c = np.array([[0, -2, -1], [0, 0, -2], [0, 0, 0] ])
d = np.dot(M, N)
print(d)
v = np.array([-12, 20, 3])
e = np.dot(M, v)
print(e)