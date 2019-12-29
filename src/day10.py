import math
import functools

def compare_slants(s1, s2):
    (dx1, dy1) = s1
    (dx2, dy2) = s2
    if dx1 == dx2 and dy1 == dy2:
        return 0
    elif dy1 < 0 and dx1 >= 0:
        if dy2 < 0 and dx2 >= 0 and 10000 * dx2 // dy2 > 10000 * dx1 // dy1:
            return 1
        return -1;
    elif dy1 >= 0 and dx1 > 0:
        if dy2 < 0 and dx2 >= 0:
            return 1
        if dy2 >= 0 and dx2 > 0 and 10000 * dy1 // dx1 > 10000 * dy2 // dx2:
            return 1
        return -1
    elif dy1 > 0 and dx1 <= 0:
        if dy2 <= 0 and dx2 < 0:
            return -1
        if dy2 > 0 and dx2 <= 0 and 10000 * dx2 // dy2 < 10000 * dx1 // dy1:
            return -1
        return 1
    else: # dy1 <= 0 and dx1 < 0
        if dy2 <= 0 and dx2 < 0 and 10000 * dy1 // dx1 < 10000 * dy2 // dx2:
            return -1
        return 1

def can_view(p1, p2, map):
    (x1, y1) = p1
    (x2, y2) = p2
    if not map[p2]:
        return 0
    dx = x2 - x1
    dy = y2 - y1
    d = math.gcd(abs(dx), abs(dy))
    if d == 0:
        return 0
    dx //= d
    dy //= d
    x1 += dx
    y1 += dy
    while x1 != x2 or y1 != y2:
        if map[(x1, y1)]:
            return 0
        x1 += dx
        y1 += dy
    return 1

file = open("data/data10.txt", "rt")

x = y = 0
space = {}

for l in file.readlines():
    for c in l[:-1]:
        space[(x,y)] = True if c == '#' else False
        x += 1
    x = 0
    y += 1

max_view = float('-inf')

for p1 in space:
    if not space[p1]:
        continue
    view = 0
    for p2 in space:
        view += can_view(p1, p2, space)
    if view > max_view:
        max_view = view
        (mx, my) = p1

print("Part 1: {}".format(max_view))

slants = set()

for (x,y) in space:
    dx = x - mx
    dy = y - my
    d = math.gcd(abs(dx), abs(dy))
    if d != 0:
        slants.add((dx // d, dy // d))

shots = 0
while shots != 200:
    for (sx,sy) in sorted(slants, key=functools.cmp_to_key(compare_slants)):
        x = mx + sx
        y = my + sy
        shot = False
        while (x,y) in space:
            if space[(x,y)]:
                shot = True
                space[(x,y)] = False
                shots += 1
                break
            x += sx
            y += sy
        if shots == 200:
            print("Part 2: {}".format(100*x+y))
            break
