def part_one():
    input = open('input.txt', 'r').readlines()
    total = 0
    
    for i in range(len(input[0])):
        operation = input[4][i]
        print(operation)
        if operation == '*':
            total += int(input[0][i]) * int(input[1][i]) * int(input[2][i]) * int(input[3][i])
        elif operation == '+':
            total += int(input[0][i]) + int(input[1][i]) + int(input[2][i]) + int(input[3][i])

    print(total)

def part_two():
    input = open('input.txt', 'r').readlines()
    input = [line.strip('\n') for line in input]
    operation = input[4].split()
    total = 0
    curr_operation = 0
    i = 0

    while i < len(input[0]):
        start_index = i
        end_index = i

        while end_index < len(input[0]):
            if input[0][end_index].isspace() and input[1][end_index].isspace() and input[2][end_index].isspace() and input[3][end_index].isspace():
                break
            end_index += 1

        numbers = [input[j][start_index:end_index] for j in range(4)]
        op = operation[curr_operation]
        num = 0

        for i in range(len(numbers[0])):
            if op == '*':
                if num == 0:
                    num = 1
                num *= int(numbers[0][i] + numbers[1][i] + numbers[2][i] + numbers[3][i])
            elif op == '+':
                num += int(numbers[0][i] + numbers[1][i] + numbers[2][i] + numbers[3][i])

        curr_operation += 1
        i = end_index + 1
        total += num

    print(total)

part_two()
