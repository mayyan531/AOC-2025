input_file = 'Day_Four_Input.txt'

def Part_One():
    total = 0
    lanes = []
    with open(input_file, 'r') as file:
        lanes = file.readlines()

    for num, lane in enumerate(lanes):
        lane = lane.strip()
        length = len(lane)
        #print("\nchecking for " + lane)

        for idx, roll in enumerate(lane):
            if roll != "@":
                continue;
            
            total += 1
            idx_to_check = []
            roll_adj = 0
            
            neighbors = [
                (num-1, idx-1),
                (num-1, idx),
                (num-1, idx+1),
                (num,   idx-1),
                (num,   idx+1),
                (num+1, idx-1),
                (num+1, idx),
                (num+1, idx+1)
            ]

            for r, c in neighbors:
                if (r < 0 or c < 0 or r>= len(lanes) or c>= length):
                    continue
                
                idx_to_check.append(lanes[r][c])
            
            #print("index " + str(idx))
            #print("checking " + str(idx_to_check))
            for index in idx_to_check:
                if index == "@":
                    roll_adj += 1

                if roll_adj == 4:
                    #print("too many adjacent")
                    total -= 1
                    break;
            #print(total)
    print(total)

def Part_Two():
    total = 0
    lanes = []
    removed = []
    with open(input_file, 'r') as file:
        input = file.readlines()

    for lane in input:
        lanes.append(list(lane.strip()))

    while True:
        #print(lanes)
        for num, lane in enumerate(lanes):
            length = len(lane)
            #print("\nchecking for " + lane)

            for idx, roll in enumerate(lane):
                if roll != "@":
                    continue;
                
                total += 1
                idx_to_check = []
                roll_adj = 0
                
                neighbors = [
                    (num-1, idx-1),
                    (num-1, idx),
                    (num-1, idx+1),
                    (num,   idx-1),
                    (num,   idx+1),
                    (num+1, idx-1),
                    (num+1, idx),
                    (num+1, idx+1)
                ]

                for r, c in neighbors:
                    if (r < 0 or c < 0 or r>= len(lanes) or c>= length):
                        continue
                    
                    idx_to_check.append(lanes[r][c])
                
                #print("index " + str(idx))
                #print("checking " + str(idx_to_check))
                for index in idx_to_check:
                    if index == "@":
                        roll_adj += 1

                    if roll_adj == 4:
                        total -= 1
                        break;
                
                if roll_adj != 4:
                    removed.append((num, idx))

        if len(removed) == 0:
            break
        else:
            for r,c in removed: lanes[r][c] = "."
            #print("lanes after a pass" + str(lanes))
        removed=[]
    print(total)


Part_Two()

