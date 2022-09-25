alph = '0123456789abcde'
for x in alph:
    summa = int(f'123{x}5', 15) + int(f'1{x}233', 15)
    if summa % 14 == 0:
        print(summa // 14)
        break
