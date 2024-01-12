G = open("input").read()
W = G.find("\n") + 1
G += "#" * W
T = G.rfind(".")

import sys
sys.setrecursionlimit(50000)

l = 0
v = [0] * len(G)
def f(p):
    if v[p] or G[p] == "#": return
    if p == T:
        global l
        l = max(l, sum(v))
        return
    v[p] = 1
    for d in {
        ".": [1, W, -1, -W],
        ">": [1],
        "v": [W],
        "<": [-1],
        "^": [-W],
    }[G[p]]: f(p + d)
    v[p] = 0

f(1)
print(l)
