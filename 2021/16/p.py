a = list(map(int, open("input").read().strip().translate({
    ord(format(i, "X")) : format(i, "04b") for i in range(16)
})))


def num(n):
    x = 0
    for _ in range(n): x = x * 2 + a.pop(0)
    return x

V = 0

def pkg():
    global V
    V += num(3)
    t = num(3)
    if t == 4:
        x = 0
        b = 1
        while b:
            b = num(1)
            x = x * 16 + num(4)
        return x
    if num(1):
        p = [pkg() for _ in range(num(11))]
    else:
        n = num(15)
        l = len(a) - n
        p = []
        while len(a) > l: p.append(pkg())
    if t == 0: return sum(p)
    if t == 1:
        x = 1
        for v in p: x *= v
        return x
    if t == 2: return min(p)
    if t == 3: return max(p)
    if t == 5: return p[0] > p[1]
    if t == 6: return p[0] < p[1]
    if t == 7: return p[0] == p[1]

x = pkg()
print(V)
print(x)
