import math
for a in [
    list(zip(*[map(int, l.split()[1:]) for l in open("input")])),
    [[int(l.split(":")[1].replace(" ", "")) for l in open("input")]]
]:
    s = 1
    for m, n in a:
        x1 = m/2 - (m*m/4 - (n+1)) ** 0.5
        x2 = m/2 + (m*m/4 - (n+1)) ** 0.5
        s *= math.floor(x2) - math.ceil(x1) + 1
    print(s)
