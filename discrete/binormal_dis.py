import math
import numpy as np

def ladder_miti(n):
    total_n = 1
    for i in range(n):
        i = i + 1
        total_n = i * total_n
    # print("miti", total_n)
    return total_n

def cal_x_nx(x, n):
    nx = n - x
    if nx == 0:
        nx = 1
    if x == 0:
        x = 1
    total_x = ladder_miti(x)
    total_nx = ladder_miti(nx)
    return total_x * total_nx

def px(give_n, give_p, give_x, q) :
    return ladder_miti(give_n) / cal_x_nx(give_x, give_n) \
                   * math.pow(give_p, give_x) \
                   * math.pow(q, give_n - give_x)

def mu(give_n, give_p):
    return give_n * give_p

def sigma2(give_n, give_p, q):
    return give_n * give_p * q

def sigma(give_n, give_p, q):
    return math.sqrt(sigma2(give_n, give_p, q))

def get_all_p(give_n, give_p, q):
    p_lixt = []
    i_list = []
    for i in range(give_n + 1):
        px_num = round(px(give_n, give_p, i, q), 4)
        p_lixt.append(px_num)
        i_list.append(i)
    return p_lixt, i_list

def sum_exp(p_lixt, i_list):
    sum = 0
    for p,i in zip(p_lixt, i_list):
        sum += p * i
    return round(sum, 4)

give_n = 5
give_p = 0.17
give_x = 0
q = 1 - give_p

print("px", px(give_n, give_p, give_x, q))
print("get_all_p:", get_all_p(give_n, give_p, q)[0])
print("sum all p:", sum_exp(get_all_p(give_n, give_p, q)[0], get_all_p(give_n, give_p, q)[1]))
print("====================================================================================")
print("mu", mu(give_n, give_p))
print("sigma", sigma(give_n, give_p, q))