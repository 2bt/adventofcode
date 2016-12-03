s = 0
for l in open("in"):
	w = map(int, l.split())
	s += all(w[i] < sum(w[:i]+w[i+1:]) for i in range(3))
print s


s = 0
w = sum(zip(*[map(int, l.split()) for l in open("in")]), ())
while w:
	s += all(w[i] < sum(w[:i]+w[i+1:3]) for i in range(3))
	w = w[3:]
print s
