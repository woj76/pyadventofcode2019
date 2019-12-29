part2 = True

reactions = {}

file = open("data/data14.txt", "rt")

for l in file.readlines():
    r = l.split(' => ')
    (target_amount, target) = tuple(r[1][:-1].split(' '))
    sources = [(int(a),n) for (a,n) in [tuple(s.split(' ')) for s in r[0].split(', ')]]
    reactions[target] = (int(target_amount), sources)

def add_requirement(name, amount, requirements):
    requirements[name] = amount + (0 if not name in requirements else requirements[name])

def calc_requirements(name, amount, reactions, requirements):
    if name == "ORE":
        return
    (spec_amount, rs) = reactions[name]
    rep = amount // spec_amount
    if amount % spec_amount != 0:
        rep += 1
    add_requirement(name, -rep * spec_amount, requirements)
    for (r_amount, r_name) in rs:
        add_requirement(r_name, rep * r_amount, requirements)
        needed = requirements[r_name]
        if needed > 0:
            calc_requirements(r_name, needed, reactions, requirements)


requirements = {}

calc_requirements("FUEL", 1, reactions, requirements)

if not part2:
    print(requirements["ORE"])
else:
    ore_limit = 1000000000000
    ore_part1 = requirements["ORE"]
    fuel = ore_limit // ore_part1
    while True:
        requirements = {}
        calc_requirements("FUEL", fuel, reactions, requirements)
        inc = (ore_limit - requirements["ORE"]) // ore_part1
        if inc == 0:
            break
        fuel += inc
    print(fuel)
