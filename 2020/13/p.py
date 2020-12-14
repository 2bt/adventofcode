import math


f = open("input")
n = int(f.readline())
a = [(-(i % -int(w)), int(w)) for i, w in enumerate(f.readline().strip().split(",")) if w.isdigit()]
b = [-n % x for _, x in a]
i = min(range(len(a)), key=lambda i:b[i])
print(a[i][1] * b[i])


m = 1
for _, x in a: m = m * x // math.gcd(m, x)

s = 0
for i, x in a:
    n = m // x
    for k in range(n, n * x, n):
        if k % -x == -1:
            s -= k * i
            break
print(s % m)
