def part_one():
    data = open("input.txt").read().split("\n")
    square_sizes = []

    for i, coord_1 in enumerate(data):
        for coord_2 in data[i+1:]:
            x_1, y_1 = map(int, coord_1.split(","))
            x_2, y_2 = map(int, coord_2.split(","))
            square_sizes.append((abs(x_1 - x_2) + 1) * (abs(y_1 - y_2) + 1))
    
    print(max(square_sizes))

part_one()


input = open("input.txt").read().strip().split("\n")

def part_two():
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

    for key, item in get_largest_square_list().items():
        x1, y1 = x[key[0]], y[key[0]]
        x2, y2 = x[key[1]], y[key[1]]
        valid = True

        #check first coord
        if y1 < y2 and x1 < x2: 
            curr = x1
            end = x2
            while curr < end:
                if curr+1 not in rows[y1]:
                    if curr not in rows[y1-1]:
                        valid = False
                        break
                    
                    if rows[y1][-1]==curr:
                        valid = False
                        break
                    
                    curr = rows[y1][rows[y1].index(curr)+1]
                    continue
                curr += 1

            if not valid: continue

            curr = y1
            end = y2
            while curr < end:
                if curr+1 not in rows:

            if not valid: continue

            curr = x.index(x2)
            end = x.index(x1)
            while curr != end:
                if rows[y2][curr-1] != rows[y2][curr] - 1:
                    if curr not in rows[y1]:
                        valid = False
                        break
                curr -= 1




                

    """ for key in rows: #fill in the gaps
        gap = False
        rows[key] = sorted(list(rows[key]))
        to_add = []

        for i in range(len(rows[key]) - 1):
            if rows[key][i]+1 != rows[key][i+1] and not gap: #not sequential,its a gap or space inside
                gap = True
                for j in range(rows[key][i]+1, rows[key][i+1]):
                    to_add.append(j)

            if rows[key][i]+1 != rows[key][i+1] and gap:
                gap=False
                continue

            elif rows[key][i]+1 == rows[key][i+1] and not gap:
                start = i

                while start + 1 < len(rows[key]):
                    if rows[key][start]+1 == rows[key][start+1]:
                        start += 1
                    else:
                        break

                if start+2 < len(rows[key]) and rows[key][start+1]+1 == rows[key][start+2]: 
                    gap = True
                else:
                    gap = False

        rows[key].extend(to_add) """

def get_largest_square_list():
    square_sizes = {}

    for i, coord_1 in enumerate(input):
        for j, coord_2 in enumerate(input[i+1:]):
            x_1, y_1 = map(int, coord_1.split(","))
            x_2, y_2 = map(int, coord_2.split(","))
            square_sizes[(i,j+i+1)] = (abs(x_1 - x_2) + 1) * (abs(y_1 - y_2) + 1)

    square_sizes = dict(sorted(square_sizes.items(), key=lambda item: item[1], reverse=True))
    return square_sizes

get_largest_square_list()
