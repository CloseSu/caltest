import sympy
import math


def ty(num):
    x = sympy.Symbol('x')
    exp = x**2
    sums = 0
    sum_f = 0
    for i in range(2):
        diff_fx = exp.diff(x,i)
        diff_fx = diff_fx.evalf(subs={x:num})
        fac_i = math.factorial(i)
        sums += diff_fx / fac_i * (num ** i)
        sum_f += diff_fx / fac_i * (x ** i)
    print(sums)
    print(sum_f)


ty(1)