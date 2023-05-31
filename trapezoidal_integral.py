from math import sin , pi
# --example--
# print(sin(0))
# >>> 0
# -----------

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
