maximum_rgb = {"red":12,"green":13,"blue":14}

# Returns True if game is possible
def check_game(game_str):
    rounds = game_str.strip().partition(": ")[2].split("; ")
    for round in rounds:
        colors = round.split(", ")
        for color in colors:
            if "red" in color and int(color.split(" ")[0]) > maximum_rgb["red"]: return False
            if "green" in color and int(color.split(" ")[0]) > maximum_rgb["green"]: return False
            if "blue" in color and int(color.split(" ")[0]) > maximum_rgb["blue"]: return False
    return True

sum = 0
with open("02-1/input.txt") as f:
    for idx, line in enumerate(f.readlines()):
        if check_game(line):
            sum += idx+1
print(sum)
