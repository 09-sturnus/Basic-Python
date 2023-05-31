a = input("aの値を入力: ")
b = input("bの値を入力: ")


# TODO
'''
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
'''
    

def is_prime(x):
    x = float(x)
    if x.is_integer():
        x = int(x)
    else:
        raise ValueError("Input is not integer")
        
    if x <= 0:
        raise ValueError("Input is not positive")

    d = 2
    while d <= x**0.5:
        if x%d == 0:
            return False
            break
        else:
            d += 1
    else:
        return True


print(is_prime(a))
print(is_prime(b))
