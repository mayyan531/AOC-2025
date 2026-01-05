import re

def part_one():
    data = open("input.txt").read().strip().split("\n")
    diagrams = [list(line.split("]")[0].strip("[")) for line in data]
    buttons = [[re.sub(r'^[(]|[)]$', '', b).split(',') for b in part] for part in (line.split(' {')[0].split("] ")[-1].split() for line in data)] #splitting the buttons then removing () then splitting into lists by ,

    number_of_presses = 0

    for diagram, button in zip(diagrams, buttons):#if is . req even pushes if # req odd pushes
        button_state = {"-1": {idx: True if i == '.' else False for idx, i in enumerate(diagram)}}
        next_button_state = {}
        found = False
        presses = 0

        while (found is False and presses < len(button)):
            presses += 1

            for key, value in button_state.items():
                if presses == 1:
                    start_idx = 0
                else:
                    start_idx = int(key[-1])+1

                for idx, b in enumerate(button[start_idx:]):
                    new_state = value.copy()

                    for part in b:
                        new_state[int(part)] = not new_state[int(part)]
                    
                    if list(new_state.values()).count(False) == 0:
                        number_of_presses += presses
                        found = True
                        break
                    else:
                        next_button_state[key + str(idx+start_idx)] = new_state.copy()

                if found:
                    break

            button_state = next_button_state.copy()
    
    return number_of_presses

#print(part_one())

def part_two():
    data = open("input.txt").read().strip().split("\n")
    buttons = [[re.sub(r'^[(]|[)]$', '', b).split(',') for b in part] for part in (line.split(' {')[0].split("] ")[-1].split() for line in data)] #splitting the buttons then removing () then splitting into lists by ,
    joltages = [[int(i) for i in line.split(' {')[-1].strip('}').split(',')] for line in data]

    for joltage, button_set in zip(joltages, buttons):
        buttons_with_this_counter = []

        for counter in range(len(joltage)):
            buttons_with_this_counter.append([idx for idx, num in enumerate(button_set) if str(counter) in num])

        for i in range(1, len(bu))

print(part_two())
