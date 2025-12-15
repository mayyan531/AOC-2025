import os

file = 'Day_Two_Input.txt'

if os.name == 'nt':
    _ = os.system('cls')
# For macOS and Linux
else:
    _ = os.system('clear')

def Part_One():
    ids = []
    total = 0
    with open(file, 'r') as f:
        ids = f.read().strip().split(',')

    for id in ids:
        id.split('-')
        start = id.split('-')[0]
        end = id.split('-')[1]

        for i in range(int(start), int(end)+1):
            string_i = str(i)
            if len(string_i)%2==1:
                continue

            length = len(string_i)//2
            
            if string_i[:length] == string_i[length:]:
                total += i

    print(total)

def Part_Two():
    ids = []
    total = 0
    with open(file, 'r') as f:
        ids = f.read().strip().split(',')

    for id in ids:
        id.split('-')
        start = id.split('-')[0]
        end = id.split('-')[1]

        for y in range(int(start), int(end)+1):
            string_i = str(y)

            if (y<10):
                continue;

            #print("\n----------------testing for " + string_i)

            #print("\nchecking for all same")
            char_one = string_i[0]
            valid = False
            for char in string_i:
                if char!=char_one:
                    valid = True
                    break;
            
            if not valid:
                #print("repeated substring found: " + string_i)
                total += y
                continue

            #print("\nchecking for repeated substrings")
            for i in range(2, len(string_i)//2+1):
                #print("checking for substring length " + str(i))
                if (len(string_i)%i)!=0:
                    #print("not divisible")
                    continue

                substring = string_i[:i]
                valid = False
                #print("checking for substring " + substring)
                for j in range(i, len(string_i), i):
                    if string_i[j:j+i]!=substring:
                        valid = True
                        break;

                if not valid:
                    total += y
                    #print("repeated substring found: " + substring)
                    break;
                        

    print("\nfinal total is " + str(total))

Part_Two()