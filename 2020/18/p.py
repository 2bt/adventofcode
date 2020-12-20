
def f(s):
    t = s.pop()
    if t.isdigit():
        x = int(t)
    elif t == ")":
        x = f(s)
        s.pop()
    while s and s[-1] in "+*":
        o = s.pop()
        if o == "+": x += f(s)
        if o == "*": x *= f(s)
    return x

def g(s, l=0):
    t = s.pop()
    if t.isdigit():
        x = int(t)
    elif t == ")":
        x = g(s)
        s.pop()
    while s:
        o = s[-1]
        p = "*+".find(s[-1])
        if p < l: break
        s.pop()
        if o == "*": x *= g(s, p + 1)
        if o == "+": x += g(s, p + 1)
    return x

print(sum(f(list(l.strip().replace(" ", ""))) for l in open("input")))
print(sum(g(list(l.strip().replace(" ", ""))) for l in open("input")))
