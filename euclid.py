a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
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
