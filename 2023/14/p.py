a = list(map(list, open("input").read().split()))
H = len(a)
W = len(a[0])

for k in range(W):
    for i in range(H):
        c = a[i][k]
        if c != ".": continue
        for j in range(i + 1, H):
            d = a[j][k]
            if d == "#": break
            if d == "O":
                a[i][k] = "O"
                a[j][k] = "."
                break

print(sum(r.count("O") * (H - i) for i, r in enumerate(a)))

q = []
for x in range(200):
    for _ in range(4):
        for k in range(W):
            for i in range(H):
                c = a[i][k]
                if c != ".": continue
                for j in range(i + 1, H):
                    d = a[j][k]
                    if d == "#": break
                    if d == "O":
                        a[i][k] = "O"
                        a[j][k] = "."
                        break
        a = list(map(list, zip(*a[::-1])))
    q.append(sum(r.count("O") * (H - i) for i, r in enumerate(a)))
print(q[-38:][(1000000000 - 1 - 200) % 38])

