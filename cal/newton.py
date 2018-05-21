import sympy
x = sympy.Symbol('x')
func = x**2 -2 * x -4

def newton(fx, num):
    return num - fx.evalf(subs={x:num}) / fx.diff(x).evalf(subs={x:num})

# print(newton(func, 2))

new_num = 0
for i in range(10):
    new_num = newton(func, new_num)
    print(new_num)
