a = map(int, file("input").read().strip())
print sum(x for x, y in zip(a, a[1:] + a[-1:]) if x == y)
print sum(x for i, x in enumerate(a) if x == a[(i + len(a)/2) % len(a)])
