from math import sin , pi, exp
# --example--
# print(sin(0))
# >>> 0
# -----------
'''
# 積分区間
a = 0
b = pi / 2

n = 100
h = (b - a) / n

S = 0

f = sin
for k in range(1, 1+n):
    if k != 0:
        S += (f(a + (k-1)*h) + f(a + k*h)) * h/2

print(S)
'''


def calc_integral(f, a=0, b=1, n=100):
    h = (b - a) / n
    S = 0.0

    for k in range(1, n+1):
        S += (f(a + (k-1)*h) + f(a + k*h)) * h/2
    return S


def func1(x):
    return 4 / (1 + x**2)


def func2(x):
    return (pi**0.5) * exp(-x**2)


print(calc_integral(sin, 0, pi/2, 50))
print(calc_integral(func1))
print(calc_integral(func2, -100, 100, 1000))
