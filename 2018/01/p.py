l = list(map(int, open("input")))

print(sum(l))

s = 0
f = set()
while 1:
    for x in l:
        f.add(s)
        s += x
        if s in f:
            print(s)
            exit()
