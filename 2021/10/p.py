e = 0
f = []
for l in open("input"):
    s = []
    for x in l.strip():
        i = "([{<".find(x)
        if i >= 0:
            s.append(i)
            continue
        i = ")]}>".find(x)
        j = s.pop()
        if i != j:
            s.clear()
            e += [3, 57, 1197, 25137][i]
            break
    if s:
        q = 0
        for i in reversed(s): q = q * 5 + i + 1
        f.append(q)
print(e)
print(sorted(f)[len(f)//2])
