import numpy as np 

np.set_printoptions(precision=None)
epsilon = float(input())
a = float(input())
n = int(input())
h = 1.0 / n
wucha = 0.00001

n += 1
x = np.linspace(0, 1, n)
temp = np.ones(n) * 0.3

y_0 = np.zeros((1, n))
y_1 = np.zeros((1, n))
y_2 = np.zeros((1, n))
y_3 = np.zeros((1, n))

A = np.zeros((n, n))
D = np.zeros((n, n))
L = np.zeros((n, n))
U = np.zeros((n, n))
b = a * h * h

B = np.ones((n, 1))
B = B * b
B[n - 1] -= epsilon + h
# print("B = ", B)

for i in range(n):
    for j in range(n):
        if i == j:
            A[i, j] = - 2 * epsilon - h
        elif i + 1 == j:
            A[i, j] = epsilon + h 
        elif i - 1 == j:
            A[i, j] = epsilon

def devide():
    print("-----------------------------------------")

def jingque():
    y = (1 - a) * (1 - np.exp( -1 * x / epsilon)) / (1 - np.exp(-1.0 / epsilon)) + a * x
    return y

def jacob():

    x_j = temp.copy() 
    cnt = 0
    while (1):
        cnt = cnt + 1
        y = x_j.copy()
        for i in range(n):
            x_j[i] = B[i]
            for j in range(max(0, i - 1), min(n, i + 2)):
                if i != j:  
                    x_j[i] = x_j[i] - A[i, j] * y[j]
            x_j[i] = x_j[i] / A[i, i]

        if np.linalg.norm(x_j - y) / 10 < wucha:
            break
    print("steps = ", cnt)
    return y        

def GS():
    x_g = temp.copy() 
    cnt = 0
    while (1):
        cnt = cnt + 1
        record = x_g.copy()
        for i in range(n):
            x_g[i] = B[i]
            for j in range(max(0, i - 1), min(n, i + 2)):
                if i != j:  
                    x_g[i] = x_g[i] - A[i, j] * x_g[j]
            x_g[i] = x_g[i] / A[i, i]

        if np.linalg.norm(x_g - record) / 10 < wucha:
            break
    print("steps = ", cnt)
    return x_g
    
def SOR(w):
    x_s = temp.copy()
    cnt = 0
    while (1):
        cnt += 1
        record = x_s.copy()
        for i in range(n):
            second = B[i]
            first = (1 - w) * x_s[i]
            for j in range(max(0, i - 1), min(n, i + 2)):
                if i != j:  
                    second = second - A[i, j] * x_s[j]
            x_s[i] = first + w * second / A[i, i]
        # print(x_s)
        if np.linalg.norm(x_s - record) / 10 < wucha:
            break
    print("steps = ", cnt)    
    return x_s


if __name__ == "__main__":

    print("A = ", A)
    devide()
    print("x = ", x)
    devide()
    y_0 = jingque()
    print("jingque = ", y_0)
    devide()

    # y_1 = jacob()
    # print("jacob = ", y_1)
    # devide()
    # print("jacob wucha = ", y_1 - jingque())

    # y_2 = GS()
    # print("GS = ", y_2)
    # devide()
    # print("GS wucha = ", y_2 - jingque())

    y_3 = SOR(0.4)
    print("SOR = ", y_3)
    devide()
    print("SOR wucha = ", y_3 - jingque())
