import math

def lcm(x, y):
    return x * y // math.gcd(x, y)

def set_speeds(planets):
    for (p1,p2) in [(l1,l2) for l1 in planets for l2 in planets if planets.index(l2) > planets.index(l1)]:
        for xyz in range(3):
            if p1[xyz] > p2[xyz]:
                p1[xyz + 3] -= 1
                p2[xyz + 3] += 1
            elif p1[xyz] < p2[xyz]:
                p1[xyz + 3] += 1
                p2[xyz + 3] -= 1
    for p in planets:
        for i in range(3):
            p[i] += p[i+3]

part2 = True

file = open("data/data12.txt", "rt")

planets = []
for l in file.readlines():
    planets.append([int(s.strip()[2:]) for s in l[1:-2].split(',')] + [0,0,0])

if not part2:
    for _ in range(1000):
        set_speeds(planets)
    energy = 0
    for p in planets:
        energy += sum(map(abs, p[0:3])) * sum(map(abs, p[3:6]))
    print(energy)
else:
    xc = yc = zc = 0
    xs = set()
    ys = set()
    zs = set()
    count = 0
    while xc == 0 or yc == 0 or zc == 0:
        xl = []
        yl = []
        zl = []
        for p in planets:
            xl.append(p[0]); xl.append(p[3])
            yl.append(p[1]); yl.append(p[4])
            zl.append(p[2]); zl.append(p[5])
        xl = tuple(xl)
        yl = tuple(yl)
        zl = tuple(zl)
        if xc == 0 and xl in xs:
            xc = count
        else:
            xs.add(xl)
        if yc == 0 and yl in ys:
            yc = count
        else:
            ys.add(yl)
        if zc == 0 and zl in zs:
            zc = count
        else:
            zs.add(zl)
        set_speeds(planets)
        count += 1
    print(lcm(xc, lcm(yc, zc)))
