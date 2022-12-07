stack = []
sizes = []
res = 0
for l in open("input"):
    if l == "$ cd ..\n":
        s = stack.pop()
        if s <= 100000: res += s
        stack[-1] += s
        sizes.append(s)
    elif l.startswith("$ cd "):
        stack.append(0)
    elif l[0].isdigit():
        stack[-1] += int(l.split(" ", 1)[0])
while len(stack) > 1:
    s = stack.pop()
    if s <= 100000: res += s
    stack[-1] += s
    sizes.append(s)
print(res)
x = stack.pop() - 40000000
for s in sorted(sizes):
    if s >= x:
        print(s)
        break
