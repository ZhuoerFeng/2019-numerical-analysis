import numpy as np 
a = np.array([ [8, 1, 6], [3, 5, 7], [4, 9, 2]])
eigen = np.linalg.eigvals(a)
print(eigen)