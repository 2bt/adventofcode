for K, M in (1, 1), (811589153, 10):
    a = [int(x) * K for x in open("input")]
    b = list(enumerate(a))
    o = (a.index(0), 0)
    for x in b * M:
        i = b.index(x)
        b.pop(i)
        b.insert((i + x[1]) % len(b), x)
    z = b.index(o)
    print(sum(b[(z + x) % len(b)][1] for x in (1000, 2000, 3000)))
