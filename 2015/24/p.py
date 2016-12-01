W = map(int, file("in"))[::-1]
#T = sum(W) / 3
T = sum(W) / 4

def can_split(w, s=0):
	if s >= T: return s == T
	for i in range(len(w)):
		if can_split(w[:i+1], s + w[i]): return True
	return False


ll = 9e9
pp = 9e9

def f(v, w, l=0, s=0, p=1):
	global ll, pp
	if s > T: return
	if l > ll: return
	if l == ll and p > pp: return
#	if s == T and can_split([x for x in W if x not in v]):
	if s == T:
		ll = l
		pp = p
		print pp
		return

	for i in range(len(w)):
		f(v + [w[i]], w[i+1:], l + 1, s + w[i], p * w[i])

f([], W)

print pp
