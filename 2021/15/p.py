import queue

a = [list(map(int, l.strip())) for l in open("input")]
w = len(a)

for n in 1, 5:
    q = queue.PriorityQueue()
    q.put((0, 0, 0))
    v = {(0, 0)}
    while q:
        r, x, y = q.get()
        if x == y == w * n - 1: break
        for i in range(4):
            x2 = x + [-1, 0, 1, 0][i]
            y2 = y + [0, -1, 0, 1][i]
            if (x2, y2) in v or x2 < 0 or y2 < 0 or x2 >= w * n or y2 >= w * n: continue
            r2 = (a[y2 % w][x2 % w] - 1 + x2 // w + y2 // w) % 9 + 1 + r
            v.add((x2, y2))
            q.put((r2, x2, y2))
    print(r)
