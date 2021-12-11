import re, collections

a = collections.defaultdict(int)
for l in open("input"):
    i, x, y, w, h = map(int, re.findall(r"\d+", l))
    for u in range(x, x + w):
        for v in range(y, y + h): a[u, v] += 1
print(sum(x > 1 for x in a.values()))

for l in open("input"):
    i, x, y, w, h = map(int, re.findall(r"\d+", l))
    if all(a[u, v] == 1 for u in range(x, x + w) for v in range(y, y + h)):
        print(i)
        break
