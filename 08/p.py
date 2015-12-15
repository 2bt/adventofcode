print sum(len(l.strip()) - len(eval(l)) for l in file("in"))



def f(l):
	s = 2
	for c in l:
		if c == '"': s += 2
		elif c == "\\": s += 2
		else: s += 1
	return s


print sum(f(l.strip()) - len(l.strip()) for l in file("in"))
