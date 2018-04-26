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


def sse(x,y):
    return ss_xx(y) - b1(x,y) * ss_xy(x, y)

def s_esu(x,y):
    return math.sqrt(sse(x,y) / (len(x) -2))

def confidence_interval_part2(x,y, crical_i):
    return crical_i * s_esu(x,y) / math.sqrt(ss_xx(x))

def t_test(x,y,b0=0):
    return (b1(x,y) - b0) / (s_esu(x,y) / math.sqrt(ss_xx(x)))

x = [1,1,3,4,5]
y = [2,1,5,3,4]

print("b1: ", b1(x, y))
print("b0: ", b0(x, y))
print("sse:", sse(x, y))
print("s esu", s_esu(x,y))
print("confidence_interval_part2:",confidence_interval_part2(x,y, 2.353))
print("t:", t_test(x,y))