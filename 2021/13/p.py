f = open("input")
p = set()
for l in f:
    if not l.strip(): break
    p.add(tuple(map(int, l.split(","))))

for i, l in enumerate(f):
    v = int(l[13:])
    p = {(2 * v - x if l[11] == "x" and x > v else x,
          2 * v - y if l[11] == "y" and y > v else y) for x, y in p}
    if i == 0: print(len(p))

mx, my = map(max, zip(*p))
for y in range(my + 1): print("".join(" #"[(x, y) in p] for x in range(mx + 1)))
