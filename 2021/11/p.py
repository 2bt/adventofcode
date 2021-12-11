a = [-1 if x == "\n" else int(x) for x in open("input").read()] + [-1] * 11
def f(i):
    if a[i] in (-1, 10): return
    a[i] += 1
    if a[i] < 10: return
    for o in [-12, -11, -10, -1, 1, 10, 11, 12]: f(i + o)
c = n = q = 0
while q < 100:
    for i in range(len(a)): f(i)
    q = a.count(10)
    if n < 100: c += q
    a = [[x, 0][x > 9] for x in a]
    n += 1
print(c)
print(n)
