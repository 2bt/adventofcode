def load(l):
    x = [-1] * 16
    i, s = 0, 16
    for c in l:
        if c == "[": s //= 2
        if c == "]": s *= 2
        if c.isdigit(): x[i] = int(c); i += s
    return x

def add(x, y):
    x = x + y
    while 1:
        # explode
        e = False
        for i in range(0, len(x), 2):
            if x[i + 1] != -1:
                for j in range(i + 2, len(x)):
                    if x[j] != -1: x[j] += x[i + 1]; break
                for j in range(i - 1, -1, -1):
                    if x[j] != -1: x[j] += x[i]; break
                x[i:i + 2] = 0, -1
                e = True
                break
        if e: continue
        # split
        for i, k in enumerate(x):
            if k > 9:
                s = 1
                while i + s < len(x) and x[i + s] == -1: s += 1
                x[i + s // 2] = (x[i] + 1) // 2
                x[i] //= 2
                break
        else: break
    return x[::2]

def mag(x):
    m = len(x) // 2
    if m == 0 or x[m] == -1: return x[0]
    return 3 * mag(x[:m]) + 2 * mag(x[m:])

a = list(map(load, open("input")))
x = a[0]
for y in a[1:]: x = add(x, y)
print(mag(x))

print(max(mag(add(x, y)) for x in a for y in a if x != y))
