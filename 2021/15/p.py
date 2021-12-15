import queue

a = [list(map(int, l.strip())) for l in open("input")]
w = len(a)

def f(x, y):
    if x < 0 or y < 0: return 0
    if x >= w * n or y >= w * n: return 0
    return (a[y % w][x % w] - 1 + x // w + y // w) % 9 + 1

for n in 1, 5:
    q = queue.PriorityQueue()
    q.put((0, 0, 0))
    v = {(0, 0)}
    t = w * n - 1
    while q:
        r, x, y = q.get()
        if (x, y) == (t, t): break
        for i in range(4):
            x2 = x + [-1, 0, 1, 0][i]
            y2 = y + [0, -1, 0, 1][i]
            dr = f(x2, y2)
            if (x2, y2) in v or not dr: continue
            v.add((x2, y2))
            q.put((r + dr, x2, y2))
    print(r)
