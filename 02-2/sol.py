def get_power(game_str):
    reds, greens, blues = (0,0,0)
    rounds = game_str.strip().partition(": ")[2].split("; ")
    for round in rounds:
        colors = round.split(", ")
        for color in colors:
            if "red" in color: reds = max(int(color.split(" ")[0]), reds)
            if "green" in color: greens = max(int(color.split(" ")[0]), greens)
            if "blue" in color: blues = max(int(color.split(" ")[0]), blues)
    return reds*greens*blues

sum = 0
with open("02-1/input.txt") as f:
    for line in f.readlines():
       sum += get_power(line)
print(sum)