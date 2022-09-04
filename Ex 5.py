
for i in range(1, 20):
    b = str(bin(i))[2:]
    if sum(list(map(int, bin(i)[2:]))) % 2 == 0:
        b = b + '0'
        b = b.replace(b[:2], '10', 1)
    else:
        b = b + '1'
        b = b.replace(b[:2], '11', 1)
    if int(b, 2) > 40:
        print(i)
        break


