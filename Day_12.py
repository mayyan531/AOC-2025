import re
from functools import lru_cache

def part_one():
    data = open("input.txt").read().splitlines()
    shapes = [i for i in range(len(data)) if re.match(r"\d:", data[i])] # Find lines that start with a digit followed by a colon for the shapes
    global shape_dict
    shape_dict = {}
    valid_regions = 0
    ##print(data)

    for index in shapes:
        #print(f"Shape found at line {index}: {data[index]}")
        shape = []
        matrix = []

        for i in range(index + 1, index+4):
            shape = [*shape, *[(i - index-1, y) for y, char in enumerate(data[i]) if char == '#']]
            matrix.append(list(data[i]))
        
        shape_dict[int(data[index].strip(":"))] = [shape]

        for i in range(3):
            shape = []
            new_matrix = []
            for col in range(3):
                shape = [*shape, *[(col, j) for j in range(3) if matrix[2-j][col] == '#']]
                new_matrix.append([matrix[j][col] for j in range(2, -1, -1)])

            matrix = new_matrix
            shape_dict[int(data[index].strip(":"))].append(shape)

    for region in [i for i in range(shapes[-1], len(data)) if re.match(r"\d*x\d*:", data[i])]:
        global gifts
        gifts = data[region].split(":")[1].strip().split(" ")
        width, height = map(int, re.match(r"(\d*)x(\d*):", data[region]).groups())
        
        #print("\nchecking region:", data[region])
        valid_regions += check_gift(frozenset(), 0, 0, width, height)

    print("Number of valid regions:", valid_regions)

@lru_cache(maxsize=None)
def check_gift(placed_gifts_locations, gift_shape_index, gift_shape_placed, width, height):
    #print(f"Checking gift shape index {gift_shape_index} with {gift_shape_placed} placed so far. Current placements: {placed_gifts_locations}")
    if gift_shape_index == len(gifts)-1 and gift_shape_placed == int(gifts[gift_shape_index]):
        #print("  valid arrangement found with placements:", placed_gifts_locations)
        return 1
    
    else:
        while gift_shape_placed == int(gifts[gift_shape_index]):
            if gift_shape_index == len(gifts)-1:
                #print("  valid arrangement found with placements:", placed_gifts_locations)
                return 1
            
            #print("Moving to next gift shape")
            gift_shape_index += 1
            gift_shape_placed = 0


        for rotation in shape_dict[gift_shape_index]:
            #print(f"\nTrying rotation for gift shape {gift_shape_index}: {rotation}")
            for x in range(width):
                for y in range(height):
                    #print(f"Trying to place gift shape {gift_shape_index} rotation at ({x},{y})")
                    new_rotation = [(x+dx, y+dy) for dx, dy in rotation]

                    #print("  New placed gifts locations:", new_placed_gifts_locations)

                    if any(
                        dx >= width or dy >= height or (dx,dy) in placed_gifts_locations
                        for dx,dy in new_rotation
                    ):
                        continue

                    new_placed_gifts_locations = placed_gifts_locations | frozenset(new_rotation)
                        #print("  Placement valid, continuing to next placement\n")
                    if check_gift(new_placed_gifts_locations, gift_shape_index, gift_shape_placed+1, width, height) == 1:
                        return 1
                        
                    #print("  Placement invalid, trying next position")
        
        #print("No valid placements found for this configuration \n")
        return 0
                                
part_one()
