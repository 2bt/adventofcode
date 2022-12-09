def clamp(v, a, b): return max(a, min(b, v))
for L in 2, 10:
    p = set()
    x = [0] * L
    y = [0] * L
    for l in open("input"):
        d, n = l.split()
        dx = {"L":-1,"R":1}.get(d, 0)
        dy = {"U":-1,"D":1}.get(d, 0)
        for _ in range(int(n)):
            p.add((x[-1], y[-1]))
            x[0] += dx
            y[0] += dy
            for i in range(1, len(x)):
                px = x[i - 1]
                py = y[i - 1]
                if abs(px - x[i]) > 1 and abs(py - y[i]) > 1: pass
                elif abs(px - x[i]) > 1: y[i] = py
                elif abs(py - y[i]) > 1: x[i] = px
                x[i] = clamp(x[i], px - 1, px + 1)
                y[i] = clamp(y[i], py - 1, py + 1)
            p.add((x[-1], y[-1]))
    print(len(p))
