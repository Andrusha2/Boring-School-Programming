
f = open('17.txt', 'r')
a = f.readlines()
a = list(map(int, a))
mx = 9973 ** 2
#a = [3, 2, 1, 3, 3]
mmx = 0
counter = 0
for i in range(1, len(a)):
    if ((abs(a[i]) % 10 == 3 and abs(a[i - 1]) % 10 != 3) or (abs(a[i]) % 10 != 3 and abs(a[i - 1]) % 10 == 3)) and ((a[i] ** 2 + a[i - 1] ** 2) >= mx):
        counter += 1
        if (a[i] ** 2 + a[i - 1] ** 2) > mmx:
            mmx = a[i] ** 2 + a[i - 1] ** 2
print(counter, mmx)
