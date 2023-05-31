from math import pi
import random

#a = int(input("a の値を入力: "))
#b = int(input("b の値を入力: "))

# TODO
'''
A = a
B = b

# a > bに大小を固定する
if b > a:
    a, b = b, a

while True:
    r = a % b
    if r == 0:
        print("%dと%dの最大公約数は%dです" % (A, B, b))
        break
    a = b
    b = r
'''


def euclid(a, b):
    if b > a:
        a, b = b, a
    
    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r


def is_relative(a, b):
    if euclid(a, b) == 1:
        return True
    else:
        return False


def rand_relative():
    rand_int = [[random.randint(1, 10000) for i in range(2)] for j in range(100000)]
    
    rate = 0.0
    
    for i in range(len(rand_int)):
        if is_relative(rand_int[i][0], rand_int[i][1]):
            rate += 1
    
    return rate / len(rand_int)


print("Theoretical Value is %e" % (6.0 / (pi**2)))
print("Actual Value is %e" % rand_relative())
