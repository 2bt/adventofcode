g = {}
dist = length = 9e99
for n, line in enumerate(open("input")):
    x = y = l = 0
    for w in line.split(","):
        d = "UDLR".find(w[0])
        dx = [0,0,-1,1][d]
        dy = [-1,1,0,0][d]
        for _ in range(int(w[1:])):
            x += dx
            y += dy
            l += 1
            if n == 0:
                if not (x,y) in g: g[x,y] = l
            else:
                if (x,y) in g:
                    dist = min(dist, abs(x) + abs(y))
                    length = min(length, l + g[x,y])
print dist, length
