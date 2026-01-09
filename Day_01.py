input_file = 'Day_One_Input.txt' 

def main():
    passwords = []
    ans = 0
    curr = 50
    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        passwords.append(line)

    for password in passwords:
        if password[0] == 'L':
            if curr == 0:
                ans -= 1

            number = int(password[1:])
            ans += number//100

            if number%100>curr:
                curr = 100 - (number%100 - curr)
                ans += 1
            else:
                curr -= number%100
                if curr == 0:
                    ans += 1

        elif password[0] == 'R':
            number = int(password[1:])
            curr += number

            while (curr > 99):
                curr = curr - 100
                ans = ans + 1
                
        """ print ("\n" +password)
        print (curr)
        print (ans) """

    print (ans)

main()