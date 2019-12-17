a = map(int, open("input").read().strip())
for _ in range(100):
    b = []
    for i in range(len(a)):
        q = abs(sum(x * [0, 1, 0, -1][((j + 1) / (1 + i))%4] for j, x in enumerate(a))) % 10
        b.append(q)
    a = b
print "".join(map(str, a[:8]))
