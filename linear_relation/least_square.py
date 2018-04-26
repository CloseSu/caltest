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

def cod(x,y):
    return b1(x,y) * ss_xy(x,y) / ss_xx(y)

def yp(x,y, target_x):
    return target_x * b1(x, y) + b0(x,y)

def confidence_interval_for_mean_value(x,y, ta2, xp, predict=0):
    s_es = s_esu(x,y)
    xp_minus_xmean = math.pow(xp - np.mean(x),2)
    xp_minus_xmean_divide_ssxx = xp_minus_xmean / ss_xx(x)
    total = math.sqrt(predict + 1/len(x) + xp_minus_xmean_divide_ssxx)
    return ta2 * s_es * total

def get_yp_range(yp, interval):
    return yp - interval, yp + interval

x = [2,7,2,7,2,7,0, 4,5,4,0,1,0,1, 0,6,6,2,2,1, 3,1,3,1,3,1]
y = [76,29,96,63,79,71,88, 41,63,88,98,99,89,96, 92,55,70,80,75,63, 90,90,68,84,80,78]
ta = 2.064
xp = 5

print("b1: ", b1(x, y))
print("b0: ", b0(x, y))
print("sse:", sse(x, y))
print("s esu", s_esu(x,y))
print("b1 confidence_interval_part2:",confidence_interval_part2(x,y, ta))
print("t:", t_test(x,y))
print("cod r2:", cod(x,y))

print("yp:", yp(x,y,xp))
print("inteval:", confidence_interval_for_mean_value(x,y,ta,xp, 1))
print("range:", get_yp_range(yp(x,y,3.5), confidence_interval_for_mean_value(x,y,ta,xp, 1)))
