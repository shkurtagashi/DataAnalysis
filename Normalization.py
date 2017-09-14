#Libraries
from pylab import *

# Signal normalization between 0 and 1
def normalization(sig):
    sig = map(lambda x: float(x), sig)
    sig = list(sig)
    normalized = []
    min_val = min(sig)
    max_val = max(sig)

    for i in range(len(sig)):
        normalized.append(((sig[i] - min_val) / (max_val - min_val)))
    return normalized


def my_custom_norm(x, y):
    return (x * x) + (y * y)