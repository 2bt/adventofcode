s1, s2 = [int(l.split()[-1]) for l in open("input")]
c = 0
for _ in xrange(40000000):
	s1 = s1 * 16807 % 2147483647
	s2 = s2 * 48271 % 2147483647
	c += s1 & 0xffff == s2 & 0xffff
print c

s1, s2 = [int(l.split()[-1]) for l in open("input")]
c = 0
for _ in xrange(5000000):
	while 1:
		s1 = s1 * 16807 % 2147483647
		if s1 & 0x3 == 0: break
	while 1:
		s2 = s2 * 48271 % 2147483647
		if s2 & 0x7 == 0: break
	c += s1 & 0xffff == s2 & 0xffff
print c
