a = open("input").read().strip()

W = 25
H = 6

l = []
while a:
    l.append(a[:W * H])
    a = a[W * H:]

q = min(l, key=lambda q:q.count("0"))
print q.count("1") * q.count("2")

s = ""
for i in range(W * H):
    for q in l:
        if q[i] != "2":
            s += " #"[int(q[i])]
            break
    if i % W == W - 1: s += "\n"
print s
