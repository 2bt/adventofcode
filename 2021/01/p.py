a = list(map(int, open("input")))
print(sum(x < y for x, y in zip(a, a[1:])))
print(sum(a[i] < a[i + 3] for i in range(len(a) - 3)))
