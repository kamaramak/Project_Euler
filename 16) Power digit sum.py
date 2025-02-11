import numpy as np
data = np.array([int(i) for i in str(2 ** 1000)])
print(np.sum(data))
