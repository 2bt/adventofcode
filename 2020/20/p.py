import collections

tiles = {}
for s in open("input").read().strip().split("\n\n"):
    l = s.split()[1:]
    tiles[int(l.pop(0)[:-1])] = t = []
    for l in l, l[::-1]:
        for _ in range(4):
            t.append(l)
            l = list(zip(*l[::-1]))

N = int(len(tiles) ** 0.5)
grid_ids = [[0] * N for _ in range(N)]
grid     = [["" for _ in range(9 * N + 1)] for _ in range(9 * N + 1)]

def f(ids, pos=0):
    if not ids: return True
    y = pos // N
    x = pos % N
    for i, id in enumerate(ids):
        grid_ids[y][x] = ids[i]
        for l in tiles[ids[i]]:
            match  = x == 0 or all(grid[y * 9 + o][x * 9] == l[o][0] for o in range(10))
            match &= y == 0 or all(grid[y * 9][x * 9 + o] == l[0][o] for o in range(10))
            if not match: continue
            for v, r in enumerate(l):
                for u, c in enumerate(r):
                    grid[y * 9 + v][x * 9 + u] = c
            if f(ids[:i] + ids[i + 1:], pos + 1): return True

f(list(tiles.keys())[::-1])
print(grid_ids[0][0] * grid_ids[0][-1] * grid_ids[-1][0] * grid_ids[-1][-1])


for i in range(N + 1): grid.pop(i * 8)
grid = list(map(list, zip(*grid[::-1])))
for i in range(N + 1): grid.pop(i * 8)

m = ["                  # ",
     "#    ##    ##    ###",
     " #  #  #  #  #  #   "]
mm = []
for m in m, m[::-1]:
    for _ in range(4):
        m = list(zip(*m[::-1]))
        mm.append(m)

for m in mm:
    for y in range(len(grid) - len(m) + 1):
        for x in range(len(grid) - len(m[0]) + 1):

            match = True
            for v, r in enumerate(m):
                for u, c in enumerate(r):
                    if c == "#" and grid[y + v][x + u] != "#":
                        match = False
                        break
                if not match: break

            if match:
                for v, r in enumerate(m):
                    for u, c in enumerate(r):
                        if c == "#": grid[y + v][x + u] = "."

print("".join(map("".join, grid)).count("#"))
