from functools import lru_cache

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

data = open("input.txt").read().split("\n")
data = [list(line) for line in data]

def part_two():
    for i in range(len(data[2])):
        if data[2][i] == '^':
            start = i
            break

    print(travel(2, start-1) + travel(2, start+1))

@lru_cache(None)
def travel(current_row, curr_index):
    if current_row >= len(data) - 1:
        return 1
    
    else:
        for i, row in enumerate(data[current_row+1:]):
            if row[curr_index] == '^':
                return travel(i+current_row+1, curr_index-1) + travel(i+current_row+1, curr_index+1)
    
    return 1

part_two()
