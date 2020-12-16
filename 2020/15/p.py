a = list(map(int, open("input").read().split(",")))
#a = [0, 3, 6]
d = { x:i for i, x in enumerate(a[:-1]) }
x = a[-1]
i = len(a) - 1
for N in 2020, 30000000:
    while i < N:
        y = x
        if x in d: x = i - d[x]
        else:      x = 0
        d[y] = i
        i += 1
    print(y)
