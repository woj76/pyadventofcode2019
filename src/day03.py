part2 = True

def createpath(directions):
    path = {}
    x = y = d = 0
    for (dir, steps) in directions:
        for _ in range(steps):
            if dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            elif dir == 'U':
                y += 1
            elif dir == 'D':
                y -= 1
            d += 1
            path[(x,y)] = d
    return path

file = open("data/data03.txt", "rt")

path1 = createpath([(x[:1], int(x[1:])) for x in file.readline()[:-1].split(',')])
path2 = createpath([(x[:1], int(x[1:])) for x in file.readline()[:-1].split(',')])

distance = float('inf')

for p in path1.keys() & path2.keys():
    if part2:
        distance = min(distance, path1[p] + path2[p])
    else:
        (x,y) = p
        distance = min(distance, abs(x) + abs(y))

print(distance)
