import heapq
a = open("input").read()
W = a.find("\n") + 1
T = len(a) - 2
a += "\n" * W
def F(MI, MA):
    v = set()
    u = [(0, 0, 0, 0), (0, 0, 0, 1)]
    while u:
        s, p, l, d = heapq.heappop(u)
        if p == T:
            print(s)
            break
        pp = p + [1,W,-1,-W][d]
        if a[pp] == "\n": continue
        ss = s + int(a[pp])
        def f(ll, dd):
            ee = pp, ll, dd
            if ee in v: return
            v.add(ee)
            heapq.heappush(u, (ss, pp, ll, dd))
        if l < MA:
            f(l + 1, d)
        if l >= MI:
            f(0, (d + 1) % 4)
            f(0, (d + 3) % 4)
F(0, 2)
F(3, 9)
