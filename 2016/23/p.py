def op(x): return ([0, 1, 2, 3, x]["abcd".find(x)], x in "abcd")
for l in open("in"):
	w = l.split()
	if len(w) == 2:
		print "{ %s, %s, %d }," % ((w[0],) + op(w[1]))
	else:
		print "{ %s, %s, %d, %s, %d }," % ((w[0],) + op(w[1]) + op(w[2]))
