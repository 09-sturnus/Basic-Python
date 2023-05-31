# TODO
epsilon = 1.0

while True:
    epsilon = epsilon / 2
    if not (1 + epsilon > 1):
        break

print(epsilon)
