import re
x1, x2, y1, y2 = map(int, re.findall(r"-?\d+", open("input").read()))

def s(n): return (n * n + n) // 2
print(s(-y1 - 1))

def f(x, y):
    u, v = x, y
    while x <= x2 and y >= y1 and (x >= x1 or u > 0):
        if x >= x1 and y <= y2: return 1
        u -= u > 0
        v -= 1
        x += u
        y += v
    return 0
print(sum(f(x,y) for y in range(y1, -y1) for x in range(x2 + 1)))
