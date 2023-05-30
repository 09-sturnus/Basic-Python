a = input("aの値を入力: ")
b = input("bの値を入力: ")

a = int(a)
b = int(b)

# TODO
d = 2
flag = True

while d <= a**0.5:
    if a%d == 0:
        print("%dは%dで割り切れるので素数ではありません" % (a, d))
        flag = False
        break
    else:
        d += 1

if flag:
    print("%dは素数です" % a)

d = 2
flag = True

while d <= b**0.5:
    if b%d == 0:
        print("%dは%dで割り切れるので素数ではありません" % (b, d))
        flag = False
        break
    else:
        d += 1

if flag:
    print("%dは素数です" % b)

