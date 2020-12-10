a = sorted(map(int, open("input")))
a = [0] + a + [a[-1] + 3]
c = [0] * 4
for x, y in zip(a, a[1:]): c[y - x] += 1
print(c[1] * c[3])


def f(i, c={len(a) - 1: 1}):
    if i not in c: c[i] = sum(f(i + o) for o in [1, 2, 3] if i + o < len(a) and a[i + o] <= a[i] + 3)
    return c[i]
print(f(0))
