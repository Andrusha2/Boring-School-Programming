def f(N, stop):
    if N == stop:
        return 1
    elif N > stop or N == 17:
        return 0
    else:
        K = f(N + 1, stop) + f(N * 2, stop)
        return K


M = f(1, 10) * f(10, 35)
print(M)
