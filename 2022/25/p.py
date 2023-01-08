x = 0
for l in open("input"):
    i = 0
    for c in l.strip(): i = i * 5 + "=-012".find(c) - 2
    x += i
r = ""
while x:
    d = x % 5
    x //= 5
    if d > 2: x += 1
    r = "012=-"[d] + r
print(r)
