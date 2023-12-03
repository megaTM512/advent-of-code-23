engine = []
gears = [] # (x,y) Coordinates
numbers = [] # (number, x, y, lenght)

# Import Engine
with open("03-2/input.txt") as engine_txt:
    for row in engine_txt:
        engine.append(row.strip())

# Get all Gears
for y,row in enumerate(engine):
    for x, col in enumerate(row):
        if col == "*": gears.append((x,y))

# Get all Numbers / RegEx would be far easier, probably, kinda
in_num = False
num_x = None
num_y = None
num = ""
for y, row in enumerate(engine):
    for x, col in enumerate(row):
        if col.isdigit() and not in_num:
            in_num = True
            num_x, num_y = (x,y)
            num = col
        elif col.isdigit() and in_num:
            num += col
        elif not col.isdigit() and in_num:
            numbers.append((num,num_x,num_y,len(num)))
            in_num = False
    if in_num:
        numbers.append((num,num_x,num_y,len(num)))
        in_num = False

# Remove all non-part numbers
parts = []
for num in numbers:
    x_low, y_low = (max(0, num[1] - 1), max(0, num[2] - 1))
    x_high, y_high = (min(len(engine[0])-1, num[1] + len(num[0])), min(len(engine)-1, num[2] + 1))
    for gear in gears:
        if gear[0] >= x_low and gear[0] <= x_high and gear[1] >= y_low and gear[1] <= y_high:
            parts.append(num)
            break



# Create new Engine-Map with ref to parts
new_engine = [[None for x in range(len(engine[0]))] for y in range(len(engine))]
for part in parts:
    for l in range(part[3]):
        new_engine[part[2]][part[1]+l] = part



# Check every adjacent part of all gears
sum = 0
for gear in gears:
    adj_parts = []
    x_low, x_high = (max(0, gear[0] - 1), min(len(engine[0])-1, gear[0] + 1))
    y_low, y_high = (max(0, gear[1] - 1), min(len(engine)-1, gear[1] + 1))
    for row in new_engine[y_low:y_high+1]:
        for col in row[x_low:x_high+1]:
            print(col)
            if col: adj_parts.append(col)
    adj_parts = list(set(adj_parts))
    if len(adj_parts) == 2:
        sum += int(adj_parts[0][0]) * int(adj_parts[1][0])

print(sum)