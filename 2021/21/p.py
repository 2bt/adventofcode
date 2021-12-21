d = []
i = 0
while 1:
    x = 3
    for _ in range(3):
        x += i
        i = (i + 1) % 100
    d.append(x)
    if i == 0: break

p = [int(l.split()[-1]) - 1 for l  in open("input")]
q = p * 1
s = [0, 0]
i = 0
j = 0
while 1:
    p[i] = (p[i] + d[j % 100]) % 10
    j += 1
    s[i] += p[i] + 1
    if s[i] >= 1000: break
    i ^= 1
print(s[i ^ 1] * j * 3)


from collections import defaultdict
from functools import cache
d = defaultdict(int)
for x in range(3):
    for y in range(3):
        for z in range(3): d[x + y + z + 3] += 1

@cache
def f(i, px, py, sx, sy):
    w = [0, 0]
    pp = px
    ss = sx
    for k, v in d.items():
        px = (pp + k) % 10
        sx = ss + px + 1
        if sx >= 21: w[0] += v
        else:
            ww = f(i ^ 1, py, px, sy, sx)
            w[0] += ww[1] * v
            w[1] += ww[0] * v
    return w
print(max(f(0, q[0], q[1], 0, 0)))
