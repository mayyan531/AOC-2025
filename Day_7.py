def part_one():
    data = open("input.txt").read().split("\n")
    data = [list(line) for line in data]

    left_found = False
    right_found = False

    for i, val in enumerate(data[2]):
        if val == '^':
            data[2][i] = 'X'
    
    for i, row in enumerate(data[0:-1]):
        if i < 2:
            continue

        for j, element in enumerate(row):
            left_found = False
            right_found = False
            if element == 'X':
                for k, row in enumerate(data[0:-1]):
                    if k <= i:
                        continue
                    if (row[j-1] == '^' or row[j-1] == "X") and not left_found:
                        left_found = True
                        data[k][j-1] = 'X'
                    if (row[j+1] == '^' or row[j+1] == "X") and not right_found:
                        right_found = True
                        data[k][j+1] = 'X'
                    if left_found and right_found:
                        break
                    
    print(sum(row.count('X') for row in data))

part_one()
