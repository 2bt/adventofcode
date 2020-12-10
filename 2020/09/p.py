a = list(map(int,open("input")))
for i in range(len(a)):
    p = sorted(a[i:i + 25])
    x = a[i + 25]
    if all(v + w != x for w in p for v in p): break
print(x)

s = i = j = 0
while s != x:
    if s < x: s += a[j]; j += 1
    if s > x: s -= a[i]; i += 1
print(min(a[i:j]) + max(a[i:j]))
