a = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"


s = set()
for l in file("in"):
	k, _, v = l.split()
	i = 0
	while 1:
		i = a.find(k, i)
		if i < 0: break
		s.add(a[:i] + v + a[i + len(k):])
		i += 1
print len(s)



r = [l.split()[::2] for l in file("in")]
m = 999
def f(s, c):
	if s == "e":
		global m
		if c < m:
			m = c
			print m
		return
	for k, v in r:
		i = 0
		while 1:
			i = s.find(v, i)
			if i < 0: break
			f(s[:i] + k + s[i + len(v):], c+1)
			i += 1
f(a, 0)
