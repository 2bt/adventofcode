s = 0
for l in open("input"):
    for d in l.split("|")[1].split(): s += len(d) in [2, 4, 3, 7]
print(s)

s = 0
for l in open("input"):
    w, d = l.split("|")
    w1, w7, w4, w2, w3, w5, w0, w6, w9, w8 = sorted(map(set, w.split()), key=len)
    if   w2 & w1 == w1: w2, w3 = w3, w2
    elif w5 & w1 == w1: w5, w3 = w3, w5
    if len(w4 - w5) == 2: w2, w5 = w5, w2
    if   not w4 - w0: w0, w9 = w9, w0
    elif not w4 - w6: w6, w9 = w9, w6
    if not w5 - w0: w6, w0 = w0, w6
    w = [w0, w1, w2, w3, w4, w5, w6, w7, w8, w9]
    s += sum(w.index(set(x)) * 10 ** (3 - i) for i, x in enumerate(d.split()))
print(s)
