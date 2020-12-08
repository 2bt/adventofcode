import functools
s1 = s2 = 0
for g in open("input").read().split("\n\n"):
    s1 += len(set(g) - {"\n"})
    s2 += len(functools.reduce(set.__iand__, map(set,g.split())))
print(s1, s2)
