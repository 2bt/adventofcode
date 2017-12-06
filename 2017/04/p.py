i = j = 0
for l in open("input"):
	l = l.split()
	i += len(set(l)) == len(l)
	j += len(set(["".join(sorted(x)) for x in l])) == len(l)
print i
print j
