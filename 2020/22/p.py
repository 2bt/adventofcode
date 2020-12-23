a, b = [list(map(int, p.split()[2:])) for p in open("input").read().split("\n\n")]
while b:
    if a[0] < b[0]: a, b = b, a
    a.append(a.pop(0))
    a.append(b.pop(0))
print(sum((i + 1) * x for i, x in enumerate(a[::-1])))


a, b = [[int(x) for x in p.split()[2:]] for p in open("input").read().split("\n\n")]
def f(a, b):
    t = tuple(a), tuple(b)
    s = {t}
    while a and b:
        win, lose = a, b
        if a[0] < len(a) and b[0] < len(b):
            if f(a[1:a[0] + 1], b[1:b[0] + 1]): win, lose = b, a
        elif a[0] < b[0]: win, lose = b, a
        win.append(win.pop(0))
        win.append(lose.pop(0))
        u = tuple(a), tuple(b)
        if u in s: return False
        s.add(u)
    return a == []
if f(a, b): a = b
print(sum((i + 1) * x for i, x in enumerate(a[::-1])))

