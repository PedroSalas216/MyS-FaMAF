# aproximacion de sum()
import numpy as np
N = 10_000
s = 0
for i in range(100):
    s += np.random.random() * N

print (s/100)    