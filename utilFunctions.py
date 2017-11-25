import numpy as np


def mtx_to_array(m):
    ar = np.zeros(m.shape[0] * m.shape[1])

    t = 0
    for k in range(m.shape[0]):
        for j in range(m.shape[1]):
            ar[t] = m[k][j]
            t = t + 1

    return ar
