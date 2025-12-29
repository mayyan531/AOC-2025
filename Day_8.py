import itertools
from math import sqrt

def part_one():
    data = open("input.txt").read().split("\n")
    distances = {}
    connections = {i: 0 for i in data} #stores coord as key and set number as value
    sets = {}
    set_count = 1

    for i, j in itertools.combinations(data, 2):
        x_1, y_1, z_1 = map(int, i.split(","))
        x_2, y_2, z_2 = map(int, j.split(","))

        distance = sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2 + (z_1 - z_2)**2)
        distances[distance] = ( distance, i, j )

    for i in range(1000):
        smallest = min(distances.keys())
        distance, coord_1, coord_2 = distances.pop(smallest)

        if connections[coord_1] == 0 and connections[coord_2] == 0:
            connections[coord_1] = set_count
            connections[coord_2] = set_count
            sets[set_count] = {coord_1, coord_2}
            set_count += 1

        elif connections[coord_1] != 0 and connections[coord_2] == 0:
            set_id = connections[coord_1]
            connections[coord_2] = set_id
            sets[set_id].add(coord_2)

        elif connections[coord_2] != 0 and connections[coord_1] == 0:
            set_id = connections[coord_2]
            connections[coord_1] = set_id
            sets[set_id].add(coord_1)
            
        else:
            if connections[coord_1] != connections[coord_2]:
                set_id_1 = connections[coord_1]
                set_id_2 = connections[coord_2]

                for coord in sets[set_id_2]:
                    connections[coord] = set_id_1
                    sets[set_id_1].add(coord)
                
                del sets[set_id_2]
    
    set_lenghts = [len(v) for v in sets.values()]
    total = max(set_lenghts)
    set_lenghts.remove(max(set_lenghts))

    for i in range(2):
        total *= max(set_lenghts)
        set_lenghts.remove(max(set_lenghts))

    print(total)

def part_two():
    data = open("input.txt").read().split("\n")
    distances = {}
    connections = {i: 0 for i in data} #stores coord as key and set number as value
    sets = {}
    set_count = 1

    for i, j in itertools.combinations(data, 2):
        x_1, y_1, z_1 = map(int, i.split(","))
        x_2, y_2, z_2 = map(int, j.split(","))

        distance = sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2 + (z_1 - z_2)**2)
        distances[distance] = ( distance, i, j )

    for i in range(len(distances)):
        smallest = min(distances.keys())
        distance, coord_1, coord_2 = distances.pop(smallest)

        if connections[coord_1] == 0 and connections[coord_2] == 0:
            connections[coord_1] = set_count
            connections[coord_2] = set_count
            sets[set_count] = {coord_1, coord_2}
            set_count += 1

        elif connections[coord_1] != 0 and connections[coord_2] == 0:
            set_id = connections[coord_1]
            connections[coord_2] = set_id
            sets[set_id].add(coord_2)

        elif connections[coord_2] != 0 and connections[coord_1] == 0:
            set_id = connections[coord_2]
            connections[coord_1] = set_id
            sets[set_id].add(coord_1)
            
        else:
            if connections[coord_1] != connections[coord_2]:
                set_id_1 = connections[coord_1]
                set_id_2 = connections[coord_2]

                for coord in sets[set_id_2]:
                    connections[coord] = set_id_1
                    sets[set_id_1].add(coord)
                
                del sets[set_id_2]

        if len(sets[next(iter(sets))]) == len(data):
            x_1, y_1, z_1 = map(int, coord_1.split(","))
            x_2, y_2, z_2 = map(int, coord_2.split(","))
            print(x_1*x_2)
            return

part_one()

