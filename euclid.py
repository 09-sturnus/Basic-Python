a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
A = int(a)
B = int(b)
a = int(a)
b = int(b)

# a > bに大小を固定する
if b > a:
    t = b
    b = a
    a = t

while True:
    r = a % b
    if r == 0:
        print("%dと%dの最大公約数は%dです" % (A, B, b))
        break
    a = b
    b = r
