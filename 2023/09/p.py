s1 = s2 = 0
for l in open("input"):
    x = list(map(int, l.split()))
    p = []
    while x != [0] * len(x):
        p.append(x)
        x = [b - a for a, b in zip(x, x[1:])]
    while 1:
        q = p.pop()
        if not p: break
        p[-1][-1] += q[-1]
        p[-1][ 0] -= q[0]
    s1 += q[-1]
    s2 += q[ 0]
print(s1, s2)

