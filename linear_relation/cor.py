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



# x = [2,3,3,3,4,4,5,5,5,6]
# y = [28.7,24.8,26,30.5,23.8,24.6,23.8,20.4,21.6,22.1]
x = [2,7,2,7,2,7,0, 4,5,4,0,1,0,1, 0,6,6,2,2,1, 3,1,3,1,3,1]
y = [76,29,96,63,79,71,88, 41,63,88,98,99,89,96, 92,55,70,80,75,63, 90,90,68,84,80,78]


print(cor_xy(x, y))