b = []
for l in open("input"):
    o, v = l.split()
    b.append([o, int(v)])

def f():
    s = set()
    a = p = 0
    while 0 <= p < len(b) and not p in s:
        s.add(p)
        o, v = b[p]
        if o == "acc": a += v
        if o == "jmp": p += v
        else: p += 1
    return p == len(b), a

print(f()[1])

for i, (o, _) in enumerate(b):
    if o == "acc": continue
    b[i][0] = ("nop", "jmp")[o == "nop"]
    ok, a = f()
    b[i][0] = o
    if ok:
        print(a)
        break
