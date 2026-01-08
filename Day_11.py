from functools import lru_cache

def part_one():
    data = open("input.txt").read().strip().split("\n")
    global mappings
    mappings = {}
    paths = 0

    for line in data:
        mappings[line[0:3]] = line[5:].split(" ")

    for value in mappings['you']:
        paths += travel(value)

    print(paths)

@lru_cache(maxsize=None)
def travel(key):
    total = 0

    for value in mappings[key]:
        if value == 'out':
            return 1
        else:
            total += travel(value)

    return total

#part_one()

def part_two():
    data = open("input.txt").read().strip().split("\n")
    global mappings
    mappings = {}
    paths = 0

    for line in data:
        mappings[line[0:3]] = line[5:].split(" ")

    for value in mappings['svr']:
        paths += travel_2(value, False, False)

    print(paths)

@lru_cache(maxsize=None)
def travel_2(key, dac, fft):
    total = 0

    for value in mappings[key]:
        if value == 'out':
            if dac and fft:
                return 1
            else:
                return 0
        elif value == 'dac' and not dac:
            total += travel_2(value, True, fft)
        elif value == 'fft' and not fft:
            total += travel_2(value, dac, True)
        else:
            total += travel_2(value, dac, fft)

    return total

part_two()
