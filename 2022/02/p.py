s = 0
for l in open("input"):
    l = l.strip()
    s += ord(l[-1]) - ord("X") + 1
    if   l in { "A X", "B Y", "C Z" }: s += 3
    elif l in { "A Y", "B Z", "C X" }: s += 6
print(s)

s = 0
for l in open("input"):
    x, y = l.split()
    if   y == "X": s += { "A":3, "B":1, "C":2 }[x]
    elif y == "Y": s += { "A":1, "B":2, "C":3 }[x] + 3
    else:          s += { "A":2, "B":3, "C":1 }[x] + 6
print(s)
