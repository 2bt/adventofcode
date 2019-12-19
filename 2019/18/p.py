import sys
sys.setrecursionlimit(100000)


g = open("input").read()
l = g.find("\n") + 1
keys = "".join(sorted(c for c in g if c.isalpha() and c.islower()))

visited = set()
queue = [(g.index("@"), "")]
for w in xrange(9999):
    queue2 = []
    for p, k in queue:
        for q in p+l, p-l, p-1, p+1:
            if g[q] == "#": continue
            if g[q].isupper() and g[q].lower() not in k: continue
            c = k
            if g[q].islower() and g[q] not in c:
                c = "".join(sorted(c + g[q]))
                if c == keys: break
            if (q, c) in visited: continue
            visited.add((q, c))
            queue2.append((q, c))
        if c == keys: break
    queue = queue2
    if c == keys: break
print w + 1


#if 0:
#    p = g.index("@")
#    g = list(g)
#    g[p] = g[p-1] = g[p+1] = g[p-l] = g[p+l] = "#"
#    g[p-1-l] = g[p-1+l] = g[p+1-l] = g[p+1+l] = "@"
#    visited = set()
#    queue = [((p-1-l, p-1+l, p+1-l, p+1+l), "")]
#    for w in xrange(9999):
#        queue2 = []
#        for ps, k in queue:
#            for i, p in enumerate(ps):
#                for q in p+l, p-l, p-1, p+1:
#                    if g[q] == "#": continue
#                    if g[q].isupper() and g[q].lower() not in k: continue
#                    c = k
#                    if g[q].islower() and g[q] not in c:
#                        print ps, k, w
#                        c = "".join(sorted(c + g[q]))
#                        if c == keys: break
#
#                    qs = ps[:i] + (q,) + ps[i + 1:]
#                    if (qs, c) in visited: continue
#                    visited.add((qs, c))
#                    queue2.append((qs, c))
#
#        queue = queue2
#        if c == keys: break
#    print w + 1
