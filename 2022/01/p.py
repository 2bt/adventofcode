x = sorted(sum(map(int, x.split())) for x in open("input").read().split("\n\n"))
print(x[-1])
print(sum(x[-3:]))
