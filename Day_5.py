def part_one():
    input = open('input.txt', 'r').readlines()
    
    sepertation = input.index('\n')
    ranges = input[:sepertation]
    items = input[sepertation + 1:]

    fresh = {}

    for r in ranges:
        r = r.strip().split('-')
        start = int(r[0]) 
        end = int(r[1])
        if start in fresh:
            if end > fresh[start]:
                fresh[start] = end
        else:
            fresh[start] = end
    
    num_fresh = sum(1 for item in items if any(int(item.strip()) >= start and int(item.strip()) <= fresh[start] for start in fresh))

    print(num_fresh)

def part_two():
    input = open('input.txt', 'r').readlines()
    
    separation = input.index('\n')
    ranges = input[:separation]
    fresh = []
    
    for r in ranges:
        r = r.strip().split('-')
        start, end = int(r[0]), int(r[1])
        overlapping_ranges = []

        for i, r in enumerate(fresh):
            one, two = r
            if (start > two or end < one):
                continue
            else:
                overlapping_ranges.append((i, r))

        if overlapping_ranges != []:
            fresh = [r for i, r in enumerate(fresh) if i not in [i for i, _ in overlapping_ranges]]
            new_start = min(start, min(r[0] for i, r in overlapping_ranges))
            new_end = max(end, max(r[1] for i, r in overlapping_ranges))
            fresh.append((new_start, new_end))
        else:
            fresh.append((start, end))
        
        overlapping_ranges = []
    
    total = sum(end - start + 1 for start, end in fresh)
    print(total)

part_two()
