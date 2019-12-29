import sys

part2 = True

x_max = 25
y_max = 6

file = open("data/data08.txt", "rt")
str = file.readline()[:-1]
file.close()

x = y = 0
layers = []
current_layer = {}

for c in [int(e) for e in str]:
    current_layer[(x,y)] = c
    x += 1
    if x == x_max:
        x = 0
        y += 1
        if y == y_max:
            y = 0
            layers.append(current_layer)
            current_layer = {}

if not part2:
    zero_count = float('inf')
    for l in layers:
        current_count = [0, 0, 0]
        for v in l.values():
            current_count[v] += 1
        if current_count[0] < zero_count:
            zero_count = current_count[0]
            res = current_count[1] * current_count[2]
    print(res)
else:
    for y in range(y_max):
        for x in range(x_max):
            pixel = 0
            for l in range(len(layers)):
                pixel = layers[l][(x,y)]
                if pixel != 2:
                    break
            sys.stdout.write('*' if pixel == 1 else ' ')
        sys.stdout.write('\n')
