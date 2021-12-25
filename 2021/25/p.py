a = [list(l.strip()) for l in open("input")]
H = len(a)
W = len(a[0])
b = [[" "] * W for _ in range(H)]
i = 0
move = True
while move:
    i += 1
    move = False
    for y in range(H):
        for x in range(W):
            if a[y][x] == "." and a[y][x - 1] == ">":
                move = True
                b[y][x] = ">"
            elif a[y][x] == ">" and a[y][(x + 1) % W] == ".":
                b[y][x] = "."
            else:
                b[y][x] = a[y][x]
    a, b = b, a
    for y in range(H):
        for x in range(W):
            if a[y][x] == "." and a[y - 1][x] == "v":
                move = True
                b[y][x] = "v"
            elif a[y][x] == "v" and a[(y + 1) % H][x] == ".":
                b[y][x] = "."
            else:
                b[y][x] = a[y][x]
    a, b = b, a
print(i)
