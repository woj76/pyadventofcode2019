part2 = True

def get_orbits(planet, orbits):
    r = []
    while True:
        if planet in orbits.keys():
            planet = orbits[planet]
            r += [planet]
        else:
            break
    return r

orbits = {}

for p in open("data/data06.txt", "rt").readlines():
    [o1, o2] = p[:-1].split(')')
    orbits[o2] = o1

if part2:
    path_length = float('inf')
    dist1 = 0
    san_list = get_orbits("SAN", orbits)
    for p in get_orbits("YOU", orbits):
        if p in san_list:
            path_length = min(path_length, dist1 + san_list.index(p))
        dist1 += 1
    print(path_length)
else:
    print(sum([len(get_orbits(p,orbits)) for p in orbits.keys()]))
