s1 = 0
m = []
for l in open("input").readlines()[::-1]:
    w = l.split()
    x = len(set(w[2:12]) & set(w[13:]))
    s1 += (1 << x) // 2
    m = [1 + sum(m[:x])] + m
print(s1, sum(m))
