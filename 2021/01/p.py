a = list(map(int, open("input")))
print(sum(x < y for x, y in zip(a, a[1:])))
print(sum(x < y for x, y in zip(a, a[3:])))
