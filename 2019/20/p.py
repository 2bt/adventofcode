G = open("input").read()
W = G.find("\n") + 1
G += " " * W
H = len(G) // W

portals  = {}
connect  = {}
is_outer = {}

for p, c in enumerate(G):
    if not c.isalpha(): continue
    name = None
    if G[p + 1].isalpha():
        name = c + G[p + 1]
        pos  = p + 2 if G[p + 2] == "." else p - 1
        is_outer[pos] = abs(pos % W - W // 2 + 1) > H // 4
    elif G[p + W].isalpha():
        name = c + G[p + W]
        pos  = p + W*2 if G[p + W*2] == "." else p - W
        is_outer[pos] = abs(pos // W - H // 2 + 1) > H // 4
    if name:
        if name in portals:
            connect[pos] = portals[name]
            connect[portals[name]] = pos
        else: portals[name] = pos


for n in 0, 1:
    goal    = portals["ZZ"], 0
    queue   = [(portals["AA"], 0)]
    visited = set(queue)
    for i in range(1, 9999):
        queue, queue2 = [], queue
        for p, l in queue2:
            for q in p-1, p+1, p-W, p+W:
                if G[q] != ".": continue
                if (q, l) in visited: continue
                if (q, l) == goal: break
                visited.add((q, l))
                queue.append((q, l))
            if (q, l) == goal: break
            if p in connect:

                if n == 0:
                    queue.append((connect[p], l))
                else:
                    if not is_outer[p]: queue.append((connect[p], l + 1))
                    elif l > 0:         queue.append((connect[p], l - 1))

        if (q, l) == goal: break
    print(i)
