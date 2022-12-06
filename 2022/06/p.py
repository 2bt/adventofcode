for Q in 4, 14:
    s = ""
    for i, c in enumerate(open("input").read()):
        s = (c+s)[:Q]
        if len(set(s)) == Q:
            print(i + 1)
            break
