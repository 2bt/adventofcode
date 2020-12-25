A = "135468729"

a = A
for _ in range(100):
    i = a[0]
    t = a[1:4]
    a = a[4:] + i
    while 1:
        i = str((int(i) - 2) % 9 + 1)
        p = a.find(i)
        if p != -1: break
    a = a[:p+1] + t + a[p+1:]
p = a.find("1")
print(a[p+1:] + a[:p])


N = 1000000
L = 10000000
t = list(map(int, A))
a = [0] * (N + 1)
p = 0
for i in t + list(range(10, len(a))):
    a[p] = i
    p = i
l = max(a)
a[l], a[0] = a[0], 0
for _ in range(L):
    n = a[l]
    p = a[n]
    q = a[p]
    r = a[q]
    x = n
    while 1:
        x -= 1
        if x == 0: x = N
        if x != p and x != q and x != r: break
    a[n] = a[r]
    a[r] = a[x]
    a[x] = p
    l = n
print(a[1] * a[a[1]])
