f = open("input")
numbers = list(map(int, f.readline().split(",")))
boards  = [list(map(int, b.split())) for b in f.read().split("\n\n")]
def f(b):
    for i, n in enumerate(numbers):
        b = [[x, 100][x==n] for x in b]
        if any(sum(b[x::5]) == 500 or sum(b[x * 5:][:5]) == 500 for x in range(5)):
            return i, sum(x % 100 for x in b) * n
scores = sorted(map(f,boards))
print(scores[0][1])
print(scores[-1][1])
