a = [10 if c == "\n" else int(c) for c in open("input").read()]
w = a.index(10) + 1
a = a + [10] * w

s = 0
for i, x in enumerate(a):
    if all(x < a[i + o] for o in [-1, -w, 1, w]): s += x + 1
print(s)

def f(p):
    if a[p] >= 9: return 0
    a[p] = 9
    return 1 + sum(f(p + o) for o in [-1, -w, 1, w])
s = 1
for x in sorted(map(f, range(len(a))))[-3:]: s *= x
print(s)
