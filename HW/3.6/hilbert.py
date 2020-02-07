import numpy as np 
import numpy.matlib as M 
import numpy.matrixlib as m
import numpy as np
import matplotlib.pyplot as plt

def devide():
    print("-----------------------------------------")

n = int(input())
H = np.fromfunction(lambda i, j: 1.0 / (i + j + 1), (n, n))
x = np.ones(n)
raodong = np.ones(n)
raodong = raodong * 1e-7
b = np.dot(H, x)
b = b + raodong
temp = H.copy()
devide()
print(H)
devide()
print(x)
devide()
print(b)
L1 = np.linalg.cholesky(H)

def chol():
    for j in range(n):
        for k in range(j):
            temp[j, j] = temp[j, j] - temp[j, k] * temp[j, k]
        temp[j, j] = np.math.sqrt(temp[j, j])
        for i in range(j + 1, n):
            for k in range(j):
                temp[i, j] = temp[i, j] - temp[i, k]*temp[j, k]
            temp[i, j] = temp[i, j] / temp[j, j]
    for i in range(n):
        for j in range(i + 1, n):
            temp[i, j] = 0

def solve():
    temp1 = temp.copy()
    y = np.linalg.solve(temp1, b)
    temp2 = np.transpose(temp)
    x = np.linalg.solve(temp2, y)
    return x

if __name__ == "__main__":
    chol()
    devide()
    print("temp - L1 = ",temp - L1)
    x_chol = solve()
    print("x_chol = ", x_chol)
    r = b - np.dot(H, x_chol)
    d_x = x - x_chol
    delta_x = 0
    delta_r = 0
    for i in range(n):
        if delta_x < d_x[i]:
            delta_x = d_x[i]
        if delta_r < r[i]:
            delta_r = r[i]
    print("delta_x = ",delta_x)
    print("delta_r = ", delta_r)
