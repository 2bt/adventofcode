lines = open("input").readlines()
p = 0
for l in lines:
    s = len(l) // 2
    x = max(set(l[:s]) & set(l[s:]))
    p += ord(x) % 32 + x.isupper() * 26
print(p)

p = 0
while lines:
    x = max(set(lines.pop().strip()) & set(lines.pop()) & set(lines.pop()))
    p += ord(x) % 32 + x.isupper() * 26
print(p)
