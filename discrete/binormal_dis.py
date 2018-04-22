import math

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

def px_list(give_n, give_p, x_list, q):
    total = 0
    for give_x in x_list:
        total += px(give_n, give_p, give_x, q)
    return total


give_n = 10
give_p = 0.25
give_x = 5
q = 1 - give_p

# print("px", px(give_n, give_p, give_x, q))
print("mu", mu(give_n, give_p))
print("sigma", sigma(give_n, give_p, q))
print("px_list", px_list(give_n, give_p, [3], q))