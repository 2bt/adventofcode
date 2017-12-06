a = map(int, open("input").read().split())
d = set()
c = 0
while 1:
	t = tuple(a)
	if t in d: break
	d.add(t)
	i = max(range(16), key=lambda x: a[x])
	s, a[i] = a[i], 0
	for j in range(16): a[(i + j + 1) % 16] += s / 16 + (j < s % 16)
	c += 1
print c
c = 0
while 1:
	i = max(range(16), key=lambda x: a[x])
	s, a[i] = a[i], 0
	for j in range(16): a[(i + j + 1) % 16] += s / 16 + (j < s % 16)
	c += 1
	if tuple(a) == t: break
print c
