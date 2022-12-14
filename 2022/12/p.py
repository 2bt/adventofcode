m = open("input").read() + "\n" * 200
W = m.find("\n") + 1
def h(p):
    c = m[p]
    if c == "\n": return 99
    if c == "S": return 0
    if c == "E": return 25
    return ord(c) - ord("a")
q = [m.find("S")]
v = set()
for i in range(999):
    q, oq = [], q
    for p in oq:
        if m[p] == "E":
            print(i)
            break
        for n in [p - 1, p + 1, p - W, p + W]:
            if n in v: continue
            if h(n) > h(p) + 1: continue
            v.add(n)
            q.append(n)
q = [m.find("E")]
v = set()
for i in range(999):
    q, oq = [], q
    for p in oq:
        if h(p) == 0:
            print(i)
            exit()
        for n in [p - 1, p + 1, p - W, p + W]:
            if n in v: continue
            if h(n) > 25 or h(n) < h(p) - 1: continue
            v.add(n)
            q.append(n)
