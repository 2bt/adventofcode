import string
from queue import PriorityQueue

UPPER = set(map(ord, string.ascii_uppercase))
LOWER = set(map(ord, string.ascii_lowercase))
WALL  = ord("#")
START = ord("@")

g = bytearray(open("input", "rb").read())
L = g.find(10) + 1
keys = sum(1 << (c - 97) for c in g if c in LOWER)

def reachable_keys(p, k):
    queue = [p]
    visited = set(queue)
    for w in range(1, 9999):
        queue2 = queue
        queue = []
        for p in queue2:
            for q in p+L, p-L, p-1, p+1:
                if q in visited: continue
                c = g[q]
                if c == WALL: continue
                if c in UPPER and ((1 << (c - 65)) & k) == 0: continue
                if c in LOWER and ((1 << (c - 97)) & k) == 0:
                    yield q, w
                    continue
                visited.add(q)
                queue.append(q)

for n in 0, 1:
    queue = PriorityQueue()
    visited = {}

    if n:
        p = g.find(b".@.")
        g[p-L:p-L+3] = b"@#@"
        g[p  :p  +3] = b"###"
        g[p+L:p+L+3] = b"@#@"
        queue.put((0, (p-L, p-L+2, p+L, p+L+2), 0))
    else:
        queue.put((0, (g.find(b"@"),), 0))

    while not queue.empty():
        w, ps, ks = queue.get()
        if visited.get((ps, ks), w) < w: continue
        if ks == keys:
            print(w)
            break
        for i, p in enumerate(ps):
            for q, v in reachable_keys(p, ks):
                kk = ks | (1 << (g[q] - 97))
                pp = ps[:i] + (q,) + ps[i+1:]
                if (pp, kk) not in visited or visited[pp, kk] > w + v:
                    queue.put((w + v, pp, kk))
                    visited[pp, kk] = min(w + v, visited.get((pp, kk), w + v))
