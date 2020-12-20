lines = open("input").readlines()
d = {}
while 1:
    l = lines.pop(0).strip()
    if not l: break
    k, v = l.split(": ")
    d[k] = [w.split() for w in v.split("|")]

def g(s, i=0, r="0"):
    if not r.isdigit():
        if i < len(s) and s[i] == r[1]: return {i + 1}
        return set()
    p = set()
    for w in d[r]:
        ii = {i}
        for v in w:
            jj, ii = ii, set()
            for x in jj: ii |= g(s, x, v)
        p |= ii
    return p

c = 0
for l in lines:
    l = l.strip()
    c += len(l) in g(l)
print(c)

d["8"] = [["42"], ["42", "8"]]
d["11"] = [["42", "31"], ["42", "11", "31"]]

c = 0
for l in lines:
    l = l.strip()
    c += len(l) in g(l)
print(c)
