sol = 0
with open("01-1/input.txt") as f:
    for line in f.readlines():
        a, e = (0, len(line) - 1)
        while not line[a].isdigit():
            a += 1
        while not line[e].isdigit():
            e -= 1
        sol += int(line[a]+line[e])

print(sol)