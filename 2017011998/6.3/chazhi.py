import numpy as np 
import matplotlib
import matplotlib.pyplot as plt

# phi 1, t, t^2
A = np.array([
    [1, 1, 1], 
    [1, 1.5, 2.25], 
    [1, 2, 4], 
    [1, 2.5, 6.25], 
    [1, 3, 9], 
    [1, 3.5, 12.25], 
    [1, 4, 16], 
    [1, 4.5, 20.25]])
def devide():
    print("-----------------------------------------")

if __name__ == "__main__":   
    t = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8])
    f = np.array([33.4, 79.5, 122.65, 159.05, 189.15, 214.15, 238.65, 252.2, 267.55, 280.5, 296.65, 301.65, 310.4, 318.15, 325.15])
    f = np.transpose(f)
    t_1 = np.ones(15)
    t_2 = t.copy()
    t_3 = t * t 
    a = np.vstack((t_1, t_2, t_3))
    b = np.dot(a, f)
    temp = np.transpose(a)
    G = np.dot(a, temp)
    L = np.linalg.cholesky(G)
    L_inv = np.linalg.inv(L)
    y = np.dot(L_inv, b)
    LT = np.transpose(L)
    LT = np.linalg.inv(LT)

    x = np.dot(LT, y)

    direct_x = np.dot (np.linalg.pinv(np.transpose(a)), f)

    real_f = x[0] * t_1 + x[1] * t_2 + x[2] * t_3
    delta_f = real_f - f
    delta = np.linalg.norm(delta_f) / np.sqrt(15)
    
    print(a)
    devide()
    print(f)
    devide()
    print(b)
    devide()
    print(G)
    devide()
    print(L)
    devide()
    print(y)
    devide()
    print(x)
    devide()
    print(direct_x)
    devide()
    print(f)
    devide()
    print(real_f)
    devide()
    print(delta_f)
    devide()
    print(delta)

    fig, ax = plt.subplots()
    ax.plot(t, f)
    ax.plot(t, real_f)
    ax.set(xlabel='x', ylabel='f', title='Curve fitting of linear function and exponential function')
    ax.grid()
    for i in range(len(t)):
        plt.scatter(t[i], f[i], marker = 'x', color = 'red')

    # fig.savefig("test.png")
    
    # x - f  x - real_f

    lnf = np.log(f)
    a = np.vstack((t_1, t_2))
    b = np.dot(a, lnf)
    G = np.dot(a, np.transpose(a))
    L = np.linalg.cholesky(G)
    L_inv = np.linalg.inv(L)
    y = np.dot(L_inv, b)
    L = np.transpose(L)
    x = np.dot( np.linalg.inv(L), y)
    numa = np.exp(x[0])
    real_f = numa * np.exp(x[1] * t_2)
    delta_f = real_f -f
    delta = np.linalg.norm(delta_f) / np.sqrt(15)
    ax.plot(t, real_f)

    print(lnf)
    devide()
    print(a)
    devide()
    print(b)
    devide()
    print(G)
    devide()
    print(L)
    devide()
    print(y)
    devide()
    print(x)
    devide()
    print(numa)
    print(x[1])
    devide()
    print(f)
    devide()
    print(real_f)
    devide()
    print(delta_f)
    devide()
    print(delta)

    plt.show()


        
