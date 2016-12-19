a = [c == "^" for c in open("in").read().strip()]
s = 0
for i in range(400000):
	s += len(a) - sum(a)
	a = [x==y!=z or x!=y==z for x, y, z in zip([0]+a, a, a[1:]+[0])]
print s
