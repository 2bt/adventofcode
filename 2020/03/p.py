a = [l.strip() for l in open("input")]

def f(dx, dy = 1):
    x = t = 0
    for y in range(0, len(a), dy):
        t += a[y][x % len(a[0])] == "#"
        x += dx
    return t

print(f(3))
print(f(1) * f(3) * f(5) * f(7) * f(1, 2))
