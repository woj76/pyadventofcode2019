part2 = True
count = 0

for pw in [str(p) for p in range(382345, 843167+1)]:
    pair = decreasing = False
    for i in range(1, len(pw)):
        c1, c2 = pw[i-1], pw[i]
        if c1 == c2:
            if not part2 or ((i < 2 or pw[i-2] != c1) and (i > len(pw)-2 or pw[i+1] != c2)):
                pair = True
        elif c1 > c2:
            decreasing = True
    if pair and not decreasing:
        count += 1

print(count)
