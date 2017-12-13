d = {}
for l in open("input"):
	a, b = l.split("<->")
	d[int(a)] = map(int, b.split(","))

def f(x, v):
	if x in v: return
	v.add(x)
	for k in d[x]: f(k, v)
	return v

print len(f(0, set()))

c = 0
w = set()
for x in d:
	if x in w: continue
	c += 1
	w |= f(x, set())
print c
