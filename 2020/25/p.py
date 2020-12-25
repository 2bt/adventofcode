N = 20201227
X, Y = map(int, open("input"))

def loop_size(p):
    s, x = 0, 1
    while x != p:
        x = (x * 7) % N
        s += 1
    return s

sx = loop_size(X)
sy = loop_size(Y)

x = 1
for _ in range(sx): x = (x * Y) % N
print(x)
