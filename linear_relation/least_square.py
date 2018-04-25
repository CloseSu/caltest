import numpy as np
import math


def ss_xx(x):
    sigma_pow_2_x = np.sum(np.power(x, 2))
    sigma_x = np.sum(x)
    return sigma_pow_2_x - math.pow(sigma_x, 2) / len(x)

def ss_xy(x,y):
    sigma_xy = np.sum(np.multiply(x,y))
    sigma_x = np.sum(x)
    sigma_y = np.sum(y)
    return sigma_xy - sigma_x * sigma_y / len(x)


def b1(x, y):
    ssxx = ss_xx(x)
    ssxy = ss_xy(x, y)
    return ssxy / ssxx

def b0(x,y):
    return np.mean(y) - b1(x, y) * np.mean(x)


x = [2,3,3,3,4,4,5,5,5,6]
y = [28.7,24.8,26,30.5,23.8,24.6,23.8,20.4,21.6,22.1]


print("b1: ", b1(x, y))
print("b0: ", b0(x, y))