a = list(map(int, open("input").read().split(",")))
m = sorted(a)[len(a) // 2]
print(sum(abs(x - m) for x in a))

def s(x): return x * (x + 1) // 2
f = [0] * max(a)
for x in a:
    for i in range(len(f)): f[i] += s(abs(i - x))
m = f.index(min(f))
print(sum(s(abs(x - m)) for x in a))
