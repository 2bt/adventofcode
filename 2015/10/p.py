a = "1113222113"
#for _ in range(50):
#	s = ""
#	i = 0
#	while i < len(a):
#		c = a[i]
#		n = 0
#		while i < len(a) and c == a[i]: i += 1; n += 1
#		s += `n` + c
#	a = s
#print len(a)


import re
for _ in range(50):
	a="".join(`len(i)`+i[0]for i in re.findall("1+|2+|3+",a))
print len(a)
