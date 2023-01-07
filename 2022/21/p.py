a = {}
for l in open("input"):
    w = l.split()
    k = w.pop(0)[:-1]
    a[k] = int(w[0]) if len(w) == 1 else w

def f(k):
    v = a[k]
    if type(v) == int: return v
    return eval(f"{f(v[0])} {v[1]} {f(v[2])}")
print(int(f("root")))

a["root"][1] = "-"
a["humn"] = 0
d0 = f("root")
while 1:
    a["humn"] += 1
    dx = f("root")
    if dx == int(dx): break
a["humn"] = int(d0 / (d0 - dx) * a["humn"])
assert f("root") == 0
print(a["humn"])
