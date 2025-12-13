def part_one():
   input = open('input.txt', 'r').readlines()
   sepertation = input.index('\n')
   ranges = input[:sepertation]
   items = input[sepertation + 1:]
   fresh = {}
   num_fresh = 0
   for r in ranges:
       r = r.strip().split('-')
       start = int(r[0])
       end = int(r[1])
       #print("\nfor range" + r[0] + "-" + r[1])
       #print( start, end)
       fresh[start] = end
   for item in items:
       print("\nfor item " + item.strip())
       for start in fresh:
           print("checking range " + str(start) + "-" + str(fresh[start]))
           if int(item.strip()) >= start and int(item.strip()) <= fresh[start]:
               print("item " + item.strip() + " is fresh")
               num_fresh += 1
               break
   print(num_fresh)
part_one()