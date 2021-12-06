a = [0] * 9
for x in open("input").read()[::2]: a[int(x)] += 1
for n in 80, 256 - 80:
    for _ in range(n): a = [a[i - 8] + a[0] * (i == 6) for i, x in enumerate(a)]
    print(sum(a))
