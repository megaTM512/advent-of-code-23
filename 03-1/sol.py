engine = []
symbols = [] # (x,y) Coordinates
numbers = [] # (number, x, y, lenght)

# Import Engine
with open("03-1/input.txt") as engine_txt:
    for row in engine_txt:
        engine.append(row.strip())

# Get all Symbol Coordinates
for y,row in enumerate(engine):
    for x, col in enumerate(row):
        if not col.isdigit() and col != ".":
            symbols.append((x,y))

# Get all Numbers
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
# Check all Numbers
sum = 0
for num in numbers:
    x_low, y_low = max(0, num[1] - 1), max(0, num[2] - 1)
    x_high, y_high = min(len(engine[0])-1, num[1] + len(num[0])), min(len(engine)-1, num[2] + 1)
    for symbol in symbols:
        if symbol[0] >= x_low and symbol[0] <= x_high and symbol[1] >= y_low and symbol[1] <= y_high:
            sum += int(num[0])
            break
print(sum) #542588 to high