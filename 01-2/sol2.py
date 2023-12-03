nums = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

def get_value(input_str):
    first_index = 10000
    last_index = 10000
    first_num = None
    last_num = None

    #first
    for key in nums.keys():
        idx = input_str.find(key)
        if idx !=-1 and idx < first_index:
            first_index = idx
            first_num = nums[key]
    #last
    for key in nums.keys():
        idx = input_str[::-1].find(key[::-1])
        if idx !=-1 and idx < last_index:
            last_index = idx
            last_num = nums[key]

    # Now check for letter words around the two digits ( if there are none, check everything ) Regex again probably better
    for i, letter in enumerate(input_str[0:first_index]):
        if letter.isdigit(): 
            first_index = i
            first_num = int(letter)
            break
    for i, letter in enumerate(input_str[::-1]):
        if letter.isdigit() and last_index > i: 
            last_index = len(input_str) - i - 1
            last_num = int(letter)
            break

    return str(first_num) + str(last_num)



def solve():
    summe = 0
    with open("01-2/input.txt") as f:
        for line in f.readlines():
            val = int(get_value(line.strip()))
            print(val)
            summe += val
    return summe


print(solve()) # Richtig!