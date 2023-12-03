import string
s1 = s2 = 0
digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for l in open("input"):
    l = l.strip()
    q = [int(x) for x in l if x.isdigit()]
    s1 += q[0] * 10 + q[-1]
    for i, d in enumerate(digits): l = l.replace(d, d[0] + str(i) + d[-1])
    q = [int(x) for x in l if x.isdigit()]
    s2 += q[0] * 10 + q[-1]
print(s1, s2)
