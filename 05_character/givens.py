import numpy as np 
import math

T = np.array([[1, 0, 0, -1, -1, 0], 
              [0, 1, 0, 1, 0, -1],
              [0, 0, 1, 0, 1, 1]])

T = np.transpose(T)

g1 = np.array([[1/np.sqrt(2), 0, 0, -1/np.sqrt(2), 0, 0], 
              [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
              [1/np.sqrt(2), 0, 0, 1/np.sqrt(2), 0, 0], 
              [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]])
            
g2 = np. array([[np.sqrt(2)/np.sqrt(3), 0, 0, 0, -1/np.sqrt(3), 0], 
              [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], 
              [1/np.sqrt(3), 0, 0, 0, np.sqrt(2)/np.sqrt(3), 0], 
              [0, 0, 0, 0, 0, 1]])
ans = np.dot(g1, T)

print(T)
print(g1)
print(ans)
print(g2)
ans = np.dot(g2, ans)
print(ans)

