def part_one():
    data = open("input.txt").read().split("\n")
    square_sizes = []

    for i, coord_1 in enumerate(data):
        for coord_2 in data[i+1:]:
            x_1, y_1 = map(int, coord_1.split(","))
            x_2, y_2 = map(int, coord_2.split(","))
            square_sizes.append((abs(x_1 - x_2) + 1) * (abs(y_1 - y_2) + 1))
    
    ##print(max(square_sizes))

input = open("input.txt").read().strip().split("\n")
x = [int(i.split(",")[0]) for i in input]
y = [int(i.split(",")[1]) for i in input]
rows = {}

for i in range(len(x)): #track the edges formed by the coords
    i_next = (i+1) % len(x)

    if y[i] == y[i_next]: #its a row
        for j in range(min(x[i], x[i_next]), max(x[i], x[i_next])+1):
            if y[i] not in rows:
                rows[y[i]] = set()

            rows[y[i]].add(j)

    elif x[i] == x[i_next]: #its a column
        for j in range(min(y[i], y[i_next]), max(y[i], y[i_next])+1):
            if j not in rows:
                rows[j] = set()
                
            rows[j].add(x[i])

for key in rows: #sort the rows
    rows[key] = sorted(list(rows[key]))

rows = dict(sorted(rows.items()))

rows[int(1534)] = []

def part_two():
    for key, item in get_largest_square_list().items():
        x1, y1 = x[key[0]], y[key[0]]
        x2, y2 = x[key[1]], y[key[1]]
        valid = True
        swapped = False

        if (y1 < y2 and x1 < x2) or (y1 > y2 and x1 > x2): #top-left to bottom-right or bottom-right to top-left 
            if y2 < y1: #swap so always going top-left to bottom-right
                x1, y1, x2, y2 = x2, y2, x1, y1
                swapped = True

            curr = x1
            end = x2
            while curr < end:
                if curr+1 not in rows[y1]:
                    if curr in rows[y1+1] and curr!=x1:
                        valid = False
                        break
                    
                    if rows[y1][-1]==curr:
                        valid = False
                        break
                    
                    curr = rows[y1][rows[y1].index(curr)+1]
                    continue

                curr = get_next_tile(swapped, key = key, curr = curr, reverse = False, curr_y = y1)

            if not valid: continue

            curr = y1
            end = y2
            while curr < end and valid:
                if x1 not in rows[curr+1]:
                    if x1+1 in rows[curr] and curr!=y1:
                        valid = False
                        break
                    
                    valid = False
                    for row in rows.items():
                        if row[0]>curr and x1 in row[1]:
                            valid = True
                            curr = get_next_tile(swapped, key = key, curr = curr, reverse=False, curr_x = x1)
                            break
                else:
                    curr = get_next_tile(swapped, key = key, curr = curr, reverse=False, curr_x = x1)
            if not valid: continue

            curr = x2
            end = x1
            while curr > end:
                if curr-1 not in rows[y2]:
                    if curr in rows[y2-1] and curr!=x2:
                        valid = False
                        break
                    
                    if rows[y2][0]==curr:
                        valid = False
                        break
                    
                    curr = rows[y2][rows[y2].index(curr)-1]
                    continue
                curr = get_next_tile(swapped, key = key, curr = curr, reverse=True, curr_y = y2)

            if not valid: continue

            curr = y2
            end = y1
            while curr > end and valid:
                if x2 not in rows[curr-1]:
                    if x2-1 in rows[curr] and curr!=y2:
                        valid = False
                        break
                    
                    valid = False
                    for row in rows.items():
                        if row[0]<curr and x2 in row[1]:
                            valid = True
                            curr = get_next_tile(swapped, key = key, curr = curr, reverse=True, curr_x = x2)
                            break
                else:
                    curr = get_next_tile(swapped, key = key, curr = curr, reverse=True, curr_x = x2)

        else:
            if x2 < x1: #swap so always going top-right to bottom-left
                x1, y1, x2, y2 = x2, y2, x1, y1
                swapped = True
            curr = x1
            end = x2
            while curr < end:
                if curr+1 not in rows[y1]:
                    if curr in rows[y1-1] and curr!=x1:
                        valid = False
                        break
                    
                    if rows[y1][-1]==curr:
                        valid = False
                        break
                    
                    curr = rows[y1][rows[y1].index(curr)+1]
                    continue
                curr = get_next_tile(swapped, key = key, curr = curr, reverse=False, curr_y = y1)

            if not valid: continue

            curr = y1
            end = y2
            while curr > end and valid:
                if x1 not in rows[curr-1]:
                    if x1+1 in rows[curr] and curr!=y1:
                        valid = False
                        break
                    
                    valid = False
                    for row in rows.items():
                        if row[0]<curr and x1 in row[1]:
                            valid = True
                            curr = get_next_tile(swapped, key = key, curr = curr, reverse=True, curr_x = x1)
                            break
                else:
                    curr = get_next_tile(swapped, key = key, curr = curr, reverse=True, curr_x = x1)
            if not valid: continue

            curr = x2
            end = x1
            while curr > end:
                if curr-1 not in rows[y2]:
                    if curr in rows[y2+1] and curr!=x2:
                        valid = False
                        break
                    
                    if rows[y2][0]==curr:
                        valid = False
                        break
                    
                    curr = rows[y2][rows[y2].index(curr)-1]
                    continue
                curr = get_next_tile(swapped, key = key, curr = curr, reverse=True, curr_y = y2)

            if not valid: continue

            curr = y2
            end = y1
            while curr < end and valid:
                if x2 not in rows[curr+1]:
                    if x2-1 in rows[curr] and curr!=y2:
                        valid = False
                        break
                    
                    valid = False
                    for row in rows.items():
                        if row[0]>curr and x2 in row[1]:
                            valid = True
                            curr = get_next_tile(swapped, key = key, curr = curr, reverse=False, curr_x = x2)
                            break
                else:
                    curr = get_next_tile(swapped, key = key, curr = curr, reverse=False, curr_x = x2)

        if valid: 
            print(item)
            return

def get_largest_square_list():
    square_sizes = {}

    for i, coord_1 in enumerate(input):
        for j, coord_2 in enumerate(input[i+1:]):
            x_1, y_1 = map(int, coord_1.split(","))
            x_2, y_2 = map(int, coord_2.split(","))
            square_sizes[(i,j+i+1)] = (abs(x_1 - x_2) + 1) * (abs(y_1 - y_2) + 1)

    square_sizes = dict(sorted(square_sizes.items(), key=lambda item: item[1], reverse=True))
    return square_sizes

def get_next_tile(swapped, key, curr, reverse, curr_y=None, curr_x=None):
    try:
        return_value = None
        if curr_x is not None:
            if swapped:
                return_value = y[key[1]+1] if x[key[1]+1] == curr_x else y[key[1]-1]
            else:
                return_value = y[key[0]+1] if x[key[0]+1] == curr_x else y[key[0]-1]
        if curr_y is not None:
            if swapped:
                return_value = x[key[1]+1] if y[key[1]+1] == curr_y else x[key[1]-1]
            else:
                return_value = x[key[0]+1] if y[key[0]+1] == curr_y else x[key[0]-1]

        #print("next tile is", return_value, "from", curr)

        if reverse and return_value < curr:
            return return_value
        elif not reverse and return_value > curr:
            return return_value
        else:
            raise IndexError
    except IndexError:
        if curr_x is not None and not reverse: #going down
            for row in rows.items():
                if row[0]>curr and curr_x in row[1]:
                    return row[0]
        elif curr_x is not None and reverse: #going up
            for row in reversed(rows.items()):
                if row[0]<curr and curr_x in row[1]:
                    return row[0]
        elif curr_y is not None and not reverse: #going right
            for col in rows[curr_y]:
                if col>curr:
                    return col
        elif curr_y is not None and reverse: #going left
            for col in reversed(rows[curr_y]):
                if col<curr:
                    return col
            
part_two()
