a = open("input").read()
N = a.find("\n") + 1
a += "." * N

D = {
    ("-", 1) : 1,
    ("-",-1) :-1,
    ("|", N) : N,
    ("|",-N) :-N,
    ("L", N) : 1,
    ("L",-1) :-N,
    ("F",-N) : 1,
    ("F",-1) : N,
    ("7", 1) : N,
    ("7",-N) :-1,
    ("J", 1) :-N,
    ("J", N) :-1,
}

p = a.find("S")
d = 1
d = N
l = 0
w = set()
while 1:
    w.add(p)
    l += 1
    p += d
    c = a[p]
    if c == "S": break
    d = D[c, d]
print(l//2)

v = set()
def f(p):
    if p in w or p in v: return
    v.add(p)
    f(p + 1)
    f(p - 1)
    f(p + N)
    f(p - N)

d = N
while 1:
    f(p + {1:N, N:-1, -1:-N, -N:1}[d])
    p += d
    f(p + {1:N, N:-1, -1:-N, -N:1}[d])
    c = a[p]
    if c == "S": break
    d = D[c, d]
print(len(v))

