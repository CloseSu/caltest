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

x = [0.0, 0.0, 1.1, 1.4, 1.6, 1.7, 2.0, 2.0, 2.2, 2.2]
y = [0.3, 0.1, 4.7, 3.2, 5.1, 7.0, 5.0, 6.1, 8.6, 9.5]
ta = 3.182
xp = 2

print("b1: ", b1(x, y))
print("b0: ", b0(x, y))
print("sse:", sse(x, y))
print("s esu", s_esu(x,y))
print("b1 confidence_interval_part2:", confidence_interval_part2(x,y, ta))
print("confidence for b1:", get_yp_range(b1(x,y), confidence_interval_part2(x,y, ta)))
print("t:", t_test(x,y))
print("cod r:", math.sqrt(cod(x,y)))
print("========================================================")
print("yp:", yp(x,y,xp))
print("confidence inteval:", confidence_interval_for_mean_value(x,y,ta,xp, 0))
print("confidence range:", get_yp_range(yp(x,y,xp), confidence_interval_for_mean_value(x,y,ta,xp, 0)))

print("predict inteval:", confidence_interval_for_mean_value(x,y,ta,xp, 1))
print("predict range:", get_yp_range(yp(x,y,xp), confidence_interval_for_mean_value(x,y,ta,xp, 1)))
