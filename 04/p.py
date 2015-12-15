import hashlib

k = "yzbqklnj"

i = 1
while 1:
	i += 2
	m = hashlib.md5()
	m.update(k + str(i))
	v = m.digest().encode("hex")
	if v[:6] == "000000":
		print i

