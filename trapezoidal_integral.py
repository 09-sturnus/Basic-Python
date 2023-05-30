from math import sin, pi
# --example--
# print(sin(0))
# >>> 0
# -----------

h = pi / 200

S = 0

for k in range(101):
    if k != 0:
        S += (sin((k-1)*h) + sin(k*h)) * h/2

print(S)