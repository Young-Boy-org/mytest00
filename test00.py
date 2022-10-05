import numpy as np

aa = np.random.randint(0,50,(5,3))
bb = aa[:,::-1]
print(aa,bb)