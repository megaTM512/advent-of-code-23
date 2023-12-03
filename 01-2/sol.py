nums = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

test = "oneight"

def get_value(input_str):
    first_num = None
    last_num = None
    a_index, e_index = (0, len(input_str) - 1)

    #Digits
    for i, letter in enumerate(input_str):
        if letter.isdigit(): 
            a_index = i
            break
    for i, letter in enumerate(input_str[::-1]):
        if letter.isdigit(): 
            e_index = len(input_str) - i - 1
            break
    first_num, last_num = (input_str[a_index],input_str[e_index])

    #Three Window
    first_str, last_str, a_index, e_index = two_side_sliding_window(input_str,3, a_index, e_index)
    if first_str: first_num = nums[first_str]
    if last_str:  last_num = nums[last_str]
            
    #Four Window
    first_str, last_str, a_index, e_index = two_side_sliding_window(input_str,4, a_index, e_index)
    if first_str: first_num = nums[first_str]
    if last_str:  last_num = nums[last_str]
    #Five Window
    first_str, last_str, a_index, e_index = two_side_sliding_window(input_str,5, a_index, e_index)
    if first_str: first_num = nums[first_str]
    if last_str:  last_num = nums[last_str]
    print(f"{input_str} : {first_num} + {last_num}")
    return str(first_num) + str(last_num)


def two_side_sliding_window(input_str, size, to1, from2):
    first_string = None
    last_string = None
    a_new , e_new = (0, len(input_str))
    while a_new + size <= to1:
        if input_str[a_new:a_new + size] in nums.keys():
            first_string = input_str[a_new:a_new + size]
            break
        a_new += 1
    while e_new - size >= from2:
        debu = input_str[e_new - size:e_new]
        if input_str[e_new - size:e_new] in nums.keys():
            last_string = input_str[e_new - size:e_new]
            break
        e_new -= 1
    if not first_string: a_new = to1
    if not last_string: e_new = from2
    return (first_string,last_string, a_new, e_new)

sum = 0


def solve():
    with open("01-2/input.txt") as f:
        for line in f.readlines():
            val = int(get_value(line.strip()))
            print(val)
            sum += val

print(get_value(test))

#print(sum) # 53186 too low