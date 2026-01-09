import os

input_file = 'Day_Three_Input.txt'

if os.name == 'nt':
    _ = os.system('cls')

def Part_One():
    total = 0
    batteries = []
    with open(input_file, 'r') as file:
        batteries = file.readlines()

    for battery in batteries:
        battery = battery.strip()
        one, two = 0, 0
        one_idx = 0
        #print("battery", battery)

        for i, num in enumerate(battery[:-1]):
            int_num = int(num)
            
            if int_num > one:
                one = int_num
                one_idx = i
                #print("Found bigger int at " + str(int_num))
        
        for num in battery[one_idx+1:]:
            int_num = int(num)
            if int_num > two:
                two = int_num
        
        #print(int(str(one)+str(two)))
        total += int(str(one)+str(two))
    
    print(total)


def Part_Two():
    total = 0
    batteries = []
    with open(input_file, 'r') as file:
        batteries = file.readlines()

    for battery in batteries:
        battery = battery.strip()
        on_num, on_idx = [], []

        #print("\ntesting battery " + battery)

        for i in range(12):
            on_num.append("0")
            on_idx.append(0)
            arr = battery[:-11]

            if (i != 0):
                arr = battery[on_idx[i-1] + 1: -(12-i-1)]
            if (i == 11):
                arr = battery[on_idx[i-1] + 1:]
            
            for j, num in enumerate(arr):
                if int(num) > int(on_num[i]):
                    on_num[i] = num
                    if(i==0):
                        on_idx[i] = j
                    else:
                        on_idx[i] = j + on_idx[i-1] + 1
                    #print("greater found at " + on_num[i] +" " + str(on_idx[i]))

        num = ''
        for i in on_num:
            num = num + i
        
        #print("voltate is " + num)
        total+=int(num)
    
    print(total)

Part_Two()

        
