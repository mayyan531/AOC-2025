import itertools
import re
from functools import lru_cache

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
presses = []
buttons_with_this_counter = []
combination_to_make_counter = []

def part_two():
    total_presses = 0
    data = open("input.txt").read().strip().split("\n")
    buttons = [[re.sub(r'^[(]|[)]$', '', b).split(',') for b in part] for part in (line.split(' {')[0].split("] ")[-1].split() for line in data)] #splitting the buttons then removing () then splitting into lists by ,
    joltages = [[int(i) for i in line.split(' {')[-1].strip('}').split(',')] for line in data]

    for joltage, button_set in zip(joltages, buttons):
        print("\nJoltage set:", joltage)
        for counter in range(len(joltage)):
            buttons_with_this_counter.append([idx for idx, num in enumerate(button_set) if str(counter) in num])

        for i, avail_buttons in enumerate(buttons_with_this_counter):
            jolt = joltage[i] 
            combinations = []

            for combo in itertools.combinations_with_replacement(avail_buttons, jolt):
                combinations.append(list(combo))

            combination_to_make_counter.append(combinations)
        
        #print(combination_to_make_counter)

        for combo in combination_to_make_counter[0]:
            determine_valid(tuple(combo), 1)

        total_presses += min(presses)
        presses.clear()
        buttons_with_this_counter.clear()
        combination_to_make_counter.clear()
    return total_presses

@lru_cache(maxsize=None)
def determine_valid(current_combo, counter_number):
    current_combo = list(current_combo)
    #print("\niteration:", counter_number, "current combo:", current_combo)
    if counter_number == len(combination_to_make_counter):
        #print("  valid combo found:", current_combo)
        presses.append(len(current_combo))
        return

    for combo in combination_to_make_counter[counter_number]:
        #print("considering combo:", combo)
        valid = True
        new_combo = current_combo.copy()
        for button in combo:
            if button not in new_combo:
                new_combo.append(button)
            else:
                b = sum(1 for r in combo if r == button)
                c = sum(1 for r in new_combo if r == button)
                if b > c:
                    for _ in range(b - c):
                        new_combo.append(int(button))

        #print("  checking combo", new_combo)

        for i in range(counter_number):
            jolt = len(combination_to_make_counter[i][0])
            if sum(1 for b in new_combo if b in buttons_with_this_counter[i]) > jolt:
                #print("    invalid combo, too many buttons for counter", i ,"needed:", jolt, "found:", sum(1 for b in new_combo if b in buttons_with_this_counter[i]))
                valid = False
                break

        if valid:
            determine_valid(tuple(new_combo), counter_number+1)

print(part_two())
