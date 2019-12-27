part2 = True

file = open("data/data01.txt", "rt")

nums = [int(x) for x in file.read().split('\n') if x != '']

totalFuel = 0

for n in nums:
    fuel = n // 3 - 2
    if part2:
        extraFuel = fuel // 3 - 2
        while extraFuel >= 0:
            fuel += extraFuel
            extraFuel = extraFuel // 3 - 2
    totalFuel += fuel

print(totalFuel)
