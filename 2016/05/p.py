import md5
s = "reyedfim"

a = ""
for i in xrange(99999999):
	m = md5.new(s + str(i)).hexdigest()
	if m.startswith("00000"):
		a += m[5]
		print a
		if len(a) == 8: break

a = ["_"] * 8
for i in xrange(99999999):
	m = md5.new(s + str(i)).hexdigest()
	if m.startswith("00000"):
		p = int(m[5], 16)
		if p < 8 and a[p] == "_":
			a[p] = m[6]
			print "".join(a)
			if not "_" in a: break

