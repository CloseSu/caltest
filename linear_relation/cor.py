import math

def sigma(x):
    total = 0
    for i in x:
        total += i
    return total

def sigma_pow_2(x):
    total = 0
    for i in x:
        total += math.pow(i, 2)
    return total

def sigma_x_muti_y(x,y):
    total = 0
    for i,j in zip(x,y):
        total += i * j
    return total

def ss_xx(x):
    sigma_pow_2_x = sigma_pow_2(x)
    sigma_x = sigma(x)
    return sigma_pow_2_x - math.pow(sigma_x, 2) / len(x)

def ss_xy(x,y):
    sigma_xy = sigma_x_muti_y(x, y)
    sigma_x = sigma(x)
    sigma_y = sigma(y)
    return sigma_xy - sigma_x * sigma_y / len(x)


def cor_xy(x,y):
    return ss_xy(x,y) / (math.sqrt(ss_xx(x) * ss_xx(y)))



x = [2,3,3,3,4,4,5,5,5,6]
y = [28.7,24.8,26,30.5,23.8,24.6,23.8,20.4,21.6,22.1]


print(cor_xy(x, y))