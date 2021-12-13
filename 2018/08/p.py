from collections import namedtuple
Node = namedtuple('Node', 'kids meta')

a = iter(map(int, open("input").read().split()))
def f():
    k, m = next(a), next(a)
    return Node([f() for _ in range(k)], [next(a) for _ in range(m)])
root = f()

def meta_sum(n): return sum(n.meta) + sum(map(meta_sum, n.kids))
print(meta_sum(root))

def value(n):
    if not n.kids: return sum(n.meta)
    return sum(value(n.kids[k - 1]) for k in n.meta if 0 < k <= len(n.kids))
print(value(root))
