import sys
sys.setrecursionlimit(5000)
a = open("input").read()
W = a.find("\n") + 1
a += "\n" * W

def f(p, d):
    if (p, d) in v: return
    c = a[p]
    if c == "\n": return
    v.add((p, d))
    q = [d]
    if c == "\\": q = [{1:W,-W:-1,W:1,-1:-W}[d]]
    if c == "/":  q = [{1:-W,W:-1,-W:1,-1:W}[d]]
    if c == "-" and d in [W,-W]: q = [1,-1]
    if c == "|" and d in [1,-1]: q = [W,-W]
    for d in q: f(p + d, d)

v = set()
s = 0
def g(p, d):
    global s
    v.clear()
    f(p, d)
    s = max(s, len(set(x for x, _ in v)))

g(0, 1)
print(s)
for x in range(W - 1):
    g(x, W)
    g(x + (W-1)**2, -W)
    g(W * x, 1)
    g(W * x + W - 1, -1)
print(s)

