f = [1] * 2024
for n in range(2, 2024):
    f[n] = n * f[n - 1]
print(f[2023] / f[2020])
# recoursion does not work with big numbers((((((
