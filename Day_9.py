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
           