x = 1
c = 0
s = 0
p = [0]
a = ""
def cycle(dx):
    global c, x, s, a
    p.append(dx)
    x += p.pop(0)
    a += " #"[x - 1 <= c % 40 <= x + 1]
    c += 1
    if c % 40 == 20: s += x * c
for l in open("input"):
    cycle(0)
    if l.startswith("addx"): cycle(int(l[5:]))
print(s)
while a:
    print(a[:40])
    a = a[40:]
