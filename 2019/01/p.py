

def fuel(x, cache={0:0}):
    if x in cache: return cache[x]
    f = max(0, x / 3 - 2)
    f += fuel(f)
    cache[x] = f
    return f

s = 0
for x in open("input"): s += fuel(int(x))
print s
