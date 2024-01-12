grid = open("input").read().split()
S = len(grid)
a = "".join(grid)
F = S * S - a.count("#")
x = a.find("S") % S
y = a.find("S") // S

patch = {(x, y): 0}
queue = [(x, y)]

def f():
    q = []
    for x, y in queue:
        for i in range(4):
            nx = x + [1, 0, -1, 0][i]
            ny = y + [0, 1, 0, -1][i]
            if grid[ny % S][nx % S] == "#": continue
            if (nx, ny) in patch: continue
            patch[nx, ny] = patch[x, y] + 1
            q.append((nx, ny))
    queue.clear()
    queue.extend(q)

for _ in range(64): f()
print(sum(i%2 == 0 for i in patch.values()))


f()
y = [sum(i%2 for i in patch.values())]
for _ in range(2):
    for _ in range(262): f()
    y.append(sum(i%2 for i in patch.values()))
q, w, e = y
a = w - q
s = e - w
q1 = (s - a) // 2
q2 = a - 3 * q1
q3 = q - q1 - q2
N = 26501365 // 262 + 1
print(q1 * N**2 + q2 * N + q3)
