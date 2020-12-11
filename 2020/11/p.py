for X in 0, 1:
    a = open("input").read() + " "*99
    w = a.find("\n") + 1
    while 1:
        b = ""
        for i, c in enumerate(a):
            if c in "#L":
                n = [c == "#", 0][X]
                for d in [-w-1, -w, 1-w, -1, 1, w-1, w, w+1]:
                    p = i + d
                    while X and a[p] == ".": p += d
                    n += a[p] == "#"
                b += "L#"[n == 0 if c == "L" else n <= 4]
            else: b += c;
        if a == b: break
        a = b
    print(a.count("#"))
