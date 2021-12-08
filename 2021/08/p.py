s = 0
for l in open("input"):
    for d in l.split("|")[1].split(): s += len(d) in [2, 4, 3, 7]
print(s)

s = 0
for l in open("input"):
    w, d = l.split("|")
    w = sorted(map(set, w.split()), key=len)
    i = [i for i in [3, 4, 5] if w[i] & w[0] == w[0]][0] # find 3
    w[3], w[i] = w[i], w[3]
    i = [i for i in [4, 5] if len(w[2] - w[i]) == 2][0]  # find 2
    w[4], w[i] = w[i], w[4]
    i = [i for i in [6, 7, 8] if not w[2] - w[i]][0]     # find 9
    w[6], w[i] = w[i], w[6]
    i = [i for i in [7, 8] if not w[5] - w[i]][0]        # find 6
    w[7], w[i] = w[i], w[7]
    s += sum([1, 7, 4, 3, 2, 5, 9, 6, 0, 8][w.index(set(x))] * 10 ** (3 - i) for i, x in enumerate(d.split()))
print(s)
