maximum_rgb = {"red":12,"green":13,"blue":14}
test = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
test2 = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"

# Returns True possible, or false else
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
indices = []
with open("02-1/input.txt") as f:
    for idx, line in enumerate(f.readlines()):
        if check_game(line):
            indices.append(idx+1)
            sum += idx+1
print(sum)
print(indices)