def f(a, x):
    return ((x % 2 == 0) <= (not(x % 3 == 0))) or (x + a >= 100)


for a in range(1, 10000):
    flag = True
    for x in range(1, 10000):
        if not(f(a, x)):
            flag = False
            break
    if flag:
        print(a)
        break
