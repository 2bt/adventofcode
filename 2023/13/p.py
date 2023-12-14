def f(r):
    w = len(r)
    for i in range(1, w):
        j = min(i, w - i)
        if r[i-j:i][::-1] == r[i:i+j]: yield i

def smudge(r):
    for m in 1, 100:
        r = list(map(list, zip(*r)))
        for l in r:
            for i, c in enumerate(l):
                l[i] = ".#"[c == "."]
                yield r, m
                l[i] = c

s1 = 0
s2 = 0
for z in open("input").read().split("\n\n"):
    r = z.split()
    for m in 1, 100:
        r = list(map(list, zip(*r)))
        for x in f(r):
            s1 += x * m
            q = x * m
            break

    for r, m in smudge(r):
        for x in f(r):
            if x and x * m != q:
                s2 += x * m
                break
        else: continue
        break

print(s1, s2)
