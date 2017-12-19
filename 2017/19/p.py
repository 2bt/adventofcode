a = open("input").read()

w = a.find("\n") + 1
p = a.find("|")
d = w
s = ""
l = -1
while 1:
	l += 1
	c = a[p]
	if c == "+":
		for e, k in (1,"-"), (-1,"-"), (w,"|"), (-w,"|"):
			if e == -d: continue
			if a[p + e] == k:
				d = e
				break
	elif c == " ": break
	elif c not in "|-": s += c
	p += d
print s
print l
