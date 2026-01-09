import re
from functools import lru_cache

def part_one():
    data = open("input.txt").read().splitlines()
    shapes = [i for i in range(len(data)) if re.match(r"\d:", data[i])] # Find lines that start with a digit followed by a colon for the shapes
    global shape_dict
    shape_dict = {}
    valid_regions = 0

    for index in shapes:
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

        total_gifts = sum(len(shape_dict[i][0])*int(x) for i, x in enumerate(gifts) if int(x) > 0)
        print("Total gifts area:", total_gifts, "Region area:", width*height)
        if total_gifts > width * height:
            continue
        
        print("checking region:\n", data[region])
        valid_regions += check_gift(frozenset(), 0, 0, width, height, region)

    print("Number of valid regions:", valid_regions)

@lru_cache(maxsize=None)
def check_gift(placed_gifts_locations, gift_shape_index, gift_shape_placed, width, height, region):
    
    if gift_shape_index == len(gifts)-1 and gift_shape_placed == int(gifts[gift_shape_index]):
        return 1
    
    else:
        while gift_shape_placed == int(gifts[gift_shape_index]):
            if gift_shape_index == len(gifts)-1:
                return 1
            
            gift_shape_index += 1
            gift_shape_placed = 0


        for rotation in shape_dict[gift_shape_index]:
            for x in range(width):
                for y in range(height):
                    new_rotation = [(x+dx, y+dy) for dx, dy in rotation]

                    if any(
                        dx >= width or dy >= height or (dx,dy) in placed_gifts_locations
                        for dx,dy in new_rotation
                    ):
                        continue

                    new_placed_gifts_locations = placed_gifts_locations | frozenset(new_rotation)
                    if check_gift(new_placed_gifts_locations, gift_shape_index, gift_shape_placed+1, width, height, region) == 1:
                        return 1
                                
        return 0
                                
part_one()
