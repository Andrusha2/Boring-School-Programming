def prost(a):
    for d in range(2, a):
        if a % d == 0:
            return False
    return True


for n in range(50):
    s = '>' + '0' * 39 + '1' * n + '2' * 39
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    summa = sum(int(i) for i in s if i != '>')
    if prost(summa):
        print(n)
        break

