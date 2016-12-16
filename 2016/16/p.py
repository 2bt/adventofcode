a = "10111100110001111"
#l = 272
l = 35651584
while len(a) < l: a += "0" + "".join("10"[c == "1"] for c in a)[::-1]
a = a[:l]
while len(a) % 2 == 0: a = ["01"[a[i] == a[i + 1]] for i in range(0, len(a), 2)]
print "".join(a)
